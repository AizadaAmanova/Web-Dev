def swap_case(s):
    a = ""
    for i in range(len(s)):
        if (s[i].isupper()):
            b = s[i].lower()
            a += b
        else:
            b = s[i].upper()
            a+= b
    return a



s = input()
print(swap_case(s))