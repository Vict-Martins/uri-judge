a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if(a+b>c and a+c>b and b+c>a):
  print('S')
elif(a+b>d and a+d>b and b+d>a):
  print('S')
elif(b+c>d and b+d>c and c+d>b):
  print('S')
elif(a+c>d and a+d>c and c+d>a):
  print('S')
else:
  print('N')