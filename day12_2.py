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
def dfs(prev_and_joker, cur):
    prev, joker = prev_and_joker
    is_big = cur.isupper()

    # Dont path twice in start
    if cur == "start" and "start" in prev:
        return

    # this condition is the only thing that changed between part 1 and 2
    if not is_big:
        if joker == cur and prev.count(cur) >= 2:  # pathing trice
            return
        elif cur in prev:  # pathing twice
            if not joker:  # allow it with the joker
                joker = cur
            else:  # stop if joker already used
                return

    prev = prev.copy()
    prev.append(cur)

    if cur == "end":
        paths.append(prev)
        return

    for neighbour in graph[cur]:
        dfs((prev, joker), neighbour)


paths = []
dfs((deque(), None), "start")

print(len(paths))
# for path in paths:
#     for node in path:
#         print(node, end="-")
#     print()

# 34 min