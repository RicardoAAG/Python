"""
23. Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
"""

def imprimir(info,n):
    if len(info)<2:
        return(info*n)
    else:
        return(info[0:2]*n)
    

info=str(input("Escribe algo, las primeras dos letras van a ser repetidas N veces: "))
n=int(input("Cuantas veces deseas copiar el texto?: "))

print(imprimir(info,n))