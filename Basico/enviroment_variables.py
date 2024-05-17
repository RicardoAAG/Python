"""
53. Write a Python program to access environment variables.
"""

import os


print(os.environ)
print('*----------------------------------*')
path = os.environ["USERPROFILE"]
print(path)
print('*----------------------------------*')
path = os.environ["PATH"]
print(path)
print('*----------------------------------*')
database_url = os.environ.get("DATABASE_URL", "localhost:5432")
print(database_url)
print('*----------------------------------*')