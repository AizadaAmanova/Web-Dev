n = int(input())
arr = list(map(int, input().split()))

reversed_arr = arr[::-1]

print(*reversed_arr)