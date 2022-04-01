import argparse

parser = argparse.ArgumentParser(description='Tool for detecting TeamViewer installations.')
parser.add_argument('file_extractor', type=str, help='File extraction library')
parser.add_argument('usnj_path', type=str, help='Path to the USN Journal')
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()


def main():
	pass


if __name__ == '__main__':
	main()

