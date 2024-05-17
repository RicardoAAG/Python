"""
Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

from math import pi

print("Inserte el valor del radio del circulo del cual se quiere saber su area: ")

radio=float(input())
area=pi*(radio**2)

print("\nArea del circulo: "+str(area))