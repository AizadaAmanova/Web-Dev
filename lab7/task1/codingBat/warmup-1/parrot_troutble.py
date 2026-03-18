def parrot_trouble(talking, hour):
  if (talking and (hour < 7 or hour > 20)):
    return True
  return False
  
  
parrot_trouble(True, 6)
parrot_trouble(True, 7)
parrot_trouble(False, 6)
