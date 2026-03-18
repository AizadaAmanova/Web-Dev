def monkey_trouble(a_smile, b_smile):
  if (a_smile  and b_smile) or not(a_smile  or b_smile ):
    return True
  return False
  
  
  
monkey_trouble(True, True)
monkey_trouble(False, False)
monkey_trouble(True, False) 