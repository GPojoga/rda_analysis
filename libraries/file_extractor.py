

def extract_file(file_path):
	try:
		with open(file_path, 'r') as fp:
			data = fp.read()
		return data
	except:
		return None
