import argparse
import json
import pathlib

parser = argparse.ArgumentParser(description='Tool for compiling the report')

parser.add_argument('install_path', type=str, help='Path to the Timeline data')
parser.add_argument('connect_path', type=str, help='Path to the connections information')
parser.add_argument('file_trace_path', type=str, help='Path to the file information')
parser.add_argument('program_path', type=str, help='Path to the program information')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def main():
	print('Loading dependencies ... ', end='', flush=True)
	with open(args.install_path, 'r') as file:
		install_data = json.load(file)
	with open(args.connect_path, 'r') as file:
		connect_data = json.load(file)
	with open(args.file_trace_path, 'r') as file:
		file_data = json.load(file)
	with open(args.program_path, 'r') as file:
		program_data = json.load(file)
	print('Done!', flush=True)

	print('Compiling the report ... ', end='', flush=True)
	report = {
		'installation': install_data,
		'connections': connect_data,
		'file trace': file_data,
		'program trace': program_data
	}
	print('Done!', flush=True)
	
	print('Storing the report ... ', end='', flush=True)
	pathlib.Path('/'.join(args.output.split('/')[:-1])).mkdir(parents=True, exist_ok=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(report, indent=2))
	print('Done!', flush=True)


if __name__ == '__main__':
	main()
