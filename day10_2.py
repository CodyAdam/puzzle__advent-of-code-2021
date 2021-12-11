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


score_table = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
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
                return 0

    score = 0
    for i in range(len(stack) - 1, 0 - 1, -1):
        score = score * 5 + score_table[stack[i]]
    return score


scores = []
for line in lines:
    score = get_line_score(line)
    if score is not 0:
        scores.append(score)

scores.sort()
print(scores[int(len(scores) / 2)])

# 33 min