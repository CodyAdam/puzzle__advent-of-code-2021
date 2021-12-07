import sys

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

states = [int(x) for x in lines[0].split(',')]
N = len(states)
states.sort()

target = states[int(N / 2)]
sum_fuel = 0
for x in states:
    sum_fuel += abs(x - target)

print(sum_fuel)

# 4 min