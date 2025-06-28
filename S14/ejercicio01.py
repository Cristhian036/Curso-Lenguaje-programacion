#PM LISTA
lista1 = [5, 1, 3]
print(lista1)

lista2 = list("12345")
print(lista2)

#PM SET
s= set([5,4,6,8,8,1])
print(s)
print(type(s))

s = {5, 4, 6, 8, 8, 1}
print(s)
print(type(s))

#PM TUPLA
tupla1 = (5, 1, 3)
print(tupla1)

tupla2 = 1, 2, 3
print(type(tupla2))
print(tupla2)

#PM DICCIONARIO
d1 = { "nombre": "Rene", "edad": 38, "documento": 41856757 }
print(d1)

#PM FUNCIONES
def funcion(x):
    return 2*x

y= funcion(3)
print(y)

#PM MODULOS
    #MAP
lista_map= [1, 2, 3, 4, 5]
def por_dos(x):
    return x * 2
lista_pordos = map(por_dos, lista_map)
print(list(lista_pordos))

    #FILTER
lista_filter = [1, 2, 3, 4, 5]
pares = filter(lambda x: x % 2 == 0, lista_filter)
print(list(pares))

    #REDUCE
from operator import add
from functools import reduce
lista_reduce = [1, 2, 3, 4, 5]
suma = reduce(add, lista_reduce)
print(suma)
