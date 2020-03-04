c = int(input(""))
aux = 0
aux1 = 0
maior = 0
ident = 0
for i in range(c):
  a, b = input('').split()
  a = int(a)
  b = float(b)
  aux = int(a)
  aux1 = float(b)
  if aux1 > maior:
    maior = float(aux1)
    ident = int(aux)
  
if maior>=8:
  print(ident)
else:
  print('Minimum note not reached') 
