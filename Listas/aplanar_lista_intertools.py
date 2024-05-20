"""
Write a  Python program to flatten a shallow list.
"""

lista=[[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lista_junta=[]

for i in range(len(lista)):
    for x in lista[i]:
        lista_junta.append(x)
        
print(lista_junta)


#otra manera de hacerlo con itertools
"""
import itertools

# Lista original
lista_anidada = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Aplanar la lista usando itertools.chain
lista_planada = list(itertools.chain(*lista_anidada))

print(lista_planada)
"""