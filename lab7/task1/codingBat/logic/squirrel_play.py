def squirrel_play(temp, is_summer):
  if (temp >= 60 and temp <= 90) and  is_summer == False : return True
  elif (is_summer == True and temp >= 60 and temp<= 100):  return True
  return False
