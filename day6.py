import sys

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

states = [int(x) for x in lines[0].split(',')]
days = 80

to_add = 0
for day in range(days):
    for i in range(len(states)):
        state = states[i]
        if states[i] == 0:
            states[i] = 6
            to_add += 1
        else:
            states[i] -= 1

    for _ in range(to_add):
        states.append(8)
    to_add = 0

print(len(states))

# 5 min