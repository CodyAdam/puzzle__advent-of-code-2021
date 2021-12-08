lines = [line.strip() for line in open("input.txt", 'r').readlines()]

digits = [set() for _ in range(10)]
total = 0

for line in lines:
    left, right = line.split(' | ')
    left = left.split()
    right = right.split()

    for digit in left:
        if len(digit) == 2:
            digits[1] = set(digit)
        elif len(digit) == 3:
            digits[7] = set(digit)
        elif len(digit) == 4:
            digits[4] = set(digit)
        elif len(digit) == 7:
            digits[8] = set(digit)

    digits_of_len = {}
    for digit in left:
        digits_of_len[len(digit)] = digits_of_len.get(len(digit),
                                                      []) + [set(digit)]

    # 9
    for digit in digits_of_len[6]:
        if digit | digits[4] != digits[8]:
            digits[9] = digit | digits[4]

    digits_of_len[6].remove(digits[9])

    # 0 and 6
    for digit in digits_of_len[6]:
        if digit | digits[1] != digits[8]:
            digits[0] = digit
        else:
            digits[6] = digit

    # 5
    for digit in digits_of_len[5]:
        if digit | digits[1] == digits[9]:
            digits[5] = digit

    digits_of_len[5].remove(digits[5])

    # 2 and 3
    for digit in digits_of_len[5]:
        if digit | digits[1] == digit:
            digits[3] = digit
        else:
            digits[2] = digit

    num_result = ''
    for digit in right:
        num_result += str(digits.index(set(digit)))
    total += int(num_result)

print(total)