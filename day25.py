from typing import DefaultDict, Deque, List
from collections import defaultdict, deque

with open("input.txt") as file:
    file = file.read()


def parse(file):
    lines = [[c for c in line] for line in file.splitlines()]
    return lines


def show(board):
    for line in board:
        for c in line:
            print(c, end="")
        print()
    print()


def get_left(board, x, y):
    return board[y][(x - 1) % len(board[y])]


def get_up(board, x, y):
    return board[(y - 1) % len(board)][x]


def get_right(board, x, y):
    return board[y][(x + 1) % len(board[y])]


def get_down(board, x, y):
    return board[(y + 1) % len(board)][x]


def step_down(board):
    moves = 0
    new = [line.copy() for line in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            cur = board[y][x]
            if cur == ".":
                if get_up(board, x, y) == "v":
                    new[y][x] = "v"
                    new[(y - 1) % len(board)][x] = "."
                    moves += 1
    return new, moves


def step_right(board):
    moves = 0
    new = [line.copy() for line in board]
    for y in range(len(board)):
        for x in range(len(board[y])):
            cur = board[y][x]
            if cur == ".":
                if get_left(board, x, y) == ">":
                    new[y][x] = ">"
                    new[y][(x - 1) % len(board[y])] = "."
                    moves += 1

    return new, moves


board = parse(file)
show(board)
moves = 1
i = 0
while moves != 0:
    i += 1
    board, moves1 = step_right(board)
    board, moves2 = step_down(board)
    moves = moves1 + moves2
    print(i)
    # show(board)

# 24 min