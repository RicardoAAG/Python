# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:01:01 2024

@author: super
"""

numero=0

def calcular(num_a_calcular):
    resultado=num_a_calcular
    for secuencia in range (num_a_calcular,1,-1):
        resultado=resultado*(secuencia-1)
    return resultado
        

print("Calculadora de factoriales, ingrese el numero: ")
numero=int(input())
print("\nEl resultado es: "+str(calcular(numero)))