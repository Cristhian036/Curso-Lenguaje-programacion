class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
    def isEmptyList(self):
        return self.cabeza is None
    def length(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    def destroyList(self):
        self.cabeza = None
    def search(self, x):
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.valor == x:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    def insertFirst(self, x):
        nuevo_nodo = Nodo(x)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    def insertLast(self, x):
        nuevo_nodo = Nodo(x)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    def removeNode(self, x):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.valor == x:
                if anterior is None: 
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False 
    def imprimirLista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("Vacio" if self.isEmptyList() else "Fin de la lista")
lista = ListaEnlazada()
lista.insertFirst(10)
lista.insertLast(20)
lista.insertLast(30)
lista.insertFirst(5)
print("Lista enlazada:")
lista.imprimirLista()
print("Longitud de la lista:", lista.length())
print("¿Está vacía la lista?", lista.isEmptyList())
print("Buscar 20 en la lista:", lista.search(20))
print("Eliminar el nodo con valor 10:", lista.removeNode(10))
lista.imprimirLista()
print("Eliminar todos los nodos.")
lista.destroyList()
lista.imprimirLista()
