binary = input()
decimal = 0

for i, digit in enumerate(binary[::-1]):
    decimal += int(digit) * (2 ** i)

print(decimal)