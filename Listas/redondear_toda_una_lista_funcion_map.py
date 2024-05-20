"""
83. Write a  Python program to round every number in a given list of numbers and print the total sum multiplied by the length of the list.
Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
Result:
243
"""

import math

lista=[22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

#otra forma de hacerlo
"""
print(sum(list(map(round, lista)) * len(lista))) 
"""

for i in range(len(lista)):
    if abs(lista[i]-int(lista[i]))>=.5:
        if lista[i]<0:
            lista[i]=(-math.ceil(abs(lista[i])))*len(lista)
        else:
            lista[i]=(math.ceil(abs(lista[i])))*len(lista)        
    else:
        if lista[i]<0:
            lista[i]=(-math.floor(abs(lista[i])))*len(lista)
        else:
            lista[i]=(math.floor(abs(lista[i])))*len(lista)

print(sum(lista))