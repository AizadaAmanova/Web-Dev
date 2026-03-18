n = int(input())
arr = list(map(int, input().split()))
result = []
for i in range(n):
    if arr[i] % 2 == 0:
        result.append(arr[i])

print(*result)