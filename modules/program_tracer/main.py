import argparse
import json
from datetime import datetime


parser = argparse.ArgumentParser(description='Tool for tracing the programs executed'
											'during RDA connections.')

parser.add_argument('timeline_path', type=str, help='Path to the Timeline data')
parser.add_argument('connect_path', type=str, help='Path to the connections information')
parser.add_argument('prefetch_path', type=str, help='Path to the prefetch information')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def get_from_prefetch(connection, prefetch):
	start = datetime.strptime(connection['connection_start'], '%Y-%m-%d %H:%M:%S')
	end = datetime.strptime(connection['connection_end'], '%Y-%m-%d %H:%M:%S')

	execs = []
	for entry in prefetch:
		exec_time = datetime.strptime(entry['timestamp'], '%d/%m/%Y %H:%M:%S')
		if exec_time >= start and exec_time <= end:
			execs.append(entry)
	
	return execs


def get_from_timeline(connection, timeline):
	start = datetime.strptime(connection['connection_start'], '%Y-%m-%d %H:%M:%S')
	end = datetime.strptime(connection['connection_end'], '%Y-%m-%d %H:%M:%S')
	execs = []
	for entry in timeline:
		exec_time = datetime.fromtimestamp(entry['StartTime'])
		if exec_time >= start and exec_time <= end:
			execs.append(entry)
	
	return execs


def main():
	print('Loading dependencies ... ', end='', flush=True)
	with open(args.timeline_path, 'r') as file:
		timeline = json.load(file)
	with open(args.connect_path, 'r') as file:
		connections = json.load(file)
	with open(args.prefetch_path, 'r') as file:
		prefetch = json.load(file)
	print('DONE!', flush=True)

	if len(connections) == 0:
		print('Warning: No connection detected ... Abort!')
		return

	print('Tracing program data ... ', end='', flush=True)
	result = []
	for i in range(len(connections)):
		result.append({
			"connection_no": i,
			"prefetch_data": get_from_prefetch(connections[i], prefetch),
			"timeline_data": get_from_timeline(connections[i], timeline)
		})
	for entry in result:
		for res in entry['timeline_data']:
			res['StartTime'] = str(datetime.fromtimestamp(res['StartTime']))
			res['LastModifiedTime'] = str(datetime.fromtimestamp(res['LastModifiedTime']))
			res['ExpirationTime'] = str(datetime.fromtimestamp(res['ExpirationTime']))
			res['EndTime'] = str(datetime.fromtimestamp(res['EndTime']))
			res['LastModifiedOnClient'] = str(datetime.fromtimestamp(res['LastModifiedOnClient']))
	print('Done!', flush=True)

	print('Storing collected data', end='', flush=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(result, indent=2))
	print('Done!')

if __name__ == "__main__":
	main()