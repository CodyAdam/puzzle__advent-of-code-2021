lines = [line.strip() for line in open("input.txt", 'r').readlines()]


class octo():
    def __init__(self, val, x, y) -> None:
        self.val = val
        self.x = x
        self.y = y
        self.blinked = False

    def get_voisin(self):
        global octos
        x, y = self.x, self.y
        vois = []
        if x >= 1:
            vois.append(octos[y][x - 1])
        if x < len(octos[0]) - 1:
            vois.append(octos[y][x + 1])
        if y >= 1:
            vois.append(octos[y - 1][x])
            if x >= 1:
                vois.append(octos[y - 1][x - 1])
            if x < len(octos[0]) - 1:
                vois.append(octos[y - 1][x + 1])
        if y < len(octos) - 1:
            vois.append(octos[y + 1][x])
            if x >= 1:
                vois.append(octos[y + 1][x - 1])
            if x < len(octos[0]) - 1:
                vois.append(octos[y + 1][x + 1])
        return vois

    def inc(self):
        if not self.blinked:
            self.val += 1
            global blink_count
            if self.val > 9:
                blink_count += 1
                self.val = 0
                self.blinked = True
                for vois in self.get_voisin():
                    vois.inc()

    def reset(self):
        self.blinked = False


def show():
    for y, row in enumerate(octos):
        for x, o in enumerate(row):
            print("▮" if o.val == 0 else o.val, end=" ")
        print()


blink_count = 0
octos = [[None] * 10 for _ in range(10)]

for y, line in enumerate(lines):
    for x, c in enumerate(line):
        octos[y][x] = octo(int(c), x, y)

N = 1000
for step in range(N):

    print(step, blink_count)
    # show()
    pass

    for y, row in enumerate(octos):
        for x, o in enumerate(row):
            o.inc()

    for y, row in enumerate(octos):
        for x, o in enumerate(row):
            o.reset()

    sync = True
    for y, row in enumerate(octos):
        for x, o in enumerate(row):
            if o.val != octos[0][0].val:
                sync = False
    if sync:
        print(step + 1)
        show()
        exit()

print(N)
show()

print(blink_count)

# 41 min