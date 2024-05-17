"""
42. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
"""

n=[]
numero=1

while numero!=0:
    numero=int(input("Inserte enteros para encontrar su suma y promedio: "))
    if numero!=0:
        n.append(numero)

#Usando For
"""
suma=0
for i in n:
    suma=suma+i
print(suma)
"""

print(sum(n))
print(sum(n)/len(n))