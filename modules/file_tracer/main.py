import argparse
import json
from datetime import datetime

parser = argparse.ArgumentParser(description='Tool for tracing the files modified'
											'during RDA connections.')

parser.add_argument('usnj_path', type=str, help='Path to the USN Journal')
parser.add_argument('connect_path', type=str, help='Path to the connections information')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def get_file_trace(connection, usn):
	start = datetime.strptime(connection['connection_start'], '%Y-%m-%d %H:%M:%S')
	end = datetime.strptime(connection['connection_end'], '%Y-%m-%d %H:%M:%S')
	
	tracer_entry = {
		'connection_no': connection['no'],
		'drives': {}
	}
	for drive in usn['drives']:
		tracer_entry['drives'][drive] = []
		for entry in usn['drives'][drive]['valid']:
			entry_time = datetime.strptime(entry['timestamp'], '%d/%m/%Y %H:%M:%S')
			if entry_time >= start and entry_time <= end:
				tracer_entry['drives'][drive].append({
					'file_path': entry['path'],
					'reason': entry['reason'].split(':')[1].strip()
				})
	return tracer_entry


def main():
	print('Loading USN Journal ... ', end='', flush=True)
	with open(args.usnj_path, 'r') as file:
		usn = json.load(file)
	print('Done!', flush=True)
	print('Loading Connection data ... ', end='', flush=True)
	with open(args.connect_path, 'r') as file:
		connections = json.load(file)
	print('Done!', flush=True)

	if len(connections) == 0:
		print('Warning: No connections detected ... Abort!')
		return

	print('Tracing files modified during connections ... ', end='', flush=True)	
	trace = [get_file_trace(connection, usn) for connection in connections]
	print('Done!')
	
	print('Storing tracing results ... ', end='', flush=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(trace, indent=2))
	print('Done!', flush=True)
		

if __name__ == '__main__':
	main()