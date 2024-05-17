"""
24. Write a Python program to test whether a passed letter is a vowel or not.
"""

def revisar(letra):
    vocales="aeiou"
    letra=letra.lower()
    if letra in vocales:
        return("Es vocal")
    else:
        return("Es consonante")
    
print(revisar("z"))