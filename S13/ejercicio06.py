cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
alumnos = []
for i in range(cantidad_estudiantes):
    nombre = input(f"Ingrese el nombre del estudiante {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    grado = int(input(f"Ingrese el grado de {nombre}: "))
    pc1 = float(input(f"Ingrese la nota de PC1 para {nombre}: "))
    pc2 = float(input(f"Ingrese la nota de PC2 para {nombre}: "))
    pc3 = float(input(f"Ingrese la nota de PC3 para {nombre}: "))
    ef = float(input(f"Ingrese la nota de EF para {nombre}: "))
    alumno = [nombre, edad, grado, [pc1, pc2, pc3, ef]]
    alumnos.append(alumno)
promedios_alumnos = []
total_promedio = 0
print("############################# REPORTE DE NOTAS #############################")
print("NOMBRE                              EDAD   GRADO   PC1   PC2   PC3   EF   PROM")
print("#######################################################################")
for alumno in alumnos:
    nombre = alumno[0]
    edad = alumno[1]
    grado = alumno[2]
    notas = alumno[3]    
    promedio = sum(notas) / len(notas)
    promedios_alumnos.append(promedio)
    total_promedio += promedio  
    print(f"{nombre:35} {edad:5} {grado:6} {notas[0]:5.2f} {notas[1]:5.2f} {notas[2]:5.2f} {notas[3]:5.2f} {promedio:5.2f}")
promedio_total_clase = total_promedio / len(alumnos)  
print("#######################################################################")
print(f"PROMEDIO TOTAL DE LA CLASE: {promedio_total_clase:5.2f}")