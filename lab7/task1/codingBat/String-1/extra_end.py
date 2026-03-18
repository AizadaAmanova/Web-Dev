def extra_end(str):
  if (len(str)<=2):
    return str*3
  else:
    return (str[len(str)-2:len(str)])*3

