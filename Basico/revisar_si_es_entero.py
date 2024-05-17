"""
36. Write a Python program to add two objects if both objects are integers.
"""

def unir(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return "Son enteros"
    else:
        return "No son enteros"
 

print(unir(1,2))
print(unir(1.8,2))   
print(unir(1,'2'))          