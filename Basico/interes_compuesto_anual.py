"""
39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years.
Test Data : amt = 10000, int = 3.5, years = 7
Expected Output : 12722.79
"""

cantidad = 10000
interes = 3.5
tiempo = 7

for i in range(1,tiempo+1):
    cantidad=cantidad+cantidad*(interes/100)
    
print(cantidad)