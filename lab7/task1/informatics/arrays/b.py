n = int(input())
array = list(map(int,input().split()))
for el in array :
    if el%2 == 0:
        print(el, end = " ")