def obtener_numero():
    while True:
        try:
            numero = int(input("Ingresa un número entero: "))
            return numero
        except ValueError:
            print("¡Error! Debes ingresar un número entero. Intenta de nuevo.")


print("Por favor, ingresa tres números enteros.")
a = obtener_numero()
b = obtener_numero()
c = obtener_numero()


numeros = [a, b, c]
numeros.sort()

menor = numeros[0]
medio = numeros[1]
mayor = numeros[2]

print(f"El número menor es: {menor}")
print(f"El número del medio es: {medio}")
print(f"El número mayor es: {mayor}")
