from subprocess import check_output
import argparse
import json
import re

parser = argparse.ArgumentParser(description='Tool for extracting windows Events')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def get_evt_sources():
	raw_logs = check_output(['wevtutil', 'enum-logs'], shell=True).decode('utf-8')
	raw_logs = raw_logs.split('\r\n')
	return [x for x in raw_logs if x != '']


def get_raw_events(evt_source):
	return check_output([
			'wevtutil', 
			'query-events', 
			evt_source, 
			'/rd:false', 
			'/format:text']).decode('utf-8', 'replace')


def process_events(raw_evt):
	events = re.split('Event\[\d+\]:\r\n', raw_evt)
	processed = []
	skipped = []
	for event in events:
		try:
			processed.append({
				'log_name' : re.search('Log Name:(.+?)\r\n', event).group(1).strip(),
				'source' : re.search('Source:(.+?)\r\n', event).group(1).strip(),
				'date': re.search('Date:(.+?)\r\n', event).group(1).strip(),
				'event_id': re.search('Event ID:(.+?)\r\n', event).group(1).strip(),
				'task': re.search('Task:(.+?)\r\n', event).group(1).strip(),
				'level': re.search('Level:(.+?)\r\n', event).group(1).strip(),
				'opcode': re.search('Opcode:(.+?)\r\n', event).group(1).strip(),
				'keyword': re.search('Keyword:(.+?)\r\n', event).group(1).strip(),
				'user': re.search('User:(.+?)\r\n', event).group(1).strip(),
				'username': re.search('User Name:(.+?)\r\n', event).group(1).strip(),
				'computer': re.search('Computer:(.+?)\r\n', event).group(1).strip(),
				'description': event.split('Description:', 1)[1].strip(),
			})
		except Exception as e:
			skipped.append(event)
	return processed, skipped


def get_events(event_source):
	return process_events(get_raw_events(event_source))


def main():
	print("Identifying event sources ... ", end='', flush=True)
	sources = get_evt_sources()
	print('Done!', flush=True)

	events = {}
	for source in sources:
		print(f"Extracting ({source}) ... ", end='', flush=True)
		events[source] = {}
		events[source]['valid'], events[source]['invalid'] = get_events(source)
		print("Done!", flush=True)

	print(f"Storing events ... ", end='', flush=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(events, indent=2))
	print("Done!", flush=True)


if __name__ == "__main__":
	main()