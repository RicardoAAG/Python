"""
25. Write a Python program that checks whether a specified value is contained within a group of values.
"""

def buscar(lista,objetivo):
    if objetivo in lista:
        return("El numero existe dentro de la lista")
    
    return("El numero no existe dentro de la lista")

#Otra manera de hacerlo
    """for i in range(len(lista)):
        if lista[i]==objetivo:
            return("El numero existe dentro de la lista")
    
    return("El numero no existe dentro de la lista")"""
    
print(buscar([1,2,3,4],5))

print(buscar([44,4,40,4],40))