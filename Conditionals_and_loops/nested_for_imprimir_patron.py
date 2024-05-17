"""
4. Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
"""

signo="* "
signos_max=5

#No es un nested for
for a in range(signos_max+1):
    print("")
    print(signo*a,end="")
        
for a in reversed(range(signos_max)):
    print("")
    print(signo*a,end="")
        
#Es nested for
for a in range(signos_max+1):
    print("")
    for b in range(a):
        print(signo,end="")

for a in reversed(range(signos_max)):
    print("")
    for b in range(a):
        print(signo,end="")              