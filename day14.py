from collections import defaultdict

############## INIT ##########################################################

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

# Create the poly string as an Array of char
poly = [c for c in lines[0]]

# Create the rules (key = 2 letters, value = the new letter that spawn)
rules = {}
for line in lines[2:]:
    left, right = line.split(" -> ")
    rules[left] = right

# Create the letter count (key = the letter, value = the number it occur)
count = defaultdict(lambda: 0)
for c in poly:
    count[c] += 1

############## LOOP ##########################################################

for _ in range(10):
    newPoly = []
    for i in range(len(poly) - 1):
        l1, l2 = poly[i], poly[i + 1]

        newPoly.append(l1)
        if l1 + l2 in rules:
            newPoly.append(rules[l1 + l2])

    newPoly.append(poly[-1])
    poly = newPoly

############## ANSWER ##########################################################

maxi = max(count.values())
mini = min(count.values())
print(maxi - mini)

# 13 min