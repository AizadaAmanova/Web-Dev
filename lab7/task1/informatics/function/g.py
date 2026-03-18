def power(a, n):
    if (n % 2 == 0):
        p = a ** 2
        p = p** (n/2)
        return p
    else :
        p = a ** (n-1)
        p = p * a
        return p
    



data = input().split()
a = float(data[0])
n = int(data[1])

print(power(a,n))