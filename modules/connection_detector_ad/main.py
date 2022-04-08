
import argparse
import sys
import json
import importlib
import datetime
import re


parser = argparse.ArgumentParser(description='Tool for detecting AnyDesk Connections.')
parser.add_argument('cwd_path', type=str, help='CWD of the program entry point')
parser.add_argument('fex_path', type=str, help='Path to the File Extractor library')
parser.add_argument('install_path', type=str, help='Path to the Installation Data')
parser.add_argument('--utc', type=int, help='Connection logs are in UTC+0.'
					' If the local time is different specify it as a signed'
					' integer from UTC. Default is 0.', default=0)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

sys.path.append(args.cwd_path)
fex = importlib.import_module(args.fex_path)


def get_connections():
	
	raw = fex.extract_file(f'C:\\ProgramData\\AnyDesk\\ad_svc.trace')
	data = [[x for x in line.split(' ') if x != ''] for line in raw.split('\n')]
	relevant = []
	for entry in data:
		if len(entry) > 12:
			if f'{entry[9]} {entry[10]} {entry[11]}' == 'Logged in from' or \
				f'{entry[9]} {entry[10]}' == 'Session closed':
				relevant.append(entry)

	connections = []
	counter = 0
	for i in range(0, len(relevant), 2):
		connections.append({
			'no': counter,
			'remote_ip': relevant[i][12],
			'connection_start': str(
				datetime.datetime.strptime(f'{relevant[i][1]} {relevant[i][2].split(".")[0]}', "%Y-%m-%d %H:%M:%S") + 
				datetime.timedelta(hours=args.utc)
									),
			'connection_end': str(
				datetime.datetime.strptime(f'{relevant[i + 1][1]} {relevant[i + 1][2].split(".")[0]}', "%Y-%m-%d %H:%M:%S") + 
				datetime.timedelta(hours=args.utc)
									),
		})
		counter += 1
	return connections


def get_time(entry):
	try:
		return datetime.datetime.strptime(f'{entry[1]} {entry[2].split(".")[0]}', "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=args.utc)
	except:
		return None


def update_client_data(connection, install_path):
	raw = fex.extract_file(f'{install_path}\\ad.trace')
	data = raw.split('\n')
	data = [[x.strip() for x in line.split(' ') if x.strip() != ''] for line in raw.split('\n')]
	connection_start = datetime.datetime.strptime(connection['connection_start'], "%Y-%m-%d %H:%M:%S")
	connection_end = datetime.datetime.strptime(connection['connection_end'], "%Y-%m-%d %H:%M:%S")
	debug = []
	for entry in data:
		log_time = get_time(entry)
		if log_time is not None and log_time >= connection_start and log_time <= connection_end:
			debug.append(entry)
			if len(entry) > 10 and f'{entry[8]} {entry[9]} {entry[10]}' == 'Incoming session request:':
				connection['remote_user'] = entry[11]
				connection['remote_rda_id'] = entry[12][1:-1]
			elif len(entry) > 9 and f'{entry[8]} {entry[9]}' == 'Remote OS:':
				connection['remote_os'] = entry[10]
			elif len(entry) > 9 and f'{entry[8]} {entry[9]}' == 'Remote version:':
				connection['remote_version'] = entry[10]


def main():
	with open(args.install_path, 'r') as file:
		install_data = json.load(file)
	if not install_data['is_installed']:
		print("No installation detected ... Abort!")
		return
	
	print('Extracting connection data ... ', end='', flush=True)
	connections = get_connections()	
	if connections is None:
		print("Warning: Could not detect any connection")
		return
	print('Done!', flush=True)

	print('Extracting remote client data .. .', end='', flush=True)
	for connection in connections:
		update_client_data(connection, install_data['installation_path'])
	print('Done!', flush=True)

	print('Storing connection data ... ', end='', flush=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(connections, indent=2))
	print('Done!', flush=True)


if __name__ == '__main__':
	main()
