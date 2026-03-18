def near_hundred(n):
  if (abs(n - 100 ) <= 10) or (abs(n-200) <= 10):
    return True
  return False
  
near_hundred(93)
near_hundred(90)
near_hundred(89) 
