"""
35. Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.
"""

def revisar(a,b):
    if a==b or a+b==5 or abs(a-b)==5:
        return True
    else:
        return False

print(revisar(1,2))
print(revisar(2,2))
print(revisar(3,2))
print(revisar(7,2))