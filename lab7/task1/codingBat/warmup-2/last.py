def last2(str):
  a = str[len(str)-2: len(str)]
  b = str[:len(str)-1]
  count = 0
  for i in range(1,len(b)):
    if (b[i-1] + b[i]) == a:
      count += 1
  return count