"""
22. Write a Python program to count the number 4 in a given list.
"""

numero=int(input("Inserta un numero: "))

residuo=numero/2

if residuo.is_integer():
    print("Su numero es par")
else:
    print("Su numero es impar")