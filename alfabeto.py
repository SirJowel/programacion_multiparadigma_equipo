import string

# Crear la lista del alfabeto
listaAlfabeto = list(string.ascii_lowercase)

indices_a_eliminar = []


for indice, letra in enumerate(listaAlfabeto):
    if indice % 3 == 0:
        indices_a_eliminar.append(indice)


for indice in reversed(indices_a_eliminar):
    listaAlfabeto.pop(indice)

print("Lista filtrada:", listaAlfabeto)