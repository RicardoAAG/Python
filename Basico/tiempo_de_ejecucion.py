"""
57. Write a Python program to get the execution time of a Python method.
"""

import timeit

medir="""
a=100
b=50
resultado=1   

for i in range(0,a):
    resultado=resultado*b
    
print(resultado)
"""

tiempo_de_ejecucion=timeit.timeit(medir,number=2)
print("Tiempo de ejecucion: ",tiempo_de_ejecucion)