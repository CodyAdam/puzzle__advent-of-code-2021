lines = [line.strip() for line in open("input.txt", 'r').readlines()]

states = [int(x) for x in lines[0].split(',')]
N = len(states)
states.sort()

targets = {}
for pivot in range(states[0], states[-1] + 1):
    for x in states:
        if not pivot in targets:
            targets[pivot] = []
        dist = abs(x - pivot)
        targets[pivot].append((dist * (dist + 1)) / 2)
        # (n * (n+1)) / 2  is the formula to get the fuel for a distance of n

min_sum = 9999999999999
for targ in targets:
    current_sum = sum(targets[targ])
    if min_sum > current_sum:
        min_sum = current_sum

print(min_sum)

# 28 min