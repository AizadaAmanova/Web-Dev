def no_teen_sum(a, b, c):
   
    return fix_teen(a) + fix_teen(b) + fix_teen(c)

def fix_teen(n):
   
    if 13 <= n <= 19:
        if n == 15 or n == 16:
            return n
        else:
            return 0
    
    return n