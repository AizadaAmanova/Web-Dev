import math
n = int(input())
a = 1
while(a < n+1 ):
    root = int(math.sqrt(a))
    if (root * root == a ):
        print(a)
    a+=1