"""
22. Write a Python program to count the number 4 in a given list.
"""

def contar(lista):
    cantidad=0
    for i in range(len(lista)):
        if lista[i]==4:
            cantidad=cantidad+1
    
    return(cantidad)
    
print(contar([1,2,3,4]))

print(contar([44,4,40,4]))