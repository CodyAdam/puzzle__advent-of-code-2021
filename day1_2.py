import sys

sys.stdin = open("input.txt", 'r')
lines = [int(line.strip()) for line in sys.stdin.readlines()]

count = 0
for i in range(len(lines) - 3):
    window = lines[i] + lines[i + 1] + lines[i + 2]
    if window < window - lines[i] + lines[i + 3]: count += 1
print(count)
