a = int(input())
b = int(input())


result = []
for i in range(a,b+1):
    if int(i**0.5)**2 == i:
        result.append(i)

print(*result)