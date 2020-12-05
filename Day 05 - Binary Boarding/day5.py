#!/usr/bin/python3
import sys

def decodeSeat(encodedSeat):
	 row = int(encodedSeat[:7].replace("F", "0").replace("B", "1"), 2)
	 col = int(encodedSeat[7:].replace("L", "0").replace("R", "1"), 2)
	 return (row, col)

def getSeatID(seat):
	return seat[0] * 8 + seat[1]

with open(sys.argv[1], "r") as infile:
	encodedSeats = [l.strip() for l in infile.readlines()]

busySeatsID = []

# Part 1
solution1 = 0
for encodedSeat in encodedSeats:
	id = getSeatID(decodeSeat(encodedSeat))
	if id > solution1:
		solution1 = id
	busySeatsID.append(id)
print("[*] Part 1: {}".format(solution1))

# Part 2
busySeatsID.sort()
for i in range(busySeatsID[0], busySeatsID[-1] + 1):
	if not i in busySeatsID:
		print("[*] Part 2: {}".format(i))
