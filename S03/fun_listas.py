import math
operaciones = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y, 
    lambda x, y: x / y if y != 0 else float("indefinida"), 
    lambda x, y: x ** y,
    lambda x: math.sqrt(x) if x >= 0 else float("indefinida"), 
    lambda x: x ** (1/3) 
]
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
    if 1 <= opcion <= 5:
        print("Resultado:", operaciones[opcion - 1](a, b))
    elif opcion == 6:
        print("Raiz cuadrada de", a, ":", operaciones[opcion - 1](a))
        print("Raiz cuadrada de", b, ":", operaciones[opcion - 1](b))
    elif opcion == 7:
        print("Raiz cubica de", a, ":", operaciones[opcion - 1](a))
        print("Raiz cubica de", b, ":", operaciones[opcion - 1](b))
    else:
        print("no valida")

ejecutar_calculadora()
