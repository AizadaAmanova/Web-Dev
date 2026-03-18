n = int(input())
array = list(map(int, input().split()))
cnt = 0
for el in array:
    if el> 0:
        cnt +=1
print(cnt)