#Enunciado 1: Escribe un programa que cuente cuántas veces aparece cada letra en una cadena ingresada.
print("Enunciado 1")
cadena = input("Introduce una cadena de texto: ")
contador_letras = {}
for letra in cadena:
    if letra.isalpha():  # Contar solo letras
        contador_letras[letra] = contador_letras.get(letra, 0) + 1
print("Frecuencia de letras:")
for letra, frecuencia in contador_letras.items():
    print(f"'{letra}': {frecuencia}")

#Enunciado 2: Crea un menú de opciones donde el usuario pueda elegir entre:
#1. Mostrar cadena en mayúsculas.
#2. Mostrar cadena en minúsculas.
#3. Contar caracteres
print("\nEnunciado 2")

cadena_texto = input("Escribe una frase: ")

while True:
    print("\n--- MENÚ ---")
    print("1. Mostrar en mayúsculas")
    print("2. Mostrar en minúsculas") 
    print("3. Contar caracteres")
    print("4. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        print("En mayúsculas:", cadena_texto.upper())
    elif opcion == "2":
        print("En minúsculas:", cadena_texto.lower())
    elif opcion == "3":
        print("Número de caracteres:", len(cadena_texto))
    elif opcion == "4":
        print("¡Adiós!")
        break
    else:
        print("Opción incorrecta, intenta otra vez")

#Enunciado 3: Un pangrama es una frase que contiene todas las letras del abecedario al menos una vez. Escribe un programa que determine si una frase es un pangrama
print("\nEnunciado 3")
frase = input("Introduce una frase para verificar si es un pangrama: ")
abecedario = set("abcdefghijklmnopqrstuvwxyz")
frase_letras = set(frase.lower())
if abecedario.issubset(frase_letras):
    print("La frase es un pangrama.")
else:
    print("La frase NO es un pangrama.")
