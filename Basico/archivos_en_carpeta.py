"""
49. Write a Python program to list all files in a directory.
"""

import os

#blanco es la carpeta, pero se puede agregar el path de una carpeta especifica
archivos=os.listdir()

for i in archivos:
    print(i)