import sys
from time import sleep


def mark(x, board):
    for line in board:
        for i in range(len(line)):
            if line[i][0] == x:
                line[i] = (line[i][0], True)


def check_win(board):
    horizontal = True
    for y in range(len(board)):
        horizontal = True
        for x in range(len(board)):
            if not board[y][x][1]:
                horizontal = False
        if horizontal:
            return board
    vertical = True
    for x in range(len(board)):
        vertical = True
        for y in range(len(board)):
            if not board[y][x][1]:
                vertical = False
        if vertical:
            return board
    return None


def get_sum_unmarked(board):
    sum_value = 0
    for line in board:
        for val in line:
            if val[1] == False:
                sum_value += val[0]
    return sum_value


#### SERIALIZATION ################
sys.stdin = open("input.txt", 'r')
lines = [line.strip() for line in sys.stdin.readlines()]

balls = [int(x) for x in lines[0].split(",")]
boards = []

board = []
for line in lines[2:]:
    if line:
        board.append([(int(x), False) for x in line.split()])
    else:
        boards.append(board)
        board = []
boards.append(board)
###################################

for num in balls:
    for board in boards:
        mark(num, board)
        winner = check_win(board)
        if winner:
            print(get_sum_unmarked(winner) * num)
            exit()