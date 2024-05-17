"""
34. Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.
"""

def sumar(a,b,c):
    if a==b or a==c or b==c:
        return 0
    else:
        return a+b+c
    

print(sumar(1,2,5))
print(sumar(5,2,5))