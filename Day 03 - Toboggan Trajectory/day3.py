#!/usr/bin/python3
import sys
import math

TREE = "#"

def extendMap(currentmap, basemap):
	for i in range(len(currentmap)):
		currentmap[i] += basemap[i]

def countTreesSlope(treemap, basemap, sRight, sDown):
	count = 0

	# Extends the map to the minimum width
	lastX = (len(treemap) / sDown) * sRight
	neededExtends = math.ceil((lastX - len(treemap[0])) / len(basemap[0]))
	for i in range(neededExtends):
		extendMap(treemap, basemap)

	currX = sRight
	for currY in range(sDown, len(treemap), sDown):
		if treemap[currY][currX] == TREE:
			count += 1
		currX += sRight

	return count


with open(sys.argv[1], "r") as infile:
	BASE_MAP = [l.strip() for l in infile.readlines()]

CURRENT_MAP = BASE_MAP.copy()

solution1 = countTreesSlope(CURRENT_MAP, BASE_MAP, 3, 1)
print("[*] Part 1: {}".format(solution1))

solution2 = countTreesSlope(CURRENT_MAP, BASE_MAP, 1, 1)
solution2 *= solution1
solution2 *= countTreesSlope(CURRENT_MAP, BASE_MAP, 5, 1)
solution2 *= countTreesSlope(CURRENT_MAP, BASE_MAP, 7, 1)
solution2 *= countTreesSlope(CURRENT_MAP, BASE_MAP, 1, 2)
print("[*] Part 2: {}".format(solution2))