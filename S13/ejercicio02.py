# Programa que solicita información de empleado usando estructuras repetitivas

# Variables globales para almacenar datos
nombre = ""
tipo_empleado = ""
salarios = []
boletas = []
meses = ["ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC"]
datos_ingresados = False

def mostrar_menu():
    print("\n========== SISTEMA DE EMPLEADOS ==========")
    print("1. Ingresar nombre y tipo de empleado")
    print("2. Ingresar salarios y boletas mensuales")
    print("3. Mostrar reporte ASCII")
    print("4. Salir")
    print("==========================================")

def opcion1():
    global nombre, tipo_empleado
    print("\n--- OPCIÓN 1: DATOS DEL EMPLEADO ---")
    nombre = input("Ingrese el nombre del empleado: ")
    
    while True:
        tipo_empleado = input("Ingrese el tipo de empleado (contratado/nombrado): ").lower()
        if tipo_empleado in ["contratado", "nombrado"]:
            break
        print("Error: Debe ingresar 'contratado' o 'nombrado'")
    
    print(f"✓ Datos guardados: {nombre} - {tipo_empleado.capitalize()}")

def opcion2():
    global salarios, boletas, datos_ingresados
    
    if not nombre:
        print("Error: Primero debe ingresar los datos del empleado (Opción 1)")
        return
    
    print("\n--- OPCIÓN 2: SALARIOS Y BOLETAS ---")
    
    # Solicitar número de meses a ingresar
    while True:
        try:
            num_meses = int(input("¿Cuántos meses desea ingresar? (1-12): "))
            if 1 <= num_meses <= 12:
                break
            print("Error: Debe ingresar un número entre 1 y 12")
        except ValueError:
            print("Error: Debe ingresar un número válido")
    
    # Limpiar datos anteriores
    salarios.clear()
    boletas.clear()
    
    # Usar for y range para ingresar datos
    for i in range(num_meses):
        print(f"\n--- Mes {i+1}: {meses[i]} ---")
        
        while True:
            try:
                salario = float(input(f"Ingrese salario de {meses[i]}: S/ "))
                if salario >= 0:
                    salarios.append(salario)
                    break
                print("Error: El salario no puede ser negativo")
            except ValueError:
                print("Error: Debe ingresar un número válido")
        
        while True:
            try:
                boleta = int(input(f"¿Boletas emitidas en {meses[i]}? (1=SI/0=NO): "))
                if boleta in [0, 1]:
                    boletas.append(boleta)
                    break
                print("Error: Debe ingresar 1 para SI o 0 para NO")
            except ValueError:
                print("Error: Debe ingresar un número válido")
    
    datos_ingresados = True
    print(f"✓ Datos de {num_meses} meses guardados correctamente")

def opcion3():
    if not datos_ingresados or not nombre:
        print("Error: Debe ingresar todos los datos antes de generar el reporte")
        print("- Use Opción 1 para ingresar datos del empleado")
        print("- Use Opción 2 para ingresar salarios y boletas")
        return
    
    print("\n########## RESUMEN DE BOLETAS DE PAGO ##########")
    print(f"Empleado: {nombre}")
    print(f"Tipo: {tipo_empleado.capitalize()}")
    print("\n######## Datos del Salario ########")
    
    # Mostrar datos usando for y range
    for i in range(len(salarios)):
        estado_boleta = "SI" if boletas[i] == 1 else "NO"
        print(f"Salario {meses[i]}: S/ {salarios[i]:.2f}  Boleta: {estado_boleta}")
    
    print("\n###############################################")
    print(f"Total meses registrados: {len(salarios)}")
    print(f"Boletas emitidas: {sum(boletas)}")
    print(f"Monto total pagado: S/ {sum(salarios):.2f}")
    print(f"Promedio mensual: S/ {sum(salarios)/len(salarios):.2f}")
    print("###############################################")

# Programa principal
def main():
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            
            if opcion == 1:
                opcion1()
            elif opcion == 2:
                opcion2()
            elif opcion == 3:
                opcion3()
            elif opcion == 4:
                print("¡Gracias por usar el sistema!")
                break
            else:
                print("Error: Opción no válida. Ingrese un número del 1 al 4")
                
        except ValueError:
            print("Error: Debe ingresar un número válido")

# Ejecutar programa
if __name__ == "__main__":
    main()
