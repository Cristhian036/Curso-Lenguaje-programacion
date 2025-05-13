def unificar_lista_enlazada(l1, l2):
    if len(l1) != len(l2):
        return False
    if not l1 and not l2:
        return True
    if l1[0] != l2[0]:
        return False
    return unificar_lista_enlazada(l1[1:], l2[1:])
print(unificar_lista_enlazada([], []))
print(unificar_lista_enlazada([1, 2, 3], [1, 2, 3]))
print(unificar_lista_enlazada([1, 2, 3], [1, 2, 4])) 
