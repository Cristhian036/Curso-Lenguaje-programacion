def buscar_elemento(x, lista):
    if not lista:
        return False
    if x == lista[0]:
        return True
    return buscar_elemento(x, lista[1:])
print(buscar_elemento(2, [1, 2, 3]))
print(buscar_elemento(4, [1, 2, 3]))