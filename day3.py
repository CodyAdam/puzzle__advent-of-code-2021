import sys

sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

N = len(lines)
bits = len(lines[0])

checksum = bits * [0]
for line in lines:
    for bit_index in range(len(line)):
        if line[bit_index] == "1":
            checksum[bit_index] += 1

s = 0
for bit_index in range(bits):
    if checksum[-bit_index - 1] > N / 2:
        s += 2**bit_index
g = s ^ (2**bits - 1)

print(s * g)

# 7 min