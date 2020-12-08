#!/usr/bin/python3

class Computer:
    def __init__(self, instructions):
        self.accumulator = 0
        self.instructions = instructions
        self.executed = [False] * len(instructions)
        self.lastInstruction = len(instructions) - 1
        self.ip = 0

    def nextInstruction(self):
        if self.ip > self.lastInstruction or self.executed[self.ip] == True: 
            # Finished successfully or instruction executed again
            return False
        else:
            self.executed[self.ip] = True

        nextInstruction = self.instructions[self.ip]
        opcode = nextInstruction[0]
        value = nextInstruction[1]

        if opcode == "acc":
            self.accumulator += value
        elif opcode == "jmp":
            self.ip += (value - 1)

        self.ip += 1
        return True

    def run(self):
        while self.nextInstruction():
            pass

    def hasFinishedSuccessfully(self):
        return self.ip > self.lastInstruction



def parseProgram(file):
    with open(file, "r") as infile:
        lines = [l.strip() for l in infile.readlines()]
    return [[ins.split()[0], int(ins.split()[1])] for ins in lines]


# Test
c = Computer(parseProgram("test.txt"))
c.run()
assert c.accumulator == 5


program = parseProgram("input.txt")
# Part 1
c = Computer(program)
c.run()
print("[*] Part 1: {}".format(c.accumulator))


# Part 2
c = None
for i in range(len(program)):
    opcode = program[i][0]
    if opcode == "nop":
        program[i][0] = "jmp"
        c = Computer(program)
        c.run()
        if c.hasFinishedSuccessfully():
            break
        else:
            program[i][0] = "nop"
    elif opcode == "jmp":
        program[i][0] = "nop"
        c = Computer(program)
        c.run()
        if c.hasFinishedSuccessfully():
            break
        else:
            program[i][0] = "jmp"

print("[*] Part 2: {}".format(c.accumulator))
