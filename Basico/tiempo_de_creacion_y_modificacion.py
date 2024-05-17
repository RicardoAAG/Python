"""
64. Write a Python program that retrieves the date and time of file creation and modification.
"""

import os
import time

creacion=os.path.getctime('err.txt')
modificacion=os.path.getmtime('err.txt')

creacion_normal=time.ctime(creacion)
modificacion_normal=time.ctime(modificacion)

print("Creacion: ",creacion_normal)
print("Ultima modificacion: ",modificacion_normal)