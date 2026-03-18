a = int(input())
b = 0
for i in range(1, a + 1):
    for j in range(i):
        b+= 1
        if b<=a:
            print(i, end = " ")
        else: 
            break
        
