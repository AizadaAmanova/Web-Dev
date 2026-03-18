def power(a,b):
    pr = 1
    for i in range(1,b+1):
        pr *= a
    return pr

data = input().split()
a = float(data[0])
b = int(data[1])

print(power(a,b))

