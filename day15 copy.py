from collections import defaultdict, deque

lines = [line.strip() for line in open("input.txt", 'r').readlines()]
grid = [[int(c) for c in line] for line in lines]
graph = defaultdict(lambda: set())
W, H = len(grid[0]), len(grid)

for y in range(H):
    for x in range(W):
        if x < W - 1:  # go Right
            graph[(x, y)].add((x + 1, y))
        if x > 0:  # go Left
            graph[(x, y)].add((x - 1, y))
        if y < H - 1:  # go Down
            graph[(x, y)].add((x, y + 1))
        if y > 0:  # go Up
            graph[(x, y)].add((x, y - 1))


def show_mins():
    for y in range(H):
        for x in range(W):
            if mins[(x, y)] < 10:
                print(" ", end="")
            print(mins[(x, y)], end=" ")
        print()


def make_min(x, y):
    pos = (x, y)
    neigh = graph[pos]
    last_mins = mins[pos]
    mins[pos] = min(min([mins[p] for p in neigh]) + grid[y][x], last_mins)
    return last_mins != mins[pos]


START = (0, 0)
END = (H - 1, W - 1)

mins = defaultdict(lambda: 999999)
mins[START] = 0

has_changed = True
while has_changed:
    has_changed = False
    for y in range(H):
        for x in range(W):
            has_changed = has_changed or make_min(x, y)

print(mins[END])

# 1 h 20