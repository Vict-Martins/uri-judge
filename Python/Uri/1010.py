linha1 = input().split(" ")
linha2 = input().split(" ")

A, B, C = linha1
D, E, F = linha2

TOTAL = (int(B)*float(C))+(int(E)*float(F))
print("VALOR A PAGAR: R$ %0.2f" %TOTAL)