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
    x, z, y = string.split(",")
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


def get_opposite_delta(i):
    p1 = (1, 1, 1)
    p2 = (1, 1, -1)
    p3 = (1, -1, 1)
    p4 = (1, -1, -1)
    p5 = (-1, 1, 1)
    p6 = (-1, 1, -1)
    p7 = (-1, -1, 1)
    p8 = (-1, -1, -1)
    return (p1, p2, p3, p4, p5, p6, p7, p8)[i]


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
        x = x[1] - x[0] + 1
        y = y[1] - y[0] + 1
        z = z[1] - z[0] + 1
        return x * y * z * (1 if self.positive else -1)

    def is_point_inside(self, point):
        x, y, z = self.bound
        xp, yp, zp = point
        in_x = xp >= x[0] and xp <= x[1]
        in_y = yp >= y[0] and yp <= y[1]
        in_z = zp >= z[0] and zp <= z[1]
        return in_z and in_x and in_y

    def is_intersecting(self, other):
        for point in self.points:
            if other.is_point_inside(point):
                return True
        for point in other.points:
            if self.is_point_inside(point):
                return True
        return False

    def get_intersection(self, other):
        for point in self.points:
            if other.is_point_inside(point):
                return other.get_intersection_from_point(point, self)
        for point in other.points:
            if self.is_point_inside(point):
                return self.get_intersection_from_point(point, other)
        return False

    def get_intersection_from_point(self, point, other):
        i = other.points.index(point)
        dx, dy, dz = get_opposite_delta(i)
        done = [False, False, False]
        x, y, z = point
        while not all(done):
            if not done[0]:
                new_coords = (x + dx, y, z)
                if self.is_point_inside(new_coords) and other.is_point_inside(
                        new_coords):
                    x += dx
                else:
                    done[0] = True

            if not done[1]:
                new_coords = (x, y + dy, z)
                if self.is_point_inside(new_coords) and other.is_point_inside(
                        new_coords):
                    y += dy
                else:
                    done[1] = True

            if not done[2]:
                new_coords = (x, y, z + dz)
                if self.is_point_inside(new_coords) and other.is_point_inside(
                        new_coords):
                    z += dz
                else:
                    done[2] = True
        point2 = (x, y, z)

        return cube_from_oppo(point, point2)

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
            neg = c.get_intersection(cube)
            neg.positive = mode == "off"
            to_add.append(neg)
    for c in to_add:
        cubes.add(c)
    if mode == "on":
        cubes.add(cube)
print(sum([c.area() for c in cubes]))

# out 43493252170964537
# exp  2758514936282235