from collections import deque

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

graph = {}

# Build the graph
for line in lines:
    left, right = line.split("-")
    if left in graph:
        graph[left].add(right)
    else:
        graph[left] = set([right])

    if right in graph:
        graph[right].add(left)
    else:
        graph[right] = set([left])


# Depth first search algo
def dfs(prev, cur):
    is_big = cur.isupper()

    # pathing twice in a lowercase => stop
    if not is_big and cur in prev:
        return

    prev = prev.copy()
    prev.append(cur)

    if cur == "end":
        paths.append(prev)

    for neighbour in graph[cur]:
        dfs(prev, neighbour)


paths = []
dfs(deque(), "start")

# for path in paths:
#     for node in path:
#         print(node, end="-")
#     print()

print(len(paths))

# 16 min