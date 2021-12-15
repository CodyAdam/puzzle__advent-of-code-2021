from collections import defaultdict, deque

lines = [line.strip() for line in open("input.txt", 'r').readlines()]
grid = [[int(c) for c in line] for line in lines]
new_grid = []

for i in range(5):
    for row in grid:
        new_grid.append([c + i for c in row] + [c + i + 1 for c in row] +
                        [c + i + 2 for c in row] + [c + i + 3 for c in row] +
                        [c + i + 4 for c in row])

grid = new_grid
W, H = len(grid[0]), len(grid)
for y in range(H):
    for x in range(W):
        if grid[y][x] > 9:
            grid[y][x] -= 9

graph = defaultdict(lambda: set())

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
    mins[pos] = min([mins[p] for p in neigh]) + grid[y][x]

    for ne_pos in neigh:
        if mins[ne_pos] > mins[pos] + grid[ne_pos[1]][ne_pos[0]]:
            mins[ne_pos] = mins[pos] + grid[ne_pos[1]][ne_pos[0]]


START = (0, 0)
END = (H - 1, W - 1)
mins = defaultdict(lambda: 9999)
mins[START] = 0
cur_ver = (1, 0)
cur_hor = (0, 1)

while cur_ver[0] != W and cur_hor[1] != H:
    if cur_ver == cur_hor:
        make_min(cur_hor[0], cur_hor[1])
        cur_ver = (cur_ver[0] + 1, 0)
        cur_hor = (0, cur_hor[1] + 1)
    else:
        make_min(cur_hor[0], cur_hor[1])
        make_min(cur_ver[0], cur_ver[1])
        cur_ver = (cur_ver[0], cur_ver[1] + 1)
        cur_hor = (cur_hor[0] + 1, cur_hor[1])

print(mins[END])

# 1 h 33