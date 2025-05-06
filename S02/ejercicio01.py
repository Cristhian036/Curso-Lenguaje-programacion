#Realizar una calculadora usando variables, con variables precargadas
import math

a = -10
b = 8

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b if b != 0 else "indefinido"
potencia = a ** b
raiz_cuadrada_a = math.sqrt(a) if a >= 0 else "indefinido"
raiz_cubica_a = a ** (1/3)
raiz_cuadrada_b = math.sqrt(b) if b >= 0 else "indefinido"
raiz_cubica_b = b ** (1/3)

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Potencia:", potencia)
print("Raíz cuadrada de", a, ":", raiz_cuadrada_a)
print("Raíz cúbica de", a, ":", raiz_cubica_a)
print("Raíz cuadrada de", b, ":", raiz_cuadrada_b)
print("Raíz cúbica de", b, ":", raiz_cubica_b)
