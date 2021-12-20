with open("input.txt") as file:
    file = file.read()


def parse(s):
    out = []
    for line in s.split("\n")[1:]:
        a, b, c = line.split(",")
        out.append((int(a), int(b), int(c)))
    return out


data = list(map(parse, file.split("\n\n")))


def permute(coords):
    a, b, c = coords

    yield (+a, +b, +c)
    yield (+b, +c, +a)
    yield (+c, +a, +b)
    yield (+c, +b, -a)
    yield (+b, +a, -c)
    yield (+a, +c, -b)

    yield (+a, -b, -c)
    yield (+b, -c, -a)
    yield (+c, -a, -b)
    yield (+c, -b, +a)
    yield (+b, -a, +c)
    yield (+a, -c, +b)

    yield (-a, +b, -c)
    yield (-b, +c, -a)
    yield (-c, +a, -b)
    yield (-c, +b, +a)
    yield (-b, +a, +c)
    yield (-a, +c, +b)

    yield (-a, -b, +c)
    yield (-b, -c, +a)
    yield (-c, -a, +b)
    yield (-c, -b, -a)
    yield (-b, -a, -c)
    yield (-a, -c, -b)


def orients(beacons):
    yield from zip(*(permute(coords) for coords in beacons))


def match(coords_a, beacon_b):
    for coords_b in orients(beacon_b):
        dm = det_match(coords_a, coords_b)
        if dm is not None:
            return [add_vec(dm, c) for c in coords_b], dm


def det_match(coords_a, coords_b):
    for i in range(len(coords_a)):
        for j in range(i):
            diff = sub_vec(coords_a[i], coords_b[j])
            if commons(coords_a, coords_b, diff) >= 12:
                return diff

    return None


def add_vec(x, y):
    return (x[0] + y[0], x[1] + y[1], x[2] + y[2])


def sub_vec(x, y):
    return (x[0] - y[0], x[1] - y[1], x[2] - y[2])


def commons(coords_a, coords_b, diff):
    s = set()

    for i in coords_a:
        s.add(i)

    for j in coords_b:
        s.add(add_vec(j, diff))

    return len(coords_a) + len(coords_b) - len(s)


def full_match(things):
    things = [*things]
    detted = [things.pop(0)]
    diffs = []

    while len(things):
        print("steps left:", len(things))
        step_match(things, detted, diffs)

    return detted, diffs


def step_match(things, detted, diffs):
    for e, i in enumerate(things):
        for j in detted:
            vals = match(j, i)
            if vals is not None:
                mch, diff = vals
                detted.append(mch)
                things.pop(e)
                diffs.append(diff)
                return


mapped, scanners = full_match(data)
beacons = set()

for view in mapped:
    for point in view:
        beacons.add(point)

print("part 1 :", len(beacons))

pos_scanners = [(0, 0, 0), *scanners]


def get_dist(x, y):
    a, b, c = x
    d, e, f = y

    return abs(a - d) + abs(b - e) + abs(c - f)


out = 0

for i in pos_scanners:
    for j in pos_scanners:
        out = max(out, get_dist(i, j))

print("part 2 :", out)