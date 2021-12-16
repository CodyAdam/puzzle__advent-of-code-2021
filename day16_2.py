from collections import defaultdict, deque
from typing import Deque

lines = [line.strip() for line in open("input.txt", 'r').readlines()]

to_bin = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}
to_hex = {v: k for k, v in to_bin.items()}


def get_bits(buffer, number):
    return "".join([buffer.popleft() for _ in range(number)])


def read_packet(buffer: Deque):
    if buffer.count("0") == len(buffer):
        length = len(buffer)
        get_bits(buffer, length)
        return (-1, length)
    bit_count = 0

    ver = int(get_bits(buffer, 3), 2)
    global ver_tot
    ver_tot += ver
    type_id = int(get_bits(buffer, 3), 2)
    bit_count += 6

    value = 0
    if type_id == 4:
        str_value = ""
        while buffer.popleft() == "1":
            str_value += get_bits(buffer, 4)
            bit_count += 5
        str_value += get_bits(buffer, 4)
        bit_count += 5
        value = int(str_value, 2)
    else:
        if buffer.popleft() == "0":
            sub_length = int(get_bits(buffer, 15), 2)
            bit_count += 16
            sub_bit_count = 0
            values = []
            while sub_bit_count < sub_length and len(buffer):
                val, sb = read_packet(buffer)
                values.append(val)
                bit_count += sb
                sub_bit_count += sb
        else:
            subpacket_count = int(get_bits(buffer, 11), 2)
            bit_count += 12
            values = []
            for _ in range(subpacket_count):
                val, sb = read_packet(buffer)
                bit_count += sb
                values.append(val)
        if type_id == 0:
            value = sum(values)
        elif type_id == 1:
            value = 1
            for x in values:
                value = value * x
        elif type_id == 2:
            value = min(values)
        elif type_id == 3:
            value = max(values)
        elif type_id == 5:
            value = 1 if values[0] > values[1] else 0
        elif type_id == 6:
            value = 1 if values[0] < values[1] else 0
        elif type_id == 7:
            value = 1 if values[0] == values[1] else 0
        else:
            print("id not found")
            exit()
    return value, bit_count


ver_tot = 0
bin_line = ""
for c in lines[0]:
    bin_line += to_bin[c]
buffer = deque()
for c in bin_line:
    buffer.append(c)

while len(buffer):
    value, bit_count = read_packet(buffer)
    print(value)

# 1h 50