"""
91. Write a  Python program to find a list with maximum and minimum lengths.
Original list:
[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
List with maximum length of lists:
(3, [13, 15, 17])
List with minimum length of lists:
(1, [0])

Original list:
[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(3, [3, 5, 7])
List with minimum length of lists:
(1, [0])

Original list:
[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
List with maximum length of lists:
(4, [1, 34, 5, 7])
List with minimum length of lists:
(1, [12])
"""

lista=[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]

longitudes=[]

for i in lista:
    longitudes.append(len(i))
    
print("Lista original: \n",lista)
print("Lista de menor tamaño: \n",lista[longitudes.index(min(longitudes))])
print("Lista de mayor tamaño: \n",lista[longitudes.index(max(longitudes))])