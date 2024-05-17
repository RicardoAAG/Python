"""
58. Write a Python program to sum the first n positive integers.
"""

def sumar(cantidad):
    total=0
    for i in range(0,cantidad+1):
        total=total+i
    return total
        
cantidad=int(input("Inserte la cantidad de enteros que desea sumar: "))

print("La suma de los primeros ",cantidad," es: ", sumar(cantidad))