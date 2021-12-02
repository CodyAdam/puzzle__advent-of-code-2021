import sys

sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

x = 0
y = 0
for line in lines:
    direction, value = line.split(" ")
    value = int(value)

    if direction == "forward":
        x += value
    elif direction == "up":
        y -= value
    elif direction == "down":
        y += value

print(x, y, x * y)

# 4 min
