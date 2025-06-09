def obtener_dato(message):
    while True:
        try:
            dato = input(message)
            return dato
        except ValueError:
            print("¡Error! Debes ingresar un valor válido. Intenta de nuevo.")

def obtener_float(message):
    while True:
        try:
            valor = float(input(message))
            return valor
        except ValueError:
            print("¡Error! Debes ingresar un número válido. Intenta de nuevo.")


codigo_producto = obtener_dato("Ingresa el código del producto: ")
nombre_producto = obtener_dato("Ingresa el nombre del producto: ")
cantidad_producto = obtener_float("Ingresa la cantidad del producto: ")
precio_producto = obtener_float("Ingresa el precio del producto: ")

IGV = 0.18  
precio_sin_igv = precio_producto * cantidad_producto
precio_igv = precio_sin_igv * IGV
precio_total = precio_sin_igv + precio_igv

print("\n--- Detalles del producto ---")
print(f"Código del producto: {codigo_producto}")
print(f"Nombre del producto: {nombre_producto}")
print(f"Cantidad: {cantidad_producto}")
print(f"Precio unitario: S/{precio_producto:.2f}")
print(f"Precio sin IGV: S/{precio_sin_igv:.2f}")
print(f"IGV (18%): S/{precio_igv:.2f}")
print(f"Precio total con IGV: S/{precio_total:.2f}")
