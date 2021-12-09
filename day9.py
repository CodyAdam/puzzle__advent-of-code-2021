lines = [line.strip() for line in open("input.txt", 'r').readlines()]

grid = [[int(c) for c in line] for line in lines]

r, c = len(grid), len(grid[0])

risk = 0
for y in range(r):
    for x in range(c):
        top, left, bot, right, cur = 10, 10, 10, 10, grid[y][x]
        if x > 0:
            left = grid[y][x - 1]
        if x < c - 1:
            right = grid[y][x + 1]
        if y > 0:
            top = grid[y - 1][x]
        if y < r - 1:
            bot = grid[y + 1][x]

        if cur < top and cur < left and cur < right and cur < bot:
            # print(cur)
            risk += cur + 1
print(risk)
# 13 min
