with open("input.txt") as file:
    file = file.read()


def parse(file):
    lines = [line.split(" ") for line in file.splitlines()]
    for index, line in enumerate(lines):
        left, right = line
        lines[index] = (left, get_bound(right))
    return lines


def get_bound(string):
    x, z, y = string.split(",")
    x = [int(n) for n in x[2:].split('..')]
    y = [int(n) for n in y[2:].split('..')]
    z = [int(n) for n in z[2:].split('..')]
    return (x, y, z)


def turn(grid, mode, inter, bound):
    xi, yi, zi = inter
    xb, yb, zb = bound
    xi = [max(xi[0], xb[0]), min(xi[1], xb[1])]
    yi = [max(yi[0], yb[0]), min(yi[1], yb[1])]
    zi = [max(zi[0], zb[0]), min(zi[1], zb[1])]
    if xi[1] < xi[0] or yi[1] < yi[0] or zi[1] < zi[0]:
        return
    on = mode == "on"
    for x in range(xi[0], xi[1] + 1):
        for y in range(yi[0], yi[1] + 1):
            for z in range(zi[0], zi[1] + 1):
                coords = (x, y, z)
                if not coords in grid and on:
                    grid.add(coords)
                elif coords in grid and not on:
                    grid.remove(coords)


grid = set()
bound = get_bound("x=-50..50,y=-50..50,z=-50..50")
data = parse(file)
for index, line in enumerate(data):
    print(index)
    mode, inter = line
    turn(grid, mode, inter, bound)
print(len(grid))

# 45 min