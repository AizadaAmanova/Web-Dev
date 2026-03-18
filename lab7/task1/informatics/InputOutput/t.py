n = int(input())

d1 = n // 1000          
d2 = (n // 100) % 10    
d3 = (n // 10) % 10     
d4 = n % 10             


rev = d4 * 1000 + d3 * 100 + d2 * 10 + d1


print(abs(n - rev) + 1)