def orde_sup(fun):
    fun()
    
def greeting():
    print('hello world')

orde_sup(greeting)

print("fun orden superior")
def operation(x, fun):
    return fun(x)
def sqrt(x):
    return x**0.5
def squared(x):
    return x**2
resultado_1= operation(16, sqrt)
print(resultado_1)
resultado_2= operation(16,squared)
print(resultado_2)

print("\nfun orden filter")
integer=[1,2,3,4,5,6,7,8,9,10,11,12]
even = list(filter(lambda x: x%2 == 0,integer))
print(even)

print("\nfun orden map")
integer=[1,2,3,4,5,6,7,8,9,10,11,12]
cubed = list(map(lambda x: x**3,integer))
print(cubed)

print("\nfun orden reduce")
from functools import reduce
integer=[1,2,3,4,5,6,7,8,9,10,11,12]
sumcub = reduce(lambda a,b: a+b ,integer)
print(sumcub)
