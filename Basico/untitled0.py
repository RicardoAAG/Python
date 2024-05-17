"""
33. Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.
"""

def sumar(a,b,c):
    if a==b or a==c or b==c:
        return 0
    else:
        return a+b+c
    

print(sumar(1,2,5))
print(sumar(5,2,5))