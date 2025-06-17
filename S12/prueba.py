#Enunciado 3: Un pangrama es una frase que contiene todas las letras del abecedario al menos una vez. Escribe un programa que determine si una frase es un pangrama

#Un pangrama también conocido como frase holoalfabética, es un texto breve que contiene todas las letras del alfabeto de un idioma
print("\nEnunciado 3")
frase = input("Introduce una frase para verificar si es un pangrama: ")
abecedario = set("abcdefghijklmnopqrstuvwxyz")
frase_letras = set(frase.lower())
if abecedario.issubset(frase_letras):
    print("La frase es un pangrama.")
else:
    print("La frase NO es un pangrama.")