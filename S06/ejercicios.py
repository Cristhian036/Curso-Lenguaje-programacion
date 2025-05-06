#Realizar en Python los puntos realizados en el marco teórico:

print("Ejercicio 01")
conocimientos = {
    "es_perro": ["Fido"],
    "es_gato": ["Tom"],
    "es_raton": ["Jerry"]
}

def es_animal(animal, categoria):
    return animal in conocimientos.get(categoria, [])

print(es_animal("Fido", "es_perro")) 
print(es_animal("Tom", "es_perro"))  
print(es_animal("Jerry", "es_raton"))


print("Ejercicio 02")
parentesco = {
    "padre": {"juan": ["maria", "carlos"]},
    "madre": {"ana": ["maria", "carlos"]}
}
def es_padre(padre, hijo):
    return hijo in parentesco.get("padre", {}).get(padre, [])

def es_madre(madre, hijo):
    return hijo in parentesco.get("madre", {}).get(madre, [])

print(es_padre("juan", "maria"))
print(es_madre("ana", "carlos")) 

print("Ejercicio 03")
def pertenece(elemento, lista):
    return elemento in lista

print(pertenece(3, [1, 2, 3, 4, 5]))


print("Ejercicio 04")
preguntas = {
    "¿Está José en Bilbao?": "No",
    "¿Dónde está Pepe?": "En Madrid",
    "¿Qué hay que hacer para conseguir una casa de protección oficial?": 
    "Presentar documentación y cumplir requisitos."
}

def obtener_respuesta(pregunta):
    return preguntas.get(pregunta, "Respuesta no disponible")

print(obtener_respuesta("¿Está José en Bilbao?")) 
print(obtener_respuesta("¿Dónde está Pepe?"))    
