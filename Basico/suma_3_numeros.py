"""
18. Write a Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
"""

def sumar(a,b,c):
    resultado=a+b+c
    if a==b==c:
        return(resultado*3)
    else:
        return(resultado)


print(sumar(1,2,3))

print(sumar(2,2,2))
