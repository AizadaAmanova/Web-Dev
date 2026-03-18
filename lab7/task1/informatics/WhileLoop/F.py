x = float(input())
y = float(input())

day = 1
current = x

while current < y:
    current += current * 0.1
    day += 1

print(day)