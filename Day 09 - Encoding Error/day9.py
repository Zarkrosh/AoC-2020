#!/usr/bin/python3

def parseInput(filename):
    with open(filename, "r") as infile:
        return [int(n) for n in infile.readlines()]

def getPart1Solution(numbers, n):
    cache = []
    for i in range(n-1):
        temp = []
        for j in range(i+1, n+i):
            temp.append(numbers[i] + numbers[j])
        cache.append(temp)

    for index in range(n, len(numbers)):
        number = numbers[index]
        valid = False
        for i in range(n-1):
            if number in cache[i][:n-i-1]:
                valid = True
                break

        if not valid:
            return number
        else:
            # Builds next cache
            cache.pop(0)
            temp = []
            for i in range(n-1):
                temp.append(numbers[index-1] + numbers[index+i])
            cache.append(temp)

def getPart2Solution(numbers, target):
    baseIndex = 0
    maxIndex = len(numbers)
    size = 1
    accum = numbers[0]
    while baseIndex < maxIndex:
        add = accum + numbers[baseIndex+size]
        if add == target:
            # Found
            solutionSet = numbers[baseIndex:baseIndex+size+1]
            return min(solutionSet) + max(solutionSet) 
        elif add < target:
            # Increase set
            accum = add
            size += 1
        elif add > target:
            # Decreases set forward
            accum -= numbers[baseIndex]
            size -= 1
            baseIndex += 1

    return None


# Test
numbers = parseInput("test.txt")
solution1 = getPart1Solution(numbers, 5)
assert solution1 == 127
assert getPart2Solution(numbers, solution1) == 62


numbers = parseInput("input.txt")
solution1 = getPart1Solution(numbers, 25)
print("[*] Part 1: {}".format(solution1))
print("[*] Part 2: {}".format(getPart2Solution(numbers, solution1)))
