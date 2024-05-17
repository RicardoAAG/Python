"""
1. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).
"""

ambos=[]

for numero in range(1500,2701):
    if numero%5==0:
        print(numero, "Es multiplo de 5")
        if numero%7==0:
            print(numero, "Es multiplo de ambos")   
            ambos.append(numero)
    if numero%7==0:
        print(numero, "Es multiplo de 7")    
        
print("Numeros que son divisibles entre ambos: ",ambos)