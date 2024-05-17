"""
12. Write a Python program that prints the calendar for a given month and year.
Note : Use 'calendar' module.
"""

import calendar

m=int(input("Inserte el mes que desea conocer (numero): "))
a=int(input("Inserte el año de ese mes: "))
        
print("\n",calendar.month(a,m))