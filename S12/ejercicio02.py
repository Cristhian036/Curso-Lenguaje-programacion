#Enunciado 1: Escribe un programa que solicite una oración y cuente cuántas palabras tiene.

print("Enunciado 1")
oracion = input("Introduce una oración: ")
contador_palabras = oracion.split()
print(f"La oración tiene {contador_palabras} palabras.")
print(f"La oración tiene {len(contador_palabras)} palabras.")

#Enunciado 2: Escribe un programa que determine si una palabra ingresada es un palíndromo (se lee igual al derecho y al revés).
print("\nEnunciado 2")
palabra = input("Introduce una palabra: ")
if palabra == palabra[::-1]:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")

#Enunciado 3: Escribe un programa que clasifique una cadena ingresada como corta, mediana o larga, según su cantidad de caracteres
print("\nEnunciado 3")
def clasificar_cadena(cadena):
    longitud = len(cadena)
    if longitud < 5:
        return "La cadena es corta."
    elif 5 <= longitud <= 15:
        return "La cadena es mediana."
    else:
        return "La cadena es larga."

cadena = input("Introduce una cadena de texto: ")
print(clasificar_cadena(cadena))

