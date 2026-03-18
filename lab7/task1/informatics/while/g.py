import math
x = int(input())
p = int(input())
y = int(input())

money = x * 100
target = y * 100
years = 0

while money < target:
   
    money += (money * p) // 100
    years += 1

print(years)