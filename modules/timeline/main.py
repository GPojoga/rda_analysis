import argparse
import pathlib
import sqlite3
import json

parser = argparse.ArgumentParser(description='Tool for extracting the Windows Timeline')
parser.add_argument('--username', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def main():
	print("Extracting ActivitiesCache.db ... ", end='')
	with sqlite3.connect(f"C:/Users/{args.username}/AppData/Local/ConnectedDevicesPlatform/L.{args.username}/ActivitiesCache.db") as database:
		cursor = database.cursor()
		data = cursor.execute("SELECT * FROM Activity").fetchall()
		fields = [x[0] for x in cursor.description]
	print("Done!")
	
	print(f'Storing Windows Timeline at {args.output} ... ', end='')
	pathlib.Path('/'.join(args.output.split('/')[:-1])).mkdir(parents=True, exist_ok=True)
	with open(args.output, 'w+') as file:
		file.write(json.dumps(
			[{fields[i] : int.from_bytes(entry[i], 'big') 
						if type(entry[i]) is bytes else entry[i]
							for i in range(len(entry))} for entry in data],
			indent=2))
	print("Done!")
	
			

if __name__ == "__main__":
	main()