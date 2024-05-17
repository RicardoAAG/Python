"""
31. Write a Python program that computes the greatest common divisor (GCD) of two positive integers.
"""

def dividir(primos,numero,divisores):
    for x in primos:
        if numero!=1:
            while float(numero/x).is_integer():
                numero=numero/x
                divisores.append(x)
                
def encontrar_MCD(divisores_1,divisores_2,divisores_comun):
    for i in divisores_1:
        if i in divisores_2:
            divisores_comun.append(i)
            divisores_2.remove(i)

numero_1=336
numero_2=360
divisores_1=[]
divisores_2=[]
divisores_comun=[]
MCD=1
primos=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97)

dividir(primos,numero_1,divisores_1)
dividir(primos,numero_2,divisores_2)
    
encontrar_MCD(divisores_1,divisores_2,divisores_comun)

for i in divisores_comun:
    MCD=MCD*i
    
print("El Maximo Comun Divisor de",numero_1,"y",numero_2,"es",MCD)

#otra forma de hacerlo
"""
# Define a function to calculate the greatest common divisor (GCD) of two numbers.
def gcd(x, y):
    # Initialize z as the remainder of x divided by y.
    z = x % y
    
    # Use a while loop to find the GCD.
    while z:
        # Update x to y, y to z, and calculate a new value for z (remainder of x divided by y).
        x = y
        y = z
        z = x % y
    
    # When z becomes 0, y contains the GCD, so return y.
    return y

# Print the GCD of specific pairs of numbers.
print("GCD of 12 & 17 =", gcd(12, 17))
print("GCD of 4 & 6 =", gcd(4, 6))
print("GCD of 336 & 360 =", gcd(336, 360))
"""