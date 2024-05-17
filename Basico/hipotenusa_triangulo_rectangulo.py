"""
60. Write a Python program to calculate the hypotenuse of a right angled triangle.
"""

import math

def calcular(op,ad):
    return math.sqrt(op**2+ad**2)

#lado opuesto a 90
op=3
#lado adjacente a 90
ad=4

print("La hipotenusa es: ",calcular(op,ad))