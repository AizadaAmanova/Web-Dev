a = input()
sum = 0

b = len(a) - 1
for i in a:
    sum+=(int(i)* (2**b))
    b-=1

print(sum)