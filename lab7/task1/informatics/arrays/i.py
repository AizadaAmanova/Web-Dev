n  = int(input())
array = list(map(int, input().split()))



first_element = array[0]
last_element = array[-1]
array.pop()
for i in range(n):
    array[i+1] = array[i]
array[-1] = first_element
array[0] = last_element
for i in range(n):
    print(array[i], end = " ")

