from typing import DefaultDict, Deque
from collections import defaultdict, deque

with open("input.txt") as file:
    file = file.read()


def parse(file):
    lines = [line.split(" ") for line in file.splitlines()]
    return lines


def step(action, inp: Deque, cache: DefaultDict):
    instruction, target1 = action[0], action[1]
    a = cache[target1]
    if len(action) == 3:
        target2 = action[2]
        if target2 in ["w", "x", "y", "z"]:
            b = cache[target2]
        else:
            b = int(target2)

    if instruction == "inp":
        cache[target1] = int(inp.popleft())
    elif instruction == "add":
        cache[target1] = a + b
    elif instruction == "mul":
        cache[target1] = a * b
    elif instruction == "div":
        cache[target1] = int(a / b)
    elif instruction == "mod":
        cache[target1] = a % b
    elif instruction == "eql":
        cache[target1] = 1 if a == b else 0


def get_next_down(inp):
    i = -1
    inp[i] -= 1
    while inp[i] == 0:
        inp[i] = 9
        i -= 1
        if i == -15:
            return None
        inp[i] -= 1
    return inp


def get_next_up(inp):
    i = -1
    inp[i] += 1
    while inp[i] == 10:
        inp[i] = 1
        i -= 1
        if i == -15:
            return None
        inp[i] += 1
    return inp


def inputs():
    inp = [1 for _ in range(14)]
    while inp:
        yield deque(inp)
        inp = get_next_up(inp)


outs = []
lines = parse(file)
inp = [1 for _ in range(14)]
for _ in range(3):
    i = 0
    while i < 14:
        min_j = []
        for j in range(1, 10):
            np = deque(inp)
            np[i] = j
            cache = defaultdict(lambda: 0)
            for line in lines:
                step(line, np, cache)
            min_j.append(cache["z"])
            if cache["z"] == 0:
                out = inp
                out[i] = j
                outs.append(int("".join([str(c) for c in out])))
        inp[i] = min_j.index(min(min_j)) + 1
        i += 1
print(max(outs))

while True:
    np = deque([int(c) for c in input().strip()])
    cache = defaultdict(lambda: 0)
    for line in lines:
        step(line, np, cache)
    print(cache["z"])