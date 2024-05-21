"""
254. Write a Python program to get the weighted average of two or more numbers.
Sample Output:
Original list elements:
[10, 50, 40]
[2, 5, 3]
Weighted average of the said two list of numbers:
39.0
Original list elements:
[82, 90, 76, 83]
[0.2, 0.35, 0.45, 32]
Weighted average of the said two list of numbers:
82.97272727272727
"""

valores=[82, 90, 76, 83]
peso=[0.2, 0.35, 0.45, 32]
numero_x_peso=0
    
for v,p in zip(valores,peso):
    numero_x_peso=numero_x_peso+v*p

#otra manera de hacerlo
"""
numero_x_peso=sum(x * y for x, y in zip(valores, peso))
"""
    
print("listas originales:\n",valores,"\n",peso)
print("Peso promedio de ambas listas: \n",numero_x_peso/sum(peso))