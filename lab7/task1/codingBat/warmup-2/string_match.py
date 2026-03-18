def string_match(a, b):
  count = 0
  for i in range(1,len(a)):
    if (a[i-1]+a[i]) in b:
      if (i<len(b)) :
        if (a[i-1] + a[i] == b[i-1] + b[i]):
          count += 1
  return count