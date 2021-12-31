from typing import DefaultDict, Deque
from collections import defaultdict, deque

with open("input.txt") as file:
    file = file.read()


def parse(file):
    lines = [line.split(" ") for line in file.splitlines()]
    return lines


outs = []
lines = parse(file)

for line in lines:
    instruction, target1 = line[0], line[1]
    if len(line) == 3:
        target2 = line[2]

    if instruction == "inp":
        outs.append(f"{target1} = inp.popleft()")
    elif instruction == "add":
        outs.append(f"{target1} = {target1} + {target2}")
    elif instruction == "mul":
        outs.append(f"{target1} = {target1} * {target2}")
    elif instruction == "div":
        outs.append(f"{target1} = int({target1} / {target2})")
    elif instruction == "mod":
        outs.append(f"{target1} = {target1} % {target2}")
    elif instruction == "eql":
        outs.append(f"{target1} = 1 if {target1} == {target2} else 0")

for out in outs:
    print(out)