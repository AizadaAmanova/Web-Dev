def cigar_party(cigars, is_weekend):
  if ((cigars >= 40 ) and is_weekend == True) or (cigars >= 40 and cigars <= 60 and is_weekend == False ):
    return True
 
  return False
  
  
  

