N = int(input())

if N == 0:
    print("NO")
elif N == 1:
    print("YES")
else:
    temp = N
    while temp % 2 == 0:
        temp //= 2
    
    if temp == 1:
        print("YES")
    else:
        print("NO")