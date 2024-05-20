"""
195. Write a  Python program to traverse a given list in reverse order, and print the elements with the original index.
Original list:
['red', 'green', 'white', 'black']
Traverse the said list in reverse order:
black
white
green
red
Traverse the said list in reverse order with original index:
3 black
2 white
1 green
0 red
"""

lista=['red','green','white','black']

print("Lista original: \n",lista)

print("\nLista impresa al reves sin index:")
for reverso in range(len(lista)-1,-1,-1):
    print(lista[reverso])


print("\nLista impresa al reves con index:")
for reverso in range(len(lista)-1,-1,-1):
    print(reverso,lista[reverso])