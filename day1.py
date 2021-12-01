import sys

sys.stdin = open("input.txt", 'r')
lines = [int(line.strip()) for line in sys.stdin.readlines()]

count = 0
for i in range(len(lines) - 1):
    if lines[i] < lines[i + 1]: count += 1
print(count)