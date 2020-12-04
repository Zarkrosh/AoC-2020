#!/usr/bin/python3

with open("input.txt", "r") as infile:
	lines = [l.strip() for l in infile.readlines()]

# Part 1
count1 = 0
count2 = 0
for line in lines:
	fields = line.split()
	numbers = fields[0].split("-")
	firstNumber = int(numbers[0])  # Part 1 -> lowest occurrence  | Part 2 -> first position
 	secondNumber = int(numbers[1]) # Part 1 -> highest occurrence | Part 2 -> second position
	letter = fields[1][0]
	password = fields[2]

	# Part 1
	occurences = password.count(letter)
	if occurences >= firstNumber and occurences <= secondNumber:
		count1 += 1

	# Part 2
	firstLetter = password[firstNumber - 1]
	secondLetter = password[secondNumber - 1]
	if (firstLetter == letter or secondLetter == letter) and firstLetter != secondLetter:
		count2 += 1 

print("[*] Part 1: {}".format(count1))
print("[*] Part 2: {}".format(count2))
