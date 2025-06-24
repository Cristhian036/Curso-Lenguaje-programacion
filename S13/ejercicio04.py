#Enunciado 1
calificaciones = []
while True:
    calificacion = input("Ingrese una calificación (o -1 para finalizar): ")
    if calificacion == '-1':
        break    
    try:
        calificacion = float(calificacion)
        calificaciones.append(calificacion)
    except ValueError:
        print("Por favor, ingrese una calificación válida.")
print("Las calificaciones ingresadas son:", calificaciones)
print("El programa ha finalizado.")

# Enunciado 2
numeros = []
while True:
    try:
        numero = int(input("Ingrese un número entre 1 y 1000: "))
        
        if 1 <= numero <= 1000:
            numeros.append(numero)
        else:
            print("Por favor, ingrese un número entre 1 y 1000.")
            continue

        continuar = input("¿Desea continuar? (Sí/No): ").lower()
        if continuar in ['no', 'n']:
            break
        elif continuar not in ['sí', 'si', 's', 'no', 'n']:
            print("Respuesta no válida. El programa finalizará.")
            break

    except ValueError:
        print("Por favor, ingrese un número válido.")
print("Los números ingresados son:", numeros)
print("El programa ha finalizado.")

# Enunciado 3
numero = int(input("Ingrese el número 5: "))

if numero == 5:
    for i in range(1, numero + 1):
        print('*' * (2*i - 1))
else:
    print("El número ingresado no es 5.")

