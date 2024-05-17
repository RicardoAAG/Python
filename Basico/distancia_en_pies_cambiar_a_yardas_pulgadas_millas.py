"""
61. Write a Python program to convert the distance (in feet) to inches, yards, and miles.
"""

distancia=str(input("Inserte una distancia en pies para convertirla a pulgadas, yardas y millas: "))

ajustar=distancia.split(".")

distancia=float(ajustar[0])
try:
    distancia=distancia+(float(ajustar[1])/12)
except IndexError:
    pass

distancia_pulgadas=distancia*12
print("Distancia en pulgadas: ",distancia_pulgadas)

distancia_yardas=distancia/3
print("Distancia en yardas: ",distancia_yardas)

distancia_millas=distancia/5280
print("Distancia en millas: ",distancia_millas)