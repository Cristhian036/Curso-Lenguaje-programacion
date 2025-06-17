#PM – Cadenas de Texto
cadena1 = "Hola, soy Dany"
cadena2 = "Python es un lenguaje de programación"

print(cadena1, cadena2)

#PM – Cadenas de Texto – Operaciones
texto = " Hola mundo "
print(texto.strip())
print(texto.upper())
print(texto.replace("Hola", "Adiós"))

    #Acceder a un carácter específico
print(texto[5])

    #Concatenación y repetición
nombre = "Dany"
mensaje = "Hola, " + nombre + "!"

print(mensaje)
print(nombre * 3)

#PM – if – else.
edad = int(input("Introduce tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

#PM – elif.

nota = int(input("Introduce tu nota: "))

if nota >= 20:
    print("Excelente trabajo!")
elif nota >= 12:
    print("Aprobaste")
else:   
    print("Necesitas mejorar")

#PM – switch – case

def obtener_mensaje(opciones):
    switcher = {
        1: "Opción 1 seleccionada",
        2: "Opción 2 seleccionada",
        3: "Opción 3 seleccionada"
    }
    return switcher.get(opciones, "Opción no válida")

opcion = int(input("Selecciona una opción (1 - 3): "))
print(obtener_mensaje(opcion))

#PM – if – elif – else.

opcion = int(input("Selecciona una opción (1 - 3): "))
if opcion == 1:
    print("Has seleccionado la opción 1")
elif opcion == 2:
    print("Has seleccionado la opción 2")
elif opcion == 3:
    print("Has seleccionado la opción 3")
else:
    print("Opción no válida")

#PM – CADENAS DE TEXTO Y CONDICIONALES – EJERCICIOS

# Ejercicio 1: Verificar cuantos caracteres tiene una cadena de texto
longitud = input("Introduce una cadena de texto: ")
print(f"La cadena tiene {len(longitud)} caracteres.")

#Ejercicio 2: Mayusculas y minúsculas
muyusminus = input("Introduce una cadena de texto: ")
print(f"La cadena en mayúsculas es: {muyusminus.upper()}")
print(f"La cadena en minúsculas es: {muyusminus.lower()}")

# Ejercicio 3: Verificar si contenía una palabra específica
palabra = input("Introduce una cadena de texto: ")
if "Python" in palabra:
    print("La cadena contiene la palabra 'Python'.")
else:
    print("La cadena no contiene la palabra 'Python'.")

    