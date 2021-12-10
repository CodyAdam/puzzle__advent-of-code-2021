lines = [line.strip() for line in open("input.txt", 'r').readlines()]


def get_oposite(char):
    if char == ")":
        return "("
    if char == "}":
        return "{"
    if char == "]":
        return "["
    if char == ">":
        return "<"
    print("cant find char", char)
    exit()


point_table = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def get_line_score(line):
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]:
            stack.append(c)
        else:
            if get_oposite(c) is stack[-1]:
                stack = stack[:-1]
            else:
                print(line, "corrupt found :", c)
                return point_table[c]
    return 0


score = 0
for line in lines:
    score += get_line_score(line)

print(score)

# 25 min