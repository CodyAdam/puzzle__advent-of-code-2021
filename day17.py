from collections import defaultdict

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

x_target, y_target = lines[0][13:].split(", ")

x_target, y_target = x_target[2:].split(".."), y_target[2:].split("..")

x_target = range(int(x_target[0]), int(x_target[1]) + 1)
y_target = range(int(y_target[0]), int(y_target[1]) + 1)


def is_valid(x_origin, y_origin, dx, dy, max_y):
    if x_origin in x_target and y_origin in y_target:
        return max(y_origin, max_y)
    elif x_origin > max(x_target) or y_origin < min(y_target):
        return None
    else:
        return is_valid(x_origin + dx, y_origin + dy, max(0, dx - 1), dy - 1,
                        max(y_origin, max_y))


grid = defaultdict(lambda: None)

for y in range(abs(min(y_target)), min(y_target) - 1, -1):
    for x in range(0, max(x_target) + 1):
        valid = is_valid(0, 0, x, y, 0)
        if valid != None:
            grid[(x, y)] = valid

######## VISUALIZE THE LAUNCHING CURVE

y_range = (min([k[1] for k in grid]), max([k[1] for k in grid]))
x_range = (min([k[0] for k in grid]), max([k[0] for k in grid]))


def show_launch():
    for y in range(y_range[1], y_range[0], -1):
        for x in range(0, x_range[1]):
            valid = grid[(x, y)]
            if (0, 0) == (x, y):
                print("S", end=" ")
            elif valid != None:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


# show_launch()

print("x :", x_range)
print("y :", y_range)
print("ans :", max([grid[pos] for pos in grid if grid[pos]]))

# 35 min