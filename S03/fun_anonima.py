#FUNCION ANONIMA

import math
suma = lambda x, y: x + y
resta = lambda x, y: x - y
multiplicacion = lambda x, y: x * y
division = lambda x, y: x / y if y != 0 else "indefinido"
potencia = lambda x, y: x ** y
raiz_cuadrada = lambda x: math.sqrt(x) if x >= 0 else "indefinido"
raiz_cubica = lambda x: x ** (1/3)

def menu():
    print("\nSeleccione una operacion:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz cuadrada")
    print("7. Raiz cubica")

a = int(input("Ingrese el 1er numero: "))
b = int(input("Ingrese el 2do numero: "))

menu()
opcion = int(input("Elija una operacion: "))

if opcion == 1:
    print("Resultado: ", suma(a, b))
elif opcion == 2:
    print("Resultado: ", resta(a, b))
elif opcion == 3:
    print("Resultado: ", multiplicacion(a, b))
elif opcion == 4:
    print("Resultado: ", division(a, b))
elif opcion == 5:
    print("Resultado: ", potencia(a, b))
elif opcion == 6:
    print("Raiz cuadrada de ", a, " : ", raiz_cuadrada(a))
    print("Raiz cuadrada de ", b, " : ", raiz_cuadrada(b))
elif opcion == 7:
    print("Raiz cubica de ", a, " : ", raiz_cubica(a))
    print("Raiz cubica de ", b, " : ", raiz_cubica(b))
else:
    print("no valido")
