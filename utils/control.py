import os
import pathlib
import json 

def add_dependencies(ctrl, stage, mod_name):
	module = ctrl[stage][mod_name]
	dep_args = []
	library_present = False
	for dependency in module['dependencies']:
		if 'module' not in dependency:
			raise Exception(f'Error: Unable to process ({mod_name}) dependencies. '
							'module is missing')
		
		if dependency['stage'] not in ctrl or \
		   dependency['module'] not in ctrl[dependency['stage']]:
			raise Exception(f'Error: The dependency {dependency["stage"]}:'
							f'{dependency["module"]}, '
							f'of module {mod_name} does not exist')

		dep = ctrl[dependency['stage']][dependency['module']]  	
		dep_args.append(dep['path' if dep['type'] == 'library' else 'output'])
		if dep['type'] == 'library':
			library_present = True
	module['input'] = [*dep_args, *module['input']] if 'input' in module else dep_args
	if library_present:
		module['input'] = [str(pathlib.Path.cwd()), *module['input']]


def control_parser(control_file):
	with open(control_file, 'r') as control:
		ctrl = json.load(control)

	for stage in ctrl:
		for mod_name in ctrl[stage]:
			module = ctrl[stage][mod_name]
			if not os.path.exists(module['path']):
				raise Exception(f"The module path {module['path']} does not exist")
			if module['type'] == 'module':
				module['executed'] = False
			if module['type'] == 'library':
				module['path'] = '.'.join(module['path'].split('.')[0].split('/'))
			if 'dependencies' in module:
				add_dependencies(ctrl, stage, mod_name)
	return ctrl
