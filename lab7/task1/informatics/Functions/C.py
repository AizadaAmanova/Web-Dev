def xor(x, y):
    return (x and not y) or (not x and y)

x, y = map(int, input().split())
x_bool = bool(x)
y_bool = bool(y)

result = xor(x_bool, y_bool)
print(1 if result else 0)