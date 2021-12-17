for y in range(abs(min(y_target)), min(y_target) + 1, -1):
    for x in range(0, max(x_target) + 1):
        valid = is_valid(0, 0, x, y, 0)
        if valid != None:
            grid[(x, y)] = valid