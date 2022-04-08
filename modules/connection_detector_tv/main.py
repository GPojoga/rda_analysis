
import argparse
import sys
import json
import importlib
import datetime
import re


parser = argparse.ArgumentParser(description='Tool for detecting TeamViewer Connections.')
parser.add_argument('cwd_path', type=str, help='CWD of the program entry point')
parser.add_argument('fex_path', type=str, help='Path to the File Extractor library')
parser.add_argument('event_path', type=str, help='Path to the Event Data')
parser.add_argument('install_path', type=str, help='Path to the Installation Data')
parser.add_argument('--utc', type=int, help='Connection logs are in UTC+0.'
					' If the local time is different specify it as a signed'
					' integer from UTC. Default is 0.', default=0)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

sys.path.append(args.cwd_path)
fex = importlib.import_module(args.fex_path)


def get_connections(cwd):
	
	raw = fex.extract_file(f'{cwd}\\Connections_incoming.txt')
	if raw is None:
		return None

	connections = [x.strip() for x in raw.split('\n') if x.strip() != '']

	conn_struct = []

	counter = 0
	for entry in connections:
		entry_data = entry.split('\t')
		conn_struct.append({
			'no': counter,
			'remote_rda_id': entry_data[0],
			'connection_start': str(
				datetime.datetime.strptime(entry_data[2], "%d-%m-%Y %H:%M:%S") + 
				datetime.timedelta(hours=args.utc)
									),
			'connection_end': str(
				datetime.datetime.strptime(entry_data[3], "%d-%m-%Y %H:%M:%S") + 
				datetime.timedelta(hours=args.utc)
								),
			'remote_user': entry_data[4]
		})
		counter += 1
	return conn_struct


def check_timestamp(connection, elem):
	elem_time = datetime.datetime.strptime(
					elem['date'].split('.')[0], '%Y-%m-%dT%H:%M:%S'
				)
	conn_start = datetime.datetime.strptime(
					connection['connection_start'], '%Y-%m-%d %H:%M:%S'
				)
	conn_end = datetime.datetime.strptime(
					connection['connection_end'], '%Y-%m-%d %H:%M:%S'
				)
	return elem_time > conn_start and elem_time < conn_end


def check_description(connection, elem):
	descr = elem['description'].split('\r\n')
	return 	descr[0].strip() == 'The Windows Filtering Platform has permitted a connection.' and \
			descr[7].split(':')[1].strip() == 'Outbound' and \
			descr[4].split('\\')[-1].strip() == 'teamviewer_service.exe'


def get_remote_ip(connection, events):
	security = events['Security']['valid']
	results = []
	for elem in security:
		if elem['source'] == 'Microsoft-Windows-Security-Auditing':
			if check_timestamp(connection, elem):
				if check_description(connection, elem):
					results.append(elem)
	
	ips = []
	for result in results:
		descr = result['description'].split('\r\n')
		ips.append(f"{descr[10].split(':')[-1].strip()}:{descr[11].split(':')[-1].strip()}")
	return [ip for ip in ips if bool(re.match('\d+\.\d+\.\d+\.\d+.:\d+', ip))]


def main():
	with open(args.install_path, 'r') as file:
		install_data = json.load(file)
	with open(args.event_path, 'r') as file:
		event_data = json.load(file)
	if not install_data['is_installed']:
		print("No installation detected ... Abort!")
		return
	
	print('Extracting connection data ... ', end='', flush=True)
	connections = get_connections(install_data['installation_path'])	
	if connections is None:
		print("Warning: Could not detect any connection")
		return
	print('Done!', flush=True)

	print('Identifying possible remote IP addresses .. .', end='', flush=True)
	for connection in connections:
		connection['possible_remote_ips'] = get_remote_ip(connection, event_data)
	print('Done!', flush=True)

	print('Storing connection data ... ', end='', flush=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(connections, indent=2))
	print('Done!', flush=True)


if __name__ == '__main__':
	main()
