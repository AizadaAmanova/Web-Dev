n = int(input())
numbers = input().split()
t = tuple(map(int, numbers))
print(hash(t))