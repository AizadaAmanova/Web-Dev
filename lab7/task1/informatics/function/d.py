def vote(a, b, c ):
    t = 0
    f = 0
    if (bool(a) == True):
        t+=1
    else : f+=1

    if (bool(b) == True):
        t+=1
    else : f+=1

    if (bool(c) == True):
        t+=1
    else : f+=1


    if (t>f):
        return int(True)
    else: return int(False)
    
    

    
data = input().split()

a = int(data[0])
b = int(data[1])
c = int(data[2])

print(vote(a,b,c))
