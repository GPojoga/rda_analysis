import subprocess
import sys
import os
from utils.control import control_parser
import argparse

parser = argparse.ArgumentParser(description='Remote Desktop Application Forensics Toolchain')
parser.add_argument('--skip', action='store_true', 
	help="If the output file of a module is present, skip the module.")
args = parser.parse_args()


CONTROL_FILE = 'module.json'

def run(pipeline, stage, module_name):
	print(f"====== {stage} | {module_name} ======")
	if args.skip and os.path.exists(pipeline[stage][module_name]['output']):
		print(f"Output file already exists. Module Skipped.")
	else:
		module = pipeline[stage][module_name]
		cmd = [
			sys.executable, 
			f"{module['path']}", 
			f"--output", 
			f"{module['output']}",
		]

		if 'input' in module:
			cmd.extend(module['input'])
		
		subprocess.run(cmd, check=True)


def process_dependencies(pipeline, stage, module_name):
	module = pipeline[stage][module_name]
	if 'dependencies' in module:
		for dependency in module['dependencies']:
			execute_module(pipeline, dependency['stage'], dependency['module'])


def execute_module(pipeline, stage, module_name):
	module = pipeline[stage][module_name]
	if module['type'] == 'module' and not module['executed']:
		process_dependencies(pipeline, stage, module_name)
		run(pipeline, stage, module_name)
		module['executed'] = True


def execute_pipeline(pipeline):
	for stage in pipeline:
		for module in pipeline[stage]:
			execute_module(pipeline, stage, module)


def main():
	ctrl = control_parser(CONTROL_FILE)
	execute_pipeline(ctrl)

	print('++++++ Pipeline Complete ++++++')


if __name__ == '__main__':
	main()
