lines = [line.strip() for line in open("input.txt", 'r').readlines()]

table = {}
count = 0
for line in lines:
    inputs, outputs = line.split(" | ")
    inputs = inputs.split(" ")
    outputs = outputs.split(" ")

    for x in outputs:
        if len(x) in [2, 3, 4, 7]:
            count += 1
print(count)

#13 min