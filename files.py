import os
import csv

os.path.join("Users", "Jake", "Desktop", "FitPy", "PyPrac", "test.txt")

with open("test.txt", "w") as f:
	f.write("Hi from Python!")

my_list = list ()

with open("test.txt", "r") as f:
	my_list.append(f.read())

print(my_list)

with open("test.csv", "w", newline='') as f:
	w = csv.writer(f, delimiter=",")
	w.writerow(["one", "two", "three"])
	w.writerow(["four", "five", "six"])

with open("test.csv", "r") as f:
	r = csv.reader(f, delimiter=",")
	for row in r:
		print(",".join(row))