x = int(input())
d = int(input())

count = 0
for digit in str(x):
    if int(digit) == d:
        count += 1

print(count)