n = int(input())
arr = list(map(int, input().split()))

result = []
for i in range(0, n, 2):
    result.append(arr[i])

print(*result)