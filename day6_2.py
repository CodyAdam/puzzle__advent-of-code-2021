import sys

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

states = [int(x) for x in lines[0].split(',')]
days = 256

sliding_window = [0] * 10
for x in states:
    sliding_window[x] += 1
print(sliding_window)

to_add = 0
for day in range(days):
    if sliding_window[0]:
        sliding_window[8 + 1] += sliding_window[0]
        sliding_window[6 + 1] += sliding_window[0]
    sliding_window = sliding_window[1:10]
    sliding_window.append(0)

print(sum(sliding_window))

#22 min