"""
17. Write a Python program to test whether a number is within 100 of 1000 or 2000.
"""

numero=5000
control=0

diferencia=abs(numero-1000)

if diferencia <= 100:
    print("Esta a ",diferencia," de 1000")
else:
    control=control+1
    
diferencia=abs(numero-2000)
    
if diferencia <= 100:
    print("Esta a ",diferencia," de 2000")
else:
    control=control+1
    
if control==2:
    print("No esta dentro del rango especifico")