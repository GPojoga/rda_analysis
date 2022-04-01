from subprocess import check_output
import pathlib
import argparse
import json

parser = argparse.ArgumentParser(description='Tool for extracting an USN journal.')
parser.add_argument('--drives', type=str, nargs='+', default='all')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def get_drives():
	drives = check_output(['fsutil', 'fsinfo', 'drives'], shell=True).decode('utf-8')
	drives = [drive.strip('\\') for drive in drives.split()[1:]]
	
	valid = []
	invalid = []
	for drive in drives:
		try:
			check_output(
				['fsutil', 'usn', 'queryJournal', drive], 
				shell=True).decode('utf-8')
		except:
			invalid.append(drive)
		else:
			valid.append(drive)
	return valid, invalid		


def get_active_drives(valid, invalid):
	if args.drives == 'all':
		drives = valid
	else:
		for drive in args.drives:
			if not (drive in valid or drive in invalid):
				raise Exception(f'The requested drive {drive} is not present on the device. '
								f'Accessible drives are {valid + invalid}.')
			if drive not in valid:
				raise Exception(f'The USN journal of drive {drive} cannot be accessed.')
		drives = args.drives
	return drives 


def get_raw_usn(drive):
	try:
		output = check_output(['fsutil', 'usn', 'readJournal', f'{drive}'],
							shell=True).decode('utf-8')
		return output
	except Exception as e:
		raise Exception(f'Could not read USN journal for drive {drive}.'
						f'Reason : {e}')


def qualify_usn(entry):
	return 'Usn' in entry \
		and 'File name' in entry \
		and 'Reason' in entry \
		and 'Time stamp' in entry \
		and 'File ID' in entry \
		and 'Parent file ID' in entry


def get_usn(drive):
	usn = [entry.split('\r\n') for entry in get_raw_usn(drive).split('\r\n\r\n')]

	valid = []
	invalid = []

	temp = []
	for entry in usn:
			struct = {}
			for field in entry:
				try:
					key, value = [val.strip() for val in field.split(':', 1)]
					struct[key] = value
				except Exception as e:
					continue
			temp.append(struct)
	usn = temp

	for entry in usn:
		if qualify_usn(entry):
			valid.append(entry)
		else:
			invalid.append(entry)

	return valid, invalid


def filter_fields(usn):
	return [
		{
			'usn': entry['Usn'],
			'name': entry['File name'],
			'reason': entry['Reason'],
			'timestamp': entry['Time stamp'],
			'id': entry['File ID'],
			'parent_id': entry['Parent file ID']
		} for entry in usn
	]


def get_path_by_id(id, drive):
	try:
		output = check_output(['fsutil', 'file', 'queryFileNameById', f'{drive}', f'0x{id}'],
								shell=True).decode('utf-8')
	except:
		return None
	output = output.split('\\\\?\\')
	return output[1].strip() if len(output) == 2 else None


def gen_filenames_id_map(usn):
	usn = usn[::-1]
	mapping = {}
	for entry in usn:
		if entry['id'] not in mapping:
			mapping[entry['id']] = entry
	return mapping


def construct_paths(usn, drive):
	def _lookup(cache, drive, entry):
		if entry['name'] == '.':
			cache[entry['id']] = f'{drive}'
			return f'{drive}'
		if entry['id'] in cache:
			cache_split = cache[entry['id']].split('\\')
			if entry['name'] != cache_split[-1]:
				cache_split[-1] = entry['name']
			cache[entry['id']] = '\\'.join(cache_split)
			return cache[entry['id']]
		
		parent = _lookup(cache, drive, ids[entry['parent_id']]) \
					if entry['parent_id'] in ids else None

		if parent is None:
			parent = get_path_by_id(entry['parent_id'], drive) 
			cache[entry['parent_id']] = parent
		
		path = entry['name'] if parent is None else f'{parent}\{entry["name"]}'
		cache[entry['id']] = path
		return path

	print(f"Mapping USN ids to filenames ... ", end="", flush=True)
	ids = gen_filenames_id_map(usn)
	cache = {}
	print(f"Done!", flush=True)
	
	print(f"Reconstructing file paths for USN Journal of drive {drive} ...", end="", flush=True)
	for entry in usn:
		entry['path'] = _lookup(cache, drive, entry)
	print("Done!", flush=True)

	return usn


def main():
	data = {
		'metadata':{},
		'drives':{}
	}

	valid_drives, invalid_drives = get_drives()
	drives = get_active_drives(valid_drives, invalid_drives)
	
	data['metadata']['valid_drives'] = valid_drives
	data['metadata']['invalid_drives'] = invalid_drives
	data['metadata']['selected_drives'] = drives

	for drive in drives:
		print(f"Extracting the USN Journal for drive {drive} ... ", end="", flush=True)
		valid, invalid = get_usn(drive)
		print("Done!", flush=True)

		data['drives'][drive] = {}
		data['drives'][drive]['invalid'] = invalid

		data['drives'][drive]['valid'] = construct_paths(filter_fields(valid), drive)

	print(f"Storing USN Journals at {args.output} ... ", end='', flush=True)
	pathlib.Path('/'.join(args.output.split('/')[:-1])).mkdir(parents=True, exist_ok=True)
	with open(args.output, 'w+') as output:
		output.write(json.dumps(data, indent=4))
	print(f"Done!", flush=True)


if __name__ == '__main__':
	main()