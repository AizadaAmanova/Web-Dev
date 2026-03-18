def min_of_four(a, b, c, d):
    min1 = a if a < b else b
    min2 = c if c < d else d
    return min1 if min1 < min2 else min2
numbers = list(map(int, input().split()))
a, b, c, d = numbers[0], numbers[1], numbers[2], numbers[3]

result = min_of_four(a, b, c, d)
print(result)