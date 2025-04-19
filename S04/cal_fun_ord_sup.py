import math
import typing as t
from functools import reduce

num = t.TypeVar("num", int, float)

def operation(x: num, y: num, fun):
    return fun(x, y)
def suma(x: num, y: num) -> num: 
    return x + y
def resta(x: num, y: num) -> num: 
    return x - y
def multiplicacion(x: num, y: num) -> num: 
    return x * y
def division(x: num, y: num) -> float: 
    return x / y if y != 0 else float("inf")
def potencia(x: num, y: num) -> num: 
    return x ** y
def raiz_cuadrada(x: num) -> float: 
    return math.sqrt(x) if x >= 0 else float("nan")
def raiz_cubica(x: num) -> float: 
    return x ** (1 / 3)
operaciones = {
    "1": suma, 
    "2": resta, 
    "3": multiplicacion,
    "4": division, 
    "5": potencia, 
    "6": raiz_cuadrada, 
    "7": raiz_cubica,
}

while True:
    a, b = float(input("\nIngrese el 1er número: ")), float(input("Ingrese el 2do número: "))

    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz cubica")
    
    opcion = input("Elija una operación: ")

    if opcion in operaciones:
        funcion = operaciones[opcion]
        if opcion in ["6", "7"]:
            print(f"Resultado de {a}: {funcion(a)}\nResultado de {b}: {funcion(b)}")
        else:
  