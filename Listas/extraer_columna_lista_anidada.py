"""
108. Write a  Python program to extract a specified column from a given nested list.
Original Nested list:
[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
Extract 1st column:
[1, 2, 1]
Original Nested list:
[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
Extract 3rd column:
[3, -5, 1]
"""

lista=[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
columna=1
lista_separada=[]

print("Lista anidada completa:\n",lista)

for i in range(len(lista)):
    lista_separada.append(lista[i][columna-1])
    
print("Columna numero",columna,"extraida\n",lista_separada)