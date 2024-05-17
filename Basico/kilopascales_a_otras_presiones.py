"""
67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure
"""

kilopascales=float(input("Inserta la cantidad de presion en kilopascales: "))

psi=kilopascales/6.895
mmhg=kilopascales*7.501
atm=kilopascales/101.3

print("Esa cantidad de kilopascales equivale a {} PSI, {} mmHg y {} atmosferas".format(psi,mmhg,atm))