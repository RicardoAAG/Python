"""
55. Write a Python program to find local IP addresses using Python's stdlib.
"""

import os
import socket

print(os.system('ipconfig'))

IP = socket.gethostbyname(socket.gethostname())
print("Your Computer IP Address is:" + IP)