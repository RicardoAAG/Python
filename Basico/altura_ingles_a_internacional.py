"""
59. Write a Python program to convert height (in feet and inches) to centimeters.
"""

altura_convertida=[0,0]
altura_original=str(input("Inserte su altura en pies para convertirla a centimetros: "))

altura_separada=altura_original.split(".")

altura_convertida[0]=int(altura_separada[0])*30.48
try:
    altura_convertida[1]=int(altura_separada[1])*2.54
except IndexError:
    pass

print("Altura en centimetros: ",sum(altura_convertida),"cm")