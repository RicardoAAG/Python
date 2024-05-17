"""
32. Write a Python program to find the least common multiple (LCM) of two positive integers.
"""

import numpy

def factores_primos(numero,factores):
    i=1
    
    while(numero!=1):
        i=i+1
        while float(numero/i).is_integer():
            numero=numero/i
            factores.append(i)
                
def extraer(factores_1,factores_2):
    factor_a_buscar=1
    mayor_1=[]
    mayor_2=[]
    mayor_ambos=[]
    if factores_1[-1]>=factores_2[-1]:
        stop=factores_1[-1]
    else:
        stop=factores_2[-1]
    
    for factor_a_buscar in range(1,stop):
        factor_a_buscar=factor_a_buscar+1
        mayor_1=[]
        mayor_2=[]
        
        if (factor_a_buscar not in factores_1 and factor_a_buscar not in factores_2)==False:
            for factor in factores_1:
                if factor_a_buscar==factor:
                    mayor_1.append(factor)
            for factor in factores_2:
                if factor_a_buscar==factor:
                    mayor_2.append(factor)
            if len(mayor_1)>=len(mayor_2):
                mayor_ambos.extend(mayor_1)
            else:
                mayor_ambos.extend(mayor_2)
            
    return(mayor_ambos)
            
    
numero_1=135
numero_2=66
factores_primos_1=[]
factores_primos_2=[]
factores_mayores=[]
mcm=1

i=1

factores_primos(numero_1,factores_primos_1)
factores_primos(numero_2,factores_primos_2)

factores_mayores=extraer(factores_primos_1,factores_primos_2)

print("El minimo comun multiplo es:",numpy.prod(factores_mayores))


#mejor forma de hacerlo

for i in range(1,numero_1*numero_2+1):
    if i%numero_1 == 0 and i%numero_2 == 0 :
        break
print("lcm of two numbers:",i)

