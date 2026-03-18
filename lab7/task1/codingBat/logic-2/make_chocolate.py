def make_chocolate(small, big, goal):
    max_big = goal // 5
    how_many_big = min(max_big, big)
    remainder = goal - (how_many_big * 5)
    if remainder <= small:
        return remainder
    else:
        return -1