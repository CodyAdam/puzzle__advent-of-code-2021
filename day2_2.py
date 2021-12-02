import sys

sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

x = 0
y = 0
aim = 0
for line in lines:
    direction, value = line.split(" ")
    value = int(value)

    if direction == "forward":
        y += value * aim
        x += value
    elif direction == "up":
        aim -= value
    elif direction == "down":
        aim += value

print(x, y, x * y)

# 7 min