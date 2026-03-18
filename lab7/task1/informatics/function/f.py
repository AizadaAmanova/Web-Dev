import math
def n_pow(a, n):
    b = math.pow(a, n)
    return b


data = input().split()
a = float(data[0])
n = int(data[1])


print(n_pow(a, n))