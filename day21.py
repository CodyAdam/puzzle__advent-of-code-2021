from typing import Tuple

with open("input.txt") as file:
    file = file.read()


def parse(s: str):
    lines = [line.split(" ")[-1] for line in s.splitlines()]
    p1, p2 = lines[0], lines[1]
    return int(p1), int(p2)


def dice_roll():
    global dice_last
    global dice_count
    dice_count += 1
    dice_last = ((dice_last) % 100) + 1
    return dice_last


def step(start) -> Tuple[int, int]:
    index = start
    rolls = [dice_roll() for _ in range(3)]
    index += sum(rolls)
    return ((index - 1) % 10) + 1


dice_count = 0
dice_last = 0
p1, p2 = parse(file)
score_p1 = 0
score_p2 = 0
while score_p1 < 1000 and score_p2 < 1000:
    p1 = step(p1)
    score_p1 += p1
    if score_p1 >= 1000: break
    p2 = step(p2)
    score_p2 += p2
    print(score_p1, score_p2, dice_count)

print(score_p1, score_p2, dice_count)
print("part 1:", min(score_p1, score_p2) * dice_count)

# 30 min