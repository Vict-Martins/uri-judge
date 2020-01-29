l1 = input().split(" ")
A, B, C = l1

TRIANGULO = (float(A)*float(C))/2
CIRCULO = (float(C)*float(C))*3.14159
TRAPEZIO = ((float(A)+float(B))*float(C))/2
QUADRADO = float(B)*float(B)
RETANGULO = float(A)*float(B)

print("TRIANGULO: %.3f" %TRIANGULO)
print("CIRCULO: %.3f" %CIRCULO)
print("TRAPEZIO: %.3f" %TRAPEZIO)
print("QUADRADO: %.3f" %QUADRADO)
print("RETANGULO: %.3f" %RETANGULO)