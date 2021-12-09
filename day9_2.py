lines = [line.strip() for line in open("input.txt", 'r').readlines()]


def get_sides(x, y):
    top, left, bot, right, cur = [10,
                                  True], [10,
                                          True], [10,
                                                  True], [10,
                                                          True], grid[(x, y)]
    if x > 0:
        left = grid[(x - 1, y)]
    if x < c - 1:
        right = grid[(x + 1, y)]
    if y > 0:
        top = grid[(x, y - 1)]
    if y < r - 1:
        bot = grid[(x, y + 1)]
    return top, left, bot, right, cur


r, c = len(lines), len(lines[0])
grid = {}
for y in range(r):
    for x in range(c):
        grid[(x, y)] = [int(lines[y][x]), False]


def bfs(x, y):
    grid[(x, y)][1] = True
    tot = 0
    top, left, bot, right, cur = get_sides(x, y)
    if top[0] > cur[0] and not top[1] and top[0] < 9:
        tot += bfs(x, y - 1)
    if bot[0] > cur[0] and not bot[1] and bot[0] < 9:
        tot += bfs(x, y + 1)
    if left[0] > cur[0] and not left[1] and left[0] < 9:
        tot += bfs(x - 1, y)
    if right[0] > cur[0] and not right[1] and right[0] < 9:
        tot += bfs(x + 1, y)
    return tot + 1


sizes = []
for y in range(r):
    for x in range(c):
        top, left, bot, right, cur = get_sides(x, y)

        if cur[0] < top[0] and cur[0] < left[0] and cur[0] < right[0] and cur[
                0] < bot[0]:
            sizes.append(bfs(x, y))
sizes.sort()

print(sizes[-1] * sizes[-2] * sizes[-3])
# 28 min
