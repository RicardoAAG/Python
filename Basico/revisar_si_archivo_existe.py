"""
41. Write a Python program to check whether a file exists.
"""

import os

def revisar(path):
    if os.path.isfile(path):
        return "Existe ese archivo"
    else:
        return "No existe"


path='C:/Users/super/Desktop/random/revisar_si_archivo_existe.py'
path_falso='C:/Users/super/Desktop/random/revisar_si_archivo_existe_2.py'

print(revisar(path))
print(revisar(path_falso))