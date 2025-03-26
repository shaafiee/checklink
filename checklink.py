import requests
import sys

def checkList(file, prefix):
	with open(file) as IF:
		counter = 0
		for line in IF:
			counter += 1
			(origin, redirect) = line.split(f"\s*,\s*")
			print(f"{origin} --> {redirect}")
			returned = requests.get(f"{prefix}{origin}", allow_redirects=True)
			print(returned.url)
			if counter > 10:
				exit()

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please enter the name of a CSV file as first argument")
		print("Optionally, enter a second argument as URL prefix")
		exit()

	try:
		checkList(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else "")
	except:
		print("Error")
