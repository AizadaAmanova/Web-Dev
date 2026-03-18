import math
h = int(input())
a = int(input())
b = int(input())

t = math.ceil((h-a)/(a-b)) + 1
print(t)