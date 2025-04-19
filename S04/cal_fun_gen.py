import math
import typing as t

num = t.TypeVar("num", int, float)
def suma(x: num, y: num) -> num:
    return x + y
def resta(x: num, y: num) -> num:
    return x - y
def multiplicacion(x: num, y: num) -> num:
    return x * y
def division(x: num, y: num) -> float:
    return x / y if y != 0 else float("infinido")
def potencia(x: num, y: num) -> num:
    return x ** y
def Raiz_cuadrada(x: num) -> float:
    return math.sqrt(x) if x >= 0 else float("indefinido")
def Raiz_cubica(x: num) -> float:
    return x ** (1 / 3)
operaciones = {
    "1": suma,"2": resta,"3": multiplicacion,"4": division,"5": potencia,"6": Raiz_cuadrada,"7": Raiz_cubica,
}
while True:
    print("\nCALCULADORA")
    a = float(input("Ingrese el 1er número: "))
    b = float(input("Ingrese el 2do número: "))

    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz cubica")

    opcion = input("\nElija una operacion: ")

    if opcion in operaciones:
        funcion = operaciones[opcion]
        if opcion == "6":
            print("\nRAIZ CUADRADA")
            print(f"Resultado de ({a}): {funcion(a)}")
            print(f"Resultado de ({b}): {funcion(b)}")
        elif opcion == "7":
            print("\nRAIZ CUBICA")
            print(f"Resultado de ({a}): {funcion(a)}")
            print(f"Resultado de ({b}): {funcion(b)}")
        else:
            print("\nResultado:", funcion(a, b))
    else:
        print("\nNO VALIDO")

    condicion = input("\n¿Desea realizar otra operación? (s/n): ").strip().lower()
    if condicion != "s":
        print("\nFINALIZADO")
        print("\n")
        break
