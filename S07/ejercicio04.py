def unificar_pila(p1, p2):
    if len(p1) != len(p2):
        return False
    if not p1 and not p2:
        return True
    if p1[0] != p2[0]:
        return False
    return unificar_pila(p1[1:], p2[1:])
print(unificar_pila([], []))
print(unificar_pila([1, 2, 3], [1, 2, 3]))
print(unificar_pila([1, 2, 3], [1, 2, 4]))