#Realizar una calculadora usando funciones, con variables precargadas.
import math

a = 10
b = 0

def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    return x / y if y != 0 else "indefinido"
def potencia(x, y):
    return x ** y
def raiz_cuadrada(x):
    return math.sqrt(x) if x >= 0 else "indefinido"
def raiz_cubica(x):
    return x ** (1/3)

print("Suma:", suma(a, b))
print("Resta:", resta(a, b))
print("Multiplicacion:", multiplicacion(a, b))
print("Division:", division(a, b))
print("Potencia:", potencia(a, b))
print("Raiz cuadrada de", a, ":", raiz_cuadrada(a))
print("Raiz cubica de", a, ":", raiz_cubica(a))
print("Raiz cuadrada de", b, ":", raiz_cuadrada(b))
print("Raiz cubica de", b, ":", raiz_cubica(b))
