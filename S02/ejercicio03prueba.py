#Realizar una calculadora usando funciones, con variables precargadas y un
#menú de opciones para calcular la suma, resta, Multiplicacion, Division,
#potencia, Raiz cuadrada, Raiz cubica.
import math
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
def menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Raíz cúbica")
    print("8. Reiniciar valores")
    print("9. Salir")
def calcular(a, b):
    menu()
    opcion = int(input("Elije una operacion"))

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
        print("Raíz cuadrada de", a, ":", raiz_cuadrada(a))
        print("Raíz cuadrada de", b, ":", raiz_cuadrada(b))
    elif opcion == 7:
        print("Raíz cúbica de", a, ":", raiz_cubica(a))
        print("Raíz cúbica de", b, ":", raiz_cubica(b))
    elif opcion == 8:
        return True  # reiniciar valores
    elif opcion == 9:
        return False  # salir
    else:
        print("Opción no válida")
    return None

while True:
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    while True:
        reiniciar = calcular(a, b)
        if reiniciar is False:
            break
        elif reiniciar is True:
            break
