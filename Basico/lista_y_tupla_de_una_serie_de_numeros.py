"""
6. Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

lista=[]

print("Inserte una serie de numeros separados por espacios, de esta serie se creara una lista y una tupla")
numeros_lista=input()
#numeros_sin_espacios=numeros_lista.replace(" ", "") #para quitar los espacios de la lista, pero el problema no lo pide
numeros_separados=numeros_lista.split(",")

lista=numeros_separados
tupla=tuple(numeros_separados)

#tupla=tuple(lista) otra forma de hacerlo

print("List: ", lista) #Tuple items are ordered, unchangeable, and allow duplicate values.
print("Tuple: ", tupla) #A tuple is a collection which is ordered and unchangeable.