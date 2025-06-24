N = int(input("Ingrese un número entero positivo: "))
if N <= 0:
    print("Por favor, ingrese un número positivo.")
else:
    fibo = [0, 1] 
    for i in range(2, N):
        fibo.append(fibo[-1] + fibo[-2])
    print("Serie de Fibonacci:", fibo[:N])
    suma_fibo = sum(fibo[:N])
    print("La suma de los primeros N números es:", suma_fibo)

print("\n--- Triángulo de asteriscos ---")

N = int(input("Ingrese un número: "))
if N <= 0:
    print("Por favor, ingrese un número positivo.")
else:
    for i in range(1, N+1):
        print('*' * (2*i - 1))
