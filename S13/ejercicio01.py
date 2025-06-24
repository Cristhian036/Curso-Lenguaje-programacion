#PM – Instrucciones Repetitivas FOR
frutas=["manzana", "pera", "naranja", "kiwi", "sandía"]
for fruta in frutas:
    print(fruta)

# PM – Instrucciones Repetitivas RANGE
for i in range(0, 5):
    print(i)

# PM – Instrucciones Repetitivas WHILE
x = 5
while x > 0:
    print(x)
    x -= 1

x = 5
while x > 0:
    x -= 1
    print(x)
    
# PM – Arreglos Unidimensionales
numeros = [8,3,14,1]
suma = sum(numeros)
maxima = max(numeros)
minima = min(numeros)
print("Suma:", suma)
print("Máximo:", maxima)
print("Mínimo:", minima)

# PM – Arreglos Bidimensionales
tabla = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print("Tabla 3x3 (1-3): ")
for fila in tabla:
    print(fila)