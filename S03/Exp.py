def sumar(x): return x + 1
def restar(x): return x - 1
def multiplicar(x): return x * 2

funciones = [sumar, restar, multiplicar]

for f in funciones:
    print(f(5))


def saludar (nombre , saludar):
    mensaje = f"{saludar}, {nombre}!"
    return mensaje

resultado = saludar (nombre='juan', saludar= 'hola')

print(resultado)

def suma (num):
    total = 0
    for n in num:
        total += n
    return total
print(suma ([1,3,5,4]))

