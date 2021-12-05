lines = [line.strip() for line in open("input.txt", 'r').readlines()]

grid = {}


def mark(x, y):
    global grid
    if (x, y) in grid:
        grid[(x, y)] += 1
    else:
        grid[(x, y)] = 1


for line in lines:
    (p1, p2) = line.split(" -> ")
    (x1, y1) = [int(x) for x in p1.split(',')]
    (x2, y2) = [int(x) for x in p2.split(',')]
    x = x1
    y = y1
    mark(x1, y1)
    while x != x2 or y != y2:
        if x2 != x:
            x += 1 if x2 - x > 0 else -1
        if y != y2:
            y += 1 if y2 - y > 0 else -1
        mark(x, y)

sum_overlap = 0
for p in grid:
    x = grid[p]
    if x >= 2: sum_overlap += 1

print(sum_overlap)

#0min