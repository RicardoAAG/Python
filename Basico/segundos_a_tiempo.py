"""
65. Write a Python program that converts seconds into days, hours, minutes, and seconds.
"""

segundos=int(input("Inserte una cantidad de segundos: "))
completo=[0,0,0,0]
conversion=[86400,3600,60,1]

for i in range(0,len(conversion)):
    completo[i]=int(segundos/conversion[i])
    segundos%=conversion[i]*completo[i]

print("Equivale a {} dias, {} minutos, {} horas y {} segundos".format(completo[0],completo[1],completo[2],completo[3]))