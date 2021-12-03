import sys

sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

oxy = set(lines.copy())
co2 = set(lines.copy())

i = 0
while len(oxy) > 1 and i < len(lines[0]):
    ones = set()
    zeros = set()
    for val in oxy:
        if val[i] == "0":
            zeros.add(val)
        else:
            ones.add(val)
    i += 1
    if len(ones) + len(zeros) == 1:
        oxy = ones | zeros
    else:
        oxy = ones if len(ones) >= len(oxy) / 2 else zeros

i = 0
while len(co2) > 1 and i < len(lines[0]):
    ones = set()
    zeros = set()
    for val in co2:
        if val[i] == "0":
            zeros.add(val)
        else:
            ones.add(val)
    i += 1
    if len(ones) + len(zeros) == 1:
        co2 = ones | zeros
    else:
        co2 = ones if len(ones) < len(co2) / 2 else zeros

print(oxy, co2)
oxy = list(oxy)[0]
co2 = list(co2)[0]
print(int(oxy, 2), int(co2, 2), int(oxy, 2) * int(co2, 2))

# 18 min