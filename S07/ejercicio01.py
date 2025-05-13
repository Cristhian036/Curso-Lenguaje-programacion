def unificar_constantes(a, b):return a == b

def unificar_variables(X, valor):return valor
def unificar_estructuras(f1, f2):
    if f1[0] != f2[0]:
        return False
    return {f1[1][i]: f2[1][i] for i in range(len(f1[1]))}
def unificar_listas(l1, l2):
    if len(l1) != len(l2):
        return False
    return {l1[0]: l2[0], 'Y': l2[1:]}
def unificar_terminos_complejos(t1, t2):
    if t1[0] != t2[0]:
        return False
    return {t1[1][i]: t2[1][i] for i in range(len(t1[1]))}
def unificar_patrones(f1, f2):
    if f1[0] != f2[0]:
        return False
    if f1[1][0] != f1[1][1]:
        return False
    return f1[1][0] == f2[1][0] and f1[1][1] == f2[1][1]
print(unificar_constantes('a', 'a')) 
print(unificar_constantes('a', 'b'))  
X = unificar_variables('X', 5)
print(X)
estructura1 = ('f', ('a', 'b'))
estructura2 = ('f', ('X', 'Y'))
print(unificar_estructuras(estructura1, estructura2)) 
lista1 = ['X', 'Y']
lista2 = [1, 2, 3]
print(unificar_listas(lista1, lista2)) 
termino1 = ('persona', ('Nombre', 'Edad'))
termino2 = ('persona', ('juan', 25))
print(unificar_terminos_complejos(termino1, termino2)) 
patron1 = ('f', ('X', 'X'))
patron2 = ('f', ('a', 'b'))
print(unificar_patrones(patron1, patron2)) 
