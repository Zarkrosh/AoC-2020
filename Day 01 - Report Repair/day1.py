#!/usr/bin/python3

with open("input.txt", "r") as infile:
	numbers = [int(n) for n in infile.readlines()]

# Part 1
for i in range(len(numbers) - 1):
	for j in range(i+1, len(numbers)):
		if numbers[i] + numbers[j] == 2020:
			print("[*] Part 1: {} * {} = {}".format(numbers[i], numbers[j], numbers[i] * numbers[j]))


"""
Part 2:
	https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
	1. Sort the given array.
	2. Loop over the array and fix the first element of the possible triplet, arr[i].
	3. Then fix two pointers, one at i + 1 and the other at n - 1. And look at the sum,
		3.1. If the sum is smaller than the required sum, increment the first pointer.
		3.2. Else, If the sum is bigger, Decrease the end pointer to reduce the sum.
		3.3. Else, if the sum of elements at two-pointer is equal to given sum then print the triplet and break
"""
numbers.sort()
for i in range(len(numbers)-1):
	relSum = 2020 - numbers[i]
	lower = i + 1
	upper = len(numbers) - 1
	
	exit = False
	while not exit:
		add = numbers[upper] + numbers[lower]
		if add < relSum: 
			lower += 1
		elif add > relSum:
			upper -= 1
		else:
			print("[*] Part 2: {} * {} * {} = {}".format(numbers[i], numbers[lower], numbers[upper], numbers[i] * numbers[lower] * numbers[upper]))
			exit = True

		if lower >= upper or lower == len(numbers) or upper == i: exit = True