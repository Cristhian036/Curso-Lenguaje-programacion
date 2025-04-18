import math
def suma(**kwargs):
    return sum(kwargs.values())
def resta(**kwargs):
    valores = list(kwargs.values())
    return valores[0] - sum(valores[1:])
def multiplicacion(**kwargs):
    resultado = 1
    for valor in kwargs.values():
        resultado *= valor
    return resultado
def division(**kwargs):
    valores = list(kwargs.values())
    return valores[0] / valores[1] if valores[1] != 0 else "indefinido"
def potencia(**kwargs):
    valores = list(kwargs.values())
    return valores[0] ** valores[1]
def raiz_cuadrada(**kwargs):
    return {k: (math.sqrt(v) if v >= 0 else "indefinido") for k, v in kwargs.items()}
def raiz_cubica(**kwargs):
    return {k: v ** (1/3) for k, v in kwargs.items()}
def menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz cúbica")

a = float(input("Ingrese el 1er número: "))
b = float(input("Ingrese el 2do número: "))

menu()
opcion = int(input("Elija una operación: "))

if opcion == 1:
    print("Resultado:", suma(a=a, b=b))
elif opcion == 2:
    print("Resultado:", resta(a=a, b=b))
elif opcion == 3:
    print("Resultado:", multiplicacion(a=a, b=b))
elif opcion == 4:
    print("Resultado:", division(a=a, b=b))
elif opcion == 5:
    print("Resultado:", potencia(a=a, b=b))
elif opcion == 6:
    print("Raiz cuadrada de", a, ":", raiz_cuadrada(a=a))
    print("Raiz cuadrada de", b, ":", raiz_cuadrada(b=b))
elif opcion == 7:
    print("Raiz cúbica de", a, ":", raiz_cubica(a=a))
    print("Raiz cúbica de", b, ":", raiz_cubica(b=b))
else:
    print("Opción no válida")
