import argparse
import pathlib
import json
import re 

parser = argparse.ArgumentParser(description='Tool for extracting Prefetch traces.')
parser.add_argument('usnj_path', type=str, help='Path to the USN Journal')
parser.add_argument('--output', type=str, required=True)
parser.add_argument('--drive', type=str, required=False, default='C:')
args = parser.parse_args()


def get_prefetch_entries(usn):
	entries = []
	for entry in usn:
		match = re.search('Windows\\\\Prefetch\\\\(.+?).pf', entry['path'])
		if match:
			exe, loc_hash = match.group(1).rsplit('-', 1) 
			entries.append({
				'timestamp' : entry['timestamp'],
				'executable' : exe,
				'location_hash' : loc_hash
			})
	return entries


def main():
	print("Loading USN Journal ... ", end='', flush=True)
	with open(args.usnj_path, 'r') as usnj:
		usn = json.load(usnj)
	print('Done!', flush=True)

	print('Extracting Prefetch data ... ', end='', flush=True)
	prefetch = get_prefetch_entries(usn['drives'][args.drive]['valid'])
	print('Done!', flush=True)

	print('Storing Prefetch data ... ', end='', flush=True)
	pathlib.Path('/'.join(args.output.split('/')[:-1])).mkdir(parents=True, exist_ok=True)
	with open(args.output, 'w+') as out:
		out.write(json.dumps(prefetch, indent=2))
	print('Done!', flush=True)
		

if __name__ == '__main__':
	main()