import math
def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def division(x, y):
    return x / y if y != 0 else float("indefinido")
def potencia(x, y):
    return x ** y
def raiz_cuadrada(x):
    return math.sqrt(x) if x >= 0 else float("indefinido")
def raiz_cubica(x):
    return x ** (1/3)
def mostrar_menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz cubica")

def ejecutar_calculadora():
    a = float(input("Ingrese el 1er número: "))
    b = float(input("Ingrese el 2do número: "))

    mostrar_menu()
    opcion = int(input("Elija una operación: "))

    if opcion == 1:
        print("Resultado:", suma(a, b))
    elif opcion == 2:
        print("Resultado:", resta(a, b))
    elif opcion == 3:
        print("Resultado:", multiplicacion(a, b))
    elif opcion == 4:
        print("Resultado:", division(a, b))
    elif opcion == 5:
        print("Resultado:", potencia(a, b))
    elif opcion == 6:
        print("Raiz cuadrada de", a, ":", raiz_cuadrada(a))
        print("Raiz cuadrada de", b, ":", raiz_cuadrada(b))
    elif opcion == 7:
        print("Raiz cubica de", a, ":", raiz_cubica(a))
        print("Raiz cubica de", b, ":", raiz_cubica(b))
    else:
        print("no valido")

ejecutar_calculadora()
