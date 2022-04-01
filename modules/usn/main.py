from subprocess import check_output
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
				['fsutil', 'usn', 'queryJournal', drive], shell=True).decode('utf-8')
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
			if drive not in valid or drive not in invalid:
				raise Exception(f'The requested drive {drive} is not present on the device.'
								f'Accessible drives are {present_drives}.')
			if drive not in valid:
				raise Exception(f'The USN journal of drive {drive} cannot be accessed.')
		drives = args.drives
	return drives 


def get_raw_usn(drive):
	try:
		return check_output(['fsutil', 'usn', 'readJournal', f'{drive}'],
							shell=True).decode('utf-8')
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
			'time_stamp': entry['Time stamp'],
			'id': entry['File ID'],
			'parent_id': entry['Parent file ID']
		} for entry in usn
	]


def construct_paths(usn, drive):
	def _lookup(cache, drive, entry):
		if entry['id'] in cache:
			return cache[entry['id']]
		if entry['name'] == '.':
			cache[entry['id']] = f'{drive}'
			return f'{drive}'
		
		parent_path = None if entry['parent_id'] not in ids 
						else _lookup(cache, drive, ids[entry['parent_id']])
		current_path = None if parent_path is None else f'{parent_path}\{entry["name"]}'

		cache[entry['id']] = current_path
		return current_path

	ids = {entry['id'] : entry for entry in usn}
	cache = {}
	
	for entry in usn:
		entry['path'] = _lookup(cache, drive, entry)
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
		valid, invalid = get_usn(drive)
		data['drives'][drive] = {}
		data['drives'][drive]['invalid'] = invalid
		data['drives'][drive]['valid'] = construct_paths(filter_fields(valid), drive)

	with open(args.output, 'w') as output:
		output.write(json.dumps(data, indent=4))


if __name__ == '__main__':
	main()