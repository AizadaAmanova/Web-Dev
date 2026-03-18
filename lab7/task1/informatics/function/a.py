array = list(map(int, input().split()))



def minimum4(array):
   
    min = array[0]
    for i in array:
        if (min>i):
            min = i
    return min
        



print(minimum4(array))



    
