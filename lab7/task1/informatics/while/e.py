import math
n = int(input())
a = 0
while (a<n):
    if (math.pow(2, a )>=n):
        print(a)
        break
    a+=1
