a = int(input())
b = int(input())
for i in range(a, b+1):
    root = int(i ** (0.5))
    if (root**2  == i):
        print(i)

        