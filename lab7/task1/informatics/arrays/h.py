n = int(input())
array = list(map(int, input().split()))
for i in range(0, n-1, 2):
    array[i], array[i+1] = array[i+1], array[i]
for el in array:
    print(el, end = " ")

    