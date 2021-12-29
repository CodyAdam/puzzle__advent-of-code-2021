from typing import Counter, Tuple
import itertools

with open("input.txt") as file:
    file = file.read()

dices = [sum(x) for x in itertools.product([1, 2, 3], repeat=3)]


def parse(s: str):
    lines = [line.split(" ")[-1] for line in s.splitlines()]
    p1, p2 = lines[0], lines[1]
    return int(p1), int(p2)


def new_index(start, roll) -> Tuple[int, int]:
    return ((start + roll - 1) % 10) + 1


def winner_counter(turn1, p1, p2, score_p1, score_p2):
    global memoization
    if (turn1, p1, p2, score_p1, score_p2) in memoization:
        return memoization[(turn1, p1, p2, score_p1, score_p2)]
    winners = Counter()
    if score_p1 >= 21 or score_p2 >= 21:
        if score_p1 > score_p2:
            winners["p1"] += 1
        else:
            winners["p2"] += 1
        return winners

    if turn1:
        sub_games = [
            winner_counter(not turn1, new_index(p1, roll), p2,
                           score_p1 + new_index(p1, roll), score_p2)
            for roll in dices
        ]
    else:
        sub_games = [
            winner_counter(not turn1, p1, new_index(p2, roll), score_p1,
                           score_p2 + new_index(p2, roll)) for roll in dices
        ]
    for sub_game in sub_games:
        winners += sub_game
    memoization[(turn1, p1, p2, score_p1, score_p2)] = winners
    return winners


memoization = {}
p1, p2 = parse(file)
count = winner_counter(True, p1, p2, 0, 0)
print("part 2:", count.most_common(1))

# 1h33 min