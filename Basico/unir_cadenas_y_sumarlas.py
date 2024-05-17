"""
10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615
"""

numero=input("Inserte un numero para realizarle la siguiente operacion n+nn+nnn: ")

numero_doble=int(numero+numero)
numero_triple=int(numero+numero+numero)

resultado=int(numero)+numero_doble+numero_triple

print("Expected Result :",resultado)