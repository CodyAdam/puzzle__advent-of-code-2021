from typing import DefaultDict, Deque
from collections import defaultdict, deque
import time

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


def steps(inp):
    w = 0
    z = 0
    y = 0
    x = 0
    w = inp.popleft()
    x = z % 26
    x = x + 12
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 4
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    x = x + 15
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 11
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    x = x + 11
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 7
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -14
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 2
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    x = x + 12
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 11
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -10
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 13
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    x = x + 11
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 9
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    x = x + 13
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 12
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -7
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 6
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    x = x + 10
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 2
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -2
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 11
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -1
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 12
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -4
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 3
    y = y * x
    z = z + y
    w = inp.popleft()
    x = z % 26
    z = int(z / 26)
    x = x + -12
    x = 0 if x == w else 1
    y = (25 * x) + 1
    z = z * y
    y = w + 13
    y = y * x
    z = z + y
    return z


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


def inputs(start):
    inp = start
    while inp:
        yield inp
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
            z = steps(np)
            min_j.append(z)
            if z == 0:
                out = inp
                out[i] = j
                outs.append(int("".join([str(c) for c in out])))
        inp[i] = min_j.index(min(min_j)) + 1
        i += 1
maxi = max(outs)
print(maxi)


def brute_force(start):
    for inp in inputs(start):
        z = steps(deque(inp))
        if z == 0:
            print(inp)


brute_force([int(c) for c in str(maxi)])

# while True:
#     np = deque([int(c) for c in input().strip()])
#     z = steps(np)
#     print(z)