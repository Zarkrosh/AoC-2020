#!/usr/bin/python3

TARGET_BAG = "shiny gold"
REACH_TABLE = dict()

def parseBags(filename):
    with open(filename, "r") as infile:
        bagList = [l.strip() for l in infile.readlines()]

    bags = dict()
    for b in bagList:
        parts = b.split(" contain ")
        container = " ".join(parts[0].split()[:-1]) # Removes bags part
        contained = []
        if not "no other bags" in parts[1]:
            for c in parts[1][:-1].split(", "):
                number = int(c.split()[0])
                containedBag = " ".join(p for p in c.split()[1:-1]) # Removes bag/bags part
                contained.append((number, containedBag))
        bags[container] = contained
    return bags

def reachesTargetBag(bags, currentBag):
    if REACH_TABLE[currentBag] != None:
        return REACH_TABLE[currentBag]

    contained = bags[currentBag]
    if len(contained) == 0:
        REACH_TABLE[currentBag] = False
    elif any('shiny gold' in c for c in contained):
        REACH_TABLE[currentBag] = True
    else:
        for (n, b) in contained:
            if reachesTargetBag(bags, b):
                REACH_TABLE[currentBag] = True
                return True # Doesn't check the others
        REACH_TABLE[currentBag] = False

    return REACH_TABLE[currentBag]

def getPart1Solution(bags):
    for k in bags.keys():
        REACH_TABLE[k] = None
    return sum(1 for k in bags.keys() if reachesTargetBag(bags, k))

def getPart2Solution(bags, currentBag):
    solution = 0
    for containedBag in bags[currentBag]:
        number = containedBag[0]
        solution += number + number * getPart2Solution(bags, containedBag[1])
    return solution

# Test
bags = parseBags("test.txt")
assert getPart1Solution(bags) == 4               # Part1
assert getPart2Solution(bags, TARGET_BAG) == 32  # Part2

# Test 2
bags = parseBags("test2.txt")
assert getPart2Solution(bags, TARGET_BAG) == 126 # Part2

# Challenge
bags = parseBags("input.txt")
print("[*] Part 1: {}".format(getPart1Solution(bags)))
print("[*] Part 2: {}".format(getPart2Solution(bags, TARGET_BAG)))
