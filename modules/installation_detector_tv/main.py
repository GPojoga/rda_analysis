import json
import sys
import pathlib
import argparse
import importlib

parser = argparse.ArgumentParser(description='Tool for detecting TeamViewer installations.')
parser.add_argument('cwd_path', type=str, help='CWD of the program entry point')
parser.add_argument('fex_path', type=str, help='Path to the File Extractor library')
parser.add_argument('usnj_path', type=str, help='Path to the USN Journal')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

sys.path.append(args.cwd_path)
fex = importlib.import_module(args.fex_path)

def is_usn_create(usn_entry):
	return usn_entry['reason'] == "0x00000100: File create"


def is_usn_delete(usn_entry):
	return usn_entry['reason'] == '0x80000200: File delete | Close'


def is_checkpoint(usn_entry):
	return is_usn_create(usn_entry) or is_usn_delete(usn_entry)


def find_checkpoints(usn):
	relevant = []
	for entry in usn:
		if entry['name'] == 'rolloutfile.tv13' and is_checkpoint(entry) and '$Recycle.Bin' not in entry['path']:
			relevant.append(entry)
	return relevant


def get_rda_id(install_path):
	data = fex.extract_file(f'{install_path}\\rolloutfile.tv13')
	return data.split(',')[0]


def get_installation_data(checkpoints):
	data = {}
	data['timeline'] = []
	for entry in checkpoints:
		if is_usn_create(entry):
			data['timeline'].append({
				'action': 'installed',
				'timestamp': entry['timestamp'],
				'path': '\\'.join(entry['path'].split('\\')[:-1])
			})
		elif is_usn_delete(entry):
			data['timeline'].append({
				'action': 'uninstalled',
				'timestamp': entry['timestamp'],
				'path': '\\'.join(entry['path'].split('\\')[:-1])
			})
		else:
			raise Exception('Error: Unknown event')
			
	data['is_installed'] = len(data['timeline']) > 0 and data['timeline'][-1]['action'] == 'installed'
	data['installation_path'] = data['timeline'][-1]['path'] if data['is_installed'] else None
	data['rda_id'] = get_rda_id(data['installation_path']) if data['is_installed'] else None
	return data


def main():
	print(f"Loading USN Journal ... ", end='', flush=True)
	with open(args.usnj_path, 'r') as usnj:
		usn = json.load(usnj)
	usn = usn['drives']['C:']['valid']
	print('Done!', flush=True)

	print(f'Processing installation data ... ', end='', flush=True)
	checkpoints = find_checkpoints(usn)
	data = get_installation_data(checkpoints)
	print('Done!', flush=True)

	print(f'Storing installation data ... ', end='', flush=True)
	pathlib.Path('/'.join(args.output.split('/')[:-1])).mkdir(parents=True, exist_ok=True)
	with open(args.output, 'w+') as output:
		output.write(json.dumps(data, indent=2))
	print('Done!', flush=True)


if __name__ == '__main__':
	main()

