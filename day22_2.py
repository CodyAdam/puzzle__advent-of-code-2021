from typing import List

with open("input.txt") as file:
    file = file.read()


def parse(file):
    lines = [line.split(" ") for line in file.splitlines()]
    for index, line in enumerate(lines):
        left, right = line
        lines[index] = (left, get_bound(right))
    return lines


def get_bound(string):
    x, y, z = string.split(",")
    x = [int(n) for n in x[2:].split('..')]
    y = [int(n) for n in y[2:].split('..')]
    z = [int(n) for n in z[2:].split('..')]
    return (x, y, z)


def get_points_from_bound(bound):
    x, y, z = bound
    p1 = (x[0], y[0], z[0])
    p2 = (x[0], y[0], z[1])
    p3 = (x[0], y[1], z[0])
    p4 = (x[0], y[1], z[1])
    p5 = (x[1], y[0], z[0])
    p6 = (x[1], y[0], z[1])
    p7 = (x[1], y[1], z[0])
    p8 = (x[1], y[1], z[1])
    return (p1, p2, p3, p4, p5, p6, p7, p8)


def cube_from_oppo(p1, p2):
    x, y, z = p1
    x2, y2, z2 = p2
    bound = ([min(x, x2), max(x, x2)], [min(y, y2),
                                        max(y, y2)], [min(z, z2),
                                                      max(z, z2)])
    return Cube(bound)


class Cube:
    def __init__(self, bound, positive=True) -> None:
        self.bound = bound
        self.points = get_points_from_bound(bound)
        self.positive = positive

    def area(self):
        x, y, z = self.bound
        x = abs(x[1] - x[0] + 1)
        y = abs(y[1] - y[0] + 1)
        z = abs(z[1] - z[0] + 1)
        return x * y * z * (1 if self.positive else -1)

    def is_intersecting(self, other):
        x1, y1, z1 = self.bound
        x2, y2, z2 = other.bound

        return x1[0] < x2[1] and x1[1] > x2[0] and y1[0] < y2[1] and y1[
            1] > y2[0] and z1[0] < z2[1] and z1[1] > z2[0]

    def get_intersection(self, other):
        x1, y1, z1 = self.bound
        x2, y2, z2 = other.bound

        min_x = max(x1[0], x2[0])
        min_y = max(y1[0], y2[0])
        min_z = max(z1[0], z2[0])

        max_x = min(x1[1], x2[1])
        max_y = min(y1[1], y2[1])
        max_z = min(z1[1], z2[1])

        p1 = (min_x, min_y, min_z)
        p2 = (max_x, max_y, max_z)
        return cube_from_oppo(p1, p2)

    def __str__(self) -> str:
        return f"{self.bound} -> {self.area()}"

    def __repr__(self) -> str:
        return str(self)


cubes = set()
data = parse(file)
for index, line in enumerate(data):
    print(index)
    mode, bound = line
    cube = Cube(bound, mode == "on")
    to_add = []
    for c in cubes:
        c: Cube
        if c.is_intersecting(cube):
            inter = c.get_intersection(cube)
            inter.positive = not c.positive
            to_add.append(inter)
    for c in to_add:
        cubes.add(c)
    if cube.positive:
        cubes.add(cube)
print(sum([c.area() for c in cubes]))
