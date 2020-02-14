e = int(input(''))
soma = 0
for i in range(e):
  e1 = int(input(''))
  for x in range(e1):
    s = str(input(''))
    for y in range(len(s)):
      soma += (ord(s[y])-65)+x+y
  print(soma)
  soma = 0;