print("#funcion generica")
def sum_numbers(v1 : int, v2 : int) -> int:
    return v1 + v2
def concat_strs(v1 : str, v2 : str) -> str:
    return v1 + v2

numbers = sum_numbers(10,20)
strs = concat_strs("app","le")
print(numbers)
print(strs)

print("\n#funcion generica definir typing")
import typing as t
T= t.TypeVar("T") 

def sum(v1 : int, v2 : int) -> int:
    return v1 + v2
numbers = sum(10,20)
srts = sum("app","le")
print(numbers)
print(srts)
