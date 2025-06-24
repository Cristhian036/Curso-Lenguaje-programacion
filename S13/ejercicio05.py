#Enunciado 1
conjunto_A = set()
for i in range(10):
    num = int(input(f"Ingrese el número {i+1} para el conjunto A: "))
    conjunto_A.add(num)

conjunto_B = set()
for i in range(10):
    num = int(input(f"Ingrese el número {i+1} para el conjunto B: "))
    conjunto_B.add(num)

print("\nUnión de A y B:", conjunto_A | conjunto_B)
print("Intersección de A y B:", conjunto_A & conjunto_B)
print("Diferencia de A y B:", conjunto_A - conjunto_B)

#Enunciado 2
personas = []
for i in range(5):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    personas.append((nombre, edad))
print("\nArreglo original:")
for persona in personas:
    print(persona)
personas_ordenadas = sorted(personas, key=lambda x: x[1])

print("\nArreglo final ordenado por edad:")
for persona in personas_ordenadas:
    print(persona)
