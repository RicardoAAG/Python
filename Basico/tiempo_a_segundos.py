"""
62. Write a Python program to convert all units of time into seconds.
"""

dias=int(input("Inserte una cantidad de dias: "))
horas=int(input("Inserte una cantidad de horas: "))
minutos=int(input("Inserte una cantidad de minutos: "))
segundos=int(input("Inserte una cantidad de segundos: "))
total=0

total=total+dias*86400+horas*3600+minutos*60+segundos


print("El total de segundos es: ",total)