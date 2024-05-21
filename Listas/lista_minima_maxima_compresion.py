"""
182. Write a Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.
Original list:
[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
Maximum sum of sub list of the said list of lists:
[2, 3, 5, 4]
Minimum sum of sub list of the said list of lists:
[1, 2, 1, 2]
"""

lista=[[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
sumas=[sum(i) for i in lista]

print("Lista original: \n",lista)
print("Lista con la suma maxima: \n",lista[sumas.index(max(sumas))])
print("Lista con la suma minima: \n",lista[sumas.index(min(sumas))])