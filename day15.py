from collections import defaultdict, deque
from line_profiler import LineProfiler

lines = [[int(c) for c in line.strip()]
         for line in open("input.txt", 'r').readlines()]

graph = defaultdict(lambda: set())
W, H = len(lines[0]), len(lines)

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


def main():
    dist = defaultdict(lambda: 9999)
    dist[(0, 0)] = 0
    q = set()
    for node in graph:
        q.add(node)

    while len(q):
        pos = min(q, key=lambda pos: dist[pos])
        q.remove(pos)

        for n in graph[pos]:
            if n in q:
                temp = dist[pos] + lines[n[1]][n[0]]
                if dist[n] > temp:
                    dist[n] = temp

    print(dist[(H - 1, W - 1)])


profile = LineProfiler()
profile.add_function(main)
profile.runcall(main)
profile.print_stats()
# 1 h 20