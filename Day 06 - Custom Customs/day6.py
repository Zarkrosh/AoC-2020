#!/usr/bin/python3

def getPart1Solution(groups):
	reduced = ["".join(set(g.replace("\n", ""))) for g in groups]
	return sum(len(r) for r in reduced)

def getPart2Solution(groups):
	reduced = [[set(l) for l in g.split("\n")] for g in groups]
	return sum([len(set.intersection(*r)) for r in reduced])


# Test
with open("test.txt", "r") as testfile:
	groups = testfile.read().split("\n\n")

assert getPart1Solution(groups) == 11 # Part 1
assert getPart2Solution(groups) == 6  # Part 2


with open("input.txt", "r") as infile:
	groups = infile.read().split("\n\n")

print("[*] Part 1: {}".format(getPart1Solution(groups)))
print("[*] Part 2: {}".format(getPart2Solution(groups)))
