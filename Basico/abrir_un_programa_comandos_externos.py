"""
45. Write a Python program that calls an external command.
"""

#https://blog.finxter.com/how-to-call-an-external-command-in-python/#:~:text=In%20Python%203.5%20and%20above,process%20returns%20an%20error%20code.
 
import os
import subprocess

#abrir un archivo,programa
subprocess.Popen("C:/Users/super/AppData/Local/Discord/Update.exe --processStart Discord.exe")


# Traverse the ipconfig information 
data = subprocess.run(['ipconfig'])

print(data)