lines = open("input.txt", 'r').read().splitlines()

tab = []
for line in lines:
    direction, value = line.split(" ")
    tab.append((direction, int(value)))

print(tab)