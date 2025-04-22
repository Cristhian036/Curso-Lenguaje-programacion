import math
from functools import reduce

def suma(numeros): return reduce(lambda a, b: a + b, numeros)
def resta(numeros): return reduce(lambda a, b: a - b, numeros)
def multiplicacion(numeros): return reduce(lambda a, b: a * b, numeros)
def division(numeros): return reduce(lambda a, b: a / b if b != 0 else float('inf'), numeros)
def potencia(numeros): return list(map(lambda x: x ** numeros[-1], numeros[:-1]))
def raiz_cuadrada(numeros): return list(map(lambda x: math.sqrt(x) if x >= 0 else "indefinido", numeros))
def raiz_cubica(numeros): return list(map(lambda x: x ** (1/3), numeros))

def menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz cubica")
    print("8. Salir")

while True:
    menu()
    opcion = int(input("Elija una operación: "))

    if opcion in range(1, 8):
        numeros = list(map(float, input("Ingrese Numeros separados por espacio: ").split()))
        funciones = [suma, resta, multiplicacion, division, potencia, raiz_cuadrada, raiz_cubica]
        nombres = ["Suma", "Resta", "Multiplicacion", "Division", "Potencia", "Raiz cuadrada", "Raiz cubica"]
        resultado = funciones[opcion - 1](numeros)
        print(f"\nOperación realizada: {nombres[opcion - 1]}")
        print(f"Numeros ingresados: {numeros}")
        print(f"Resultado: {resultado}")
    elif opcion == 8:
        print("Finalizado")
        break
    else:
        print("no valido")

    continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
    if continuar != 's':
        print("Finalizado")
        break
