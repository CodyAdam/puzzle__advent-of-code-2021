with open("input.txt") as file:
    file = file.read()


def parse(s: str):
    lines = s.splitlines()
    algo = [c == "#" for c in lines[0]]

    image = set()
    for y, line in enumerate(lines[2:]):
        for x, c in enumerate(line):
            if c == "#":
                image.add((x, y))
    return algo, image


def get_binary(pix, image, fill_state):
    binary = "0b"
    for coord in get_neigh(pix):
        state = coord in image
        state = state if not fill_state else not state
        binary += "1" if (state or
                          (fill_state and is_fill(coord, image))) else "0"
    return binary


def get_state(binary, algo):
    return algo[int(binary, 2)]


def get_neigh(coord: tuple):
    x, y = coord
    neigh = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x, y),
             (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    return neigh


def print_img(image):
    min_x = min(image, key=lambda coord: coord[0])[0]
    min_y = min(image, key=lambda coord: coord[1])[1]
    max_x = max(image, key=lambda coord: coord[0])[0]
    max_y = max(image, key=lambda coord: coord[1])[1]
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            print("#" if (x, y) in image else " ", end="")
        print()
    print()


def is_fill(pix, image):
    for neigh in get_neigh(pix):
        if neigh in image: return False
    return True


algo, image = parse(file)
steps = 50
fill_state = False
for _ in range(steps):
    new_image = set()
    dones = set()
    if fill_state:
        next_fill_state = algo[-1]
    else:
        next_fill_state = algo[0]
    for pix in image:
        for neigh in get_neigh(pix):
            if neigh not in dones:
                binary = get_binary(neigh, image, fill_state)
                state = get_state(binary, algo)
                if not next_fill_state and state:
                    new_image.add(neigh)
                elif next_fill_state and not state:
                    new_image.add(neigh)
                dones.add(neigh)
    fill_state = next_fill_state

    image = new_image
    print_img(image)
print(len(image))

# 1 h 42