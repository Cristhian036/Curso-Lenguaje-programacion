#PM - Ejemplo 01
for num in range(0, 11, 2):
        print(num)

# PM - Ejemplo 02
a, b = 0, 1
count = 0
n = 7
while count < n:
    print(a)
    a, b = b, a + b
    count += 1

# PM - Ejemplo 03
table = 3
for i in range(1, 11):
    print(f"{table} x {i} = {table * i}")

# PM - Ejemplo 04
list_numbers = [1, 2, 3, 4, 5]
inverted_list = list_numbers[::-1]
print("Lista original:", list)
print("Lista invertida:", inverted_list[::-1])

# PM - Ejemplo 05
matriz = [
     [5,1,3],
     [2,4,6],
     [7,8,9]
]
diagonal = [matriz[i][i] for i in range(len(matriz))]
print("Matriz")
for fila in matriz:
    print(fila) 
print("Diagonal principal:", diagonal)