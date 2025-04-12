def sumar(x): return x + 1
def restar(x): return x - 1
def multiplicar(x): return x * 2

funciones = [sumar, restar, multiplicar]

for f in funciones:
    print(f(5))
