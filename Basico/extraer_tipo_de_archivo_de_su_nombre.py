"""
7. Write a Python program that accepts a filename from the user and prints the extension of the file.
Sample filename : abc.java
Output : java
"""

print("Escriba el nombre del archivo, para mostrar solo su extension: ")

archivo=input()
archivo_separado=archivo.split(".")
extension=archivo_separado[1]

print("Su archivo es del tipo:",extension)