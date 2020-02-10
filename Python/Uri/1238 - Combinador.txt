np = ''
e = int(input(''))
for i in range(e):
  p = str(input('')).split()
  p1,p2 = p
  c1 = len(p1)
  c2 = len(p2)
  if(c1 > c2):
    maior = c1
  else:
    maior = c2
  for x in range(maior):
    if(x < c1):
      np += str(p1[x])
    if(x < c2):  
      np += str(p2[x])
    if(x == maior-1):
      print(np)
      np = ''
    
