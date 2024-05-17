# -*- coding: utf-8 -*-
"""
19. Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
"""

def buscar(info,separado):
    if info[0:2]=="Is":
        return info
    else:
        return "Is"+info
    

print("Escribe lo que sea: ")
info=input()
separado=info.split(" ")

print(buscar(info,separado))