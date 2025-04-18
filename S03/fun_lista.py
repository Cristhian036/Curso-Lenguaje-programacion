
def sumar(num):
    total = 0
    for n in num:
        total += n
    return total

a = int(input("Ingrese el 1er numero: "))
b = int(input("Ingrese el 2do numero: "))

resultado = sumar([a, b])
print("La suma es:", resultado)

