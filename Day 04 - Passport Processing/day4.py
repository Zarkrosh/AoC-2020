#!/usr/bin/python3
import sys
import re

"""
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
"""
def isValidNumber(s, least, most):
	res = False
	try:
		num = int(s)
		if num >= least and num <= most: res = True
	except:
		pass
	return res

def isValidBirthYear(s):
	return isValidNumber(s, 1920, 2002)

def isValidIssueYear(s):
	return isValidNumber(s, 2010, 2020)

def isValidExpirationYear(s):
	return isValidNumber(s, 2020, 2030)

def isValidHeight(s):
	valid = False
	try:
		measure = s[-2:]
		value = int(s[:-2])
		if measure == "cm" and value >= 150 and value <= 193: valid = True
		elif measure == "in" and value >= 59 and value <= 76: valid = True
	except:
		pass
	return valid

def isValidHair(s):
	return re.match(HAIR_REGEX, s) != None

def isValidEyeColor(s):
	return s in EYE_TYPES

def isValidPassportID(s):
	return re.match(PASSPORT_ID_REGEX, s) != None

MANDATORY_FIELDS = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
FIELDS_CHECK = [isValidBirthYear, isValidIssueYear, isValidExpirationYear, isValidHeight, isValidHair, isValidEyeColor, isValidPassportID]

HAIR_REGEX = re.compile("^#[0-9a-f]{6}$")
EYE_TYPES = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
PASSPORT_ID_REGEX = re.compile("^[0-9]{9}$")



with open(sys.argv[1], "r") as infile:
	rawPassports = infile.read().split("\n\n")

# Generate passports
passports = []
for p in rawPassports:
	passport = dict()
	f = p.split("\n")
	for l in f:
		fields = l.split()
		for field in fields:
			k = field.split(":")[0].lower()
			v = field.split(":")[1].lower()
			passport[k] = v

	passports.append(passport)


# Part 1
solution1 = 0
for passport in passports:
	valid = True
	for field in MANDATORY_FIELDS:
		k = passport.keys()
		if not field in k:
			valid = False
			break

	if valid:
		solution1 += 1

print("[*] Part 1: {}".format(solution1))


# Part 2
solution2 = 0
for passport in passports:
	valid = True
	for i in range(len(MANDATORY_FIELDS)):
		field = MANDATORY_FIELDS[i]
		if not field in passport.keys() or not FIELDS_CHECK[i](passport[field]):
			valid = False
			break

	if valid:
		solution2 += 1

print("[*] Part 2: {}".format(solution2))
