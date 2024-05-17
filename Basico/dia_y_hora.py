"""3. Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2014-07-05 14:34:14"""

import datetime

fecha_milisegundos=datetime.datetime.now()
fecha1=fecha_milisegundos.replace(microsecond=0) #haciendo milisegundos 0
print(fecha1)

fecha2=fecha_milisegundos.strftime('%Y-%m-%d %H:%M:%S') #cambiando el formato
print(fecha2)