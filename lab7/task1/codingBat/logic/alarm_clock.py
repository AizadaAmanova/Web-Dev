def alarm_clock(day, vacation):
  days = [1,2,3,4,5]
  if (day in days ) and vacation == False:
    return "7:00"
  elif (day in days) and vacation == True:
    return "10:00"
  elif (day == 0 or day == 6) and vacation == True :
    return "off"
  else: 
    return "10:00"
    
