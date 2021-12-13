from collections import deque

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

grid = set()
instructions = 0
for line in lines:
    if line.startswith("fold along"):
        _, _, axis = line.split(" ")
        axis, value = axis.split("=")
        value = int(value)
        instructions += 1

        to_remove = set()
        to_add = set()
        if axis == "x":
            for x, y in grid:
                if x > value:
                    to_add.add((value - (x - value), y))
                    to_remove.add((x, y))
        else:
            for x, y in grid:
                if y > value:
                    to_add.add((x, value - (y - value)))
                    to_remove.add((x, y))
        grid = grid | to_add
        grid = grid ^ to_remove
        # if instructions == 1: # you only have to remove this line for P2
        #     break

    elif line:
        x, y = line.split(",")
        grid.add((int(x), int(y)))

for y in range(8):
    for x in range(40):
        print('#' if (x, y) in grid else ".", end="")
    print()

print(len(grid))

# 24 min