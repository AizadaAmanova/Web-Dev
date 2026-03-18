import math
x = int(input())
sum = 0
for i in range(1, int(math.sqrt(x)) + 1):
    if (x%i == 0):
        if i*i == x:
            sum+=1
        else: 
            sum +=2

print(sum)
