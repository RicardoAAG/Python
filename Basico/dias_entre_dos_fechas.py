"""
14. Write a Python program to calculate the number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
"""

import datetime

print("Inserte la primera fecha en el siguiente formato (aa,mm,dd): ")
primera_fecha=input().split(",")

print("\nInserte la segunda fecha en el siguiente formato (aa,mm,dd): ")
segunda_fecha=input().split(",")

fecha1=datetime.date(int(primera_fecha[0]),int(primera_fecha[1]),int(primera_fecha[2]))
fecha2=datetime.date(int(segunda_fecha[0]),int(segunda_fecha[1]),int(segunda_fecha[2]))
fecha3=fecha1-fecha2

print("\nLa diferencia entre estas fechas es de", abs(int(fecha3.days)) ,"dias")