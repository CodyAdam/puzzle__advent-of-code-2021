from collections import defaultdict

############## INIT ##########################################################

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

# count the number of couple there is (key = 2 letter, value = number of occur)
couples = defaultdict(lambda: 0)
# count the number of letter there is (key = 1 letter, value = number of occur)
count = defaultdict(lambda: 0)

for i in range(len(lines[0]) - 1):
    l1, l2 = lines[0][i] + lines[0][i + 1]
    couples[l1 + l2] += 1
    count[l1] += 1
count[lines[0][-1]] += 1

# Create the rules (key = 2 letters, value = the new letter that spawn)
rules = {}
for line in lines[2:]:
    left, right = line.split(" -> ")
    rules[left] = right

############## LOOP ##########################################################

for _ in range(40):
    new_couples = couples.copy()
    for couple in couples:
        l1, l2 = couple[0], couple[1]

        if l1 + l2 in rules:

            #  Exemple :
            #
            #  rule is AB -> C
            #  poly is ABB
            #
            #  couples = { AB:1, BB:1}
            #
            #  insert C in AB -> poly is ACBB
            #  AB -= 1
            #  AC += 1
            #  CB += 1
            #  new_couples = { AB:0, BB:1, AC:1, CB:1}

            new_couples[l1 + rules[l1 + l2]] += couples[couple]
            new_couples[rules[l1 + l2] + l2] += couples[couple]
            count[rules[l1 + l2]] += couples[couple]
            new_couples[couple] -= couples[couple]
    couples = new_couples

############## ANSWER ##########################################################

maxi = max(count.values())
mini = min(count.values())
print(maxi - mini)

# 40 min