import math
def prime(a):
    if (a == 2): return True
    if (a % 2 == 0): return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if (a % i == 0): 
            return False
    return True



a = int(input())
if( prime(a)):
    print("prime")
else: 
    print("composite")