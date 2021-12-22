from math import ceil, floor
from collections import deque

lines = [line.strip() for line in open("input.txt", 'r').readlines()]


def str2array(string):
    if "," in string:
        count = 0
        left = ""
        right = ""
        for i, c in enumerate(string[1:-1]):
            if c == "[":
                count += 1
            elif c == "]":
                count -= 1
            elif c == ',' and count == 0:
                left = string[1:i + 1]
                right = string[i + 2:-1]
                break
        return [str2array(left), str2array(right)]
    else:
        return int(string)


def add(arr1, arr2):
    if not arr1:
        return arr2
    return [arr1, arr2]


def check_explode(arr, index=[]):
    if type(arr) is int:
        return []
    else:
        if len(index) >= 4:
            return [("explode", tuple(index))]
        else:
            [left, right] = arr
            return [
                x for x in [
                    *check_explode(left, index +
                                   [0]), *check_explode(right, index + [1])
                ] if x
            ]


def check_split(arr, index=[]):
    if type(arr) is int:
        value = arr
        if value >= 10:
            return ("split", tuple(index))
        else:
            return None
    else:
        [left, right] = arr
        l = check_split(left, index + [0])
        r = check_split(right, index + [1])
        return l if l else r


def get_1_left(index: list):
    index = list(index)
    if sum(index) == 0:
        return index + [0]
    for i in range(1, len(index) + 1):
        if index[-i] == 1:
            index[-i] = 0
            break
        else:
            index[-i] = 1
    return tuple(index + [1, 1, 1, 1])


def get_1_right(index):
    index = list(index)
    if sum(index) == len(index):
        return index + [1]
    for i in range(1, len(index) + 1):
        if index[-i] == 0:
            index[-i] = 1
            break
        else:
            index[-i] = 0
    return tuple(index + [0, 0, 0, 0])


def add_at_index(arr, index, value):
    current = arr
    while len(index) > 1 and type(current[index[0]]) is not int:
        current = current[index[0]]
        index = index[1:]
    current[index[0]] += value


def get_at_index(arr, index):
    current = arr
    real_index = ()
    while len(index) > 1 and type(current[index[0]]) is not int:
        real_index = real_index + (index[0], )
        current = current[index[0]]
        index = index[1:]
    return current[index[0]], real_index + (index[0], )


def set_at_index(arr, index, value):
    current = arr
    while len(index) > 1 and type(current[index[0]]) is not int:
        current = current[index[0]]
        index = index[1:]
    current[index[0]] = value


def explode(arr, index):
    left, right = get_at_index(arr, index)[0]
    left_index, right_index = get_1_left(index), get_1_right(index)
    add_at_index(arr, left_index, left)
    add_at_index(arr, right_index, right)
    set_at_index(arr, index, 0)
    global q
    if get_at_index(arr, right_index)[0] >= 10:
        to_add = ("split", right_index)
        q.append(to_add)
    if get_at_index(arr, left_index)[0] >= 10:
        to_add = ("split", left_index)
        q.append(to_add)


def split(arr, index):
    value, real_index = get_at_index(arr, index)
    left, right = floor(value / 2.0), ceil(value / 2.0)
    set_at_index(arr, index, [left, right])
    if len(real_index) >= 4:
        global q
        q.append(("explode", real_index))


def get_magnitude(arr):
    if type(arr) is int:
        return arr
    else:
        [left, right] = arr
        return get_magnitude(left) * 3 + 2 * get_magnitude(right)


to_explode = deque()
to_split = deque()
q = deque()
arr = None
for line in lines:
    arr = add(arr, str2array(line))
    print("addition  :", arr)
    for items in check_explode(arr):
        q.appendleft(items)
    changed = True
    while changed:
        changed = False
        ope = None
        index = None
        for item in reversed(q):
            ope, index = item
            if item[0] == "explode":
                q.remove(item)
                changed = True
                break
        else:
            item = check_split(arr)
            if type(item) is tuple:
                changed = True
                ope, index = item
            else:
                continue
        if ope == "explode":
            explode(arr, index)
            print("exploding :", arr)
        else:
            split(arr, index)
            print("spliting  :", arr)
print(get_magnitude(arr))
# 3h
