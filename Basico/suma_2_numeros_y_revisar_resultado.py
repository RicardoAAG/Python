"""
34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

def sumar(a,b):
    resultado=a+b
    #if resultado in range(15,20)
    if 15<=resultado<=20:
        return 20
    else:
        return resultado
    

print(sumar(1,2))
print(sumar(10,5))
print(sumar(8,9))
print(sumar(10,15))