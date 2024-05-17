"""
66. Write a Python program to calculate the body mass index.
"""

Peso=float(input("Inserte su peso en kilos: "))
Altura=float(input("Inserte su altura en metros: "))

IMC=Peso/Altura**2

print("Su indice de masa corporal es: ",IMC)