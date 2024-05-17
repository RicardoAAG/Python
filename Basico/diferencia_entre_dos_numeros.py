"""
16. Write a Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
"""

def calcular(numero,diferencia):
    if numero > 17:
        return(diferencia*2)
    else:
        return(diferencia)

print("Inserta un numero: ")
numero=int(input())

diferencia=abs(17-numero)

print(calcular(numero,diferencia))