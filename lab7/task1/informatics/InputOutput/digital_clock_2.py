n = int(input())
h = n //60 //60 %24
m = n//60 % 60
s = n % 60
print(f"{h}:{m:02d}:{s:02d}")