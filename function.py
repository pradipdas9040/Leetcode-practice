def swap(a, b):
  '''
  This function will swap two variables without using any other variables 
  '''
  a = a + b
  b = a - b
  a = a - b
  return a, b
