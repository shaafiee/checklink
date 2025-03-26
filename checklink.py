import requests
import sys
import traceback
import json
import re

def checkList(file, prefix):
	with open(file) as IF:
		incorrect = []
		counter = 0
		success = 0
		fail = 0
		for line in IF:
			(origin, redirect) = line.split(",")
			#origin = f"{prefix}{origin}"
			redirect = redirect.replace("\n", "")
			try:
				returned = requests.get(f"{prefix}{origin}", allow_redirects=True)
				if re.match(r"^.*" + redirect + ".*", returned.url):
					success += 1
					print(f"[OK] {origin} --> {redirect}")
				else:
					incorrect.append({"origin": origin, "redirect": redirect})
					fail += 1
					print(f"[ERROR] {origin} --> {redirect}")
			except:
				fail += 1
				pass
			counter += 1
		successRate = int((success / counter) * 100)
		print("\n")
		print(f"{successRate}% success")
		if successRate < 100:
			print(f"Check errors.json")
		print("\n")
		with open("errors.json", "w") as WF:
			WF.write(json.dumps(incorrect))

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please enter the name of a CSV file as first argument")
		print("Optionally, enter a second argument as URL prefix")
		exit()

	try:
		checkList(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else "")
	except:
		print("=========================ERROR!=========================")
		print("========================================================")
		print(traceback.format_exc())
		print("========================================================")
