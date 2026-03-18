def fibo(a ):
    if (a == 0 or a == 1):
        return 1
    prev = 1
    current = 1
    next = 1
    for i in range(2, a+1):
        next = prev + current
        prev = current
        current = next


    return next


a = int(input())
print(fibo(a))
















# 0 1 1 2 3 5 8 13 21 34






