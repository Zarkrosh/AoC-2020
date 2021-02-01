#!/usr/bin/python3
from copy import deepcopy

FLOOR = "."
EMPTY = "L"
OCCUPIED = "#"
DIRECTIONS = [(i,j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]

def parseInput(filename):
    with open(filename, "r") as infile:
        return [list(s.strip()) for s in infile.readlines()]

def getNextState(seatsMap, tolerance, adjacentSeats):
    changed = False
    nMapa = deepcopy(seatsMap)
    for iRow in range(len(seatsMap)):
        for iCol in range(len(seatsMap[0])):
            caringSeats = []
            if adjacentSeats:
                # Cares about the adjacent seats in every direction
                caringSeats = [(iCol+adj[0], iRow+adj[1]) for adj in DIRECTIONS if iCol + adj[0] >= 0 and iCol + adj[0] < len(seatsMap[0]) and iRow + adj[1] >= 0 and iRow + adj[1] < len(seatsMap)]
            else:
                # Cares about the first available seat in every direction
                for dir in DIRECTIONS:
                    cCol = iCol
                    cRow = iRow
                    stop = False
                    while not stop:
                        cCol += dir[0]
                        cRow += dir[1]
                        if cCol >= 0 and cCol < len(seatsMap[0]) and cRow >= 0 and cRow < len(seatsMap):
                            if seatsMap[cRow][cCol] == OCCUPIED or seatsMap[cRow][cCol] == EMPTY:
                                caringSeats.append((cCol, cRow))
                                stop = True
                        else:
                            stop = True
                    
            nOccupied = sum(1 if seatsMap[a[1]][a[0]] == OCCUPIED else 0 for a in caringSeats)
            if seatsMap[iRow][iCol] == EMPTY and nOccupied == 0:
                nMapa[iRow][iCol] = OCCUPIED
                changed = True
            elif seatsMap[iRow][iCol] == OCCUPIED and nOccupied >= tolerance:
                nMapa[iRow][iCol] = EMPTY
                changed = True
    return (nMapa, changed)

def getSolution(seatsMap, tolerance, adjacentSeats):
    hasChanged = True
    while hasChanged:
        seatsMap, hasChanged = getNextState(seatsMap, tolerance, adjacentSeats)
    return sum(1 if seatsMap[i][j] == OCCUPIED else 0 for i in range(len(seatsMap)) for j in range(len(seatsMap[0])))

def getPart1Solution(seatsMap):
    return getSolution(seatsMap, 4, True)

def getPart2Solution(seatsMap):
    return getSolution(seatsMap, 5, False)



# Tests
seatsMap = parseInput("test.txt")
assert getPart1Solution(seatsMap) == 37
assert getPart2Solution(seatsMap) == 26

# Challenge
seatsMap = parseInput("input.txt")
print("[*] Solution 1: {}".format(getPart1Solution(seatsMap)))
print("[*] Solution 2: {}".format(getPart2Solution(seatsMap)))