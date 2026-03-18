n = int(input())
array = list(map(int, input().split()))
array.reverse()
for el in array :
    print(el, end = " ")