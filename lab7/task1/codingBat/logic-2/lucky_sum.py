def lucky_sum(a, b, c):
    total = 0
    
    if a == 13:
        return 0
    total += a
    
    if b == 13:
        return total
    total += b
    
    if c == 13:
        return total
    total += c
    
    return total