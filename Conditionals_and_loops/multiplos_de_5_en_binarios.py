"""
13. Write a Python program that accepts a sequence of comma separated 4 digit binary numbers as its input. 
The program will print the numbers that are divisible by 5 in a comma separated sequence.
Sample Data : 0100,0011,1010,1001,1100,1001
Expected Output : 1010
"""

def divisibles():
    for posicion in range(0,len(binarios_convertidos)):
        if binarios_convertidos[posicion]%5==0:
            print(binarios_separado[posicion])

def convertir():
    
    for lugar,binario in zip(range(0,len(binarios_separado)),binarios_separado):
        binarios_convertidos.append(0)
        for posicion,valor in enumerate(reversed(binario)):
            binarios_convertidos[lugar]=binarios_convertidos[lugar]+(int(valor)*2**posicion) 
    

binarios_separado=[]
binarios_convertidos=[]

binarios=input("Inserta valores en binario de 4 digitos, separados por comas: ")

binarios_separado=binarios.split(",")
convertir()
divisibles()


#Usando int(binario, 2) para convertir binario a decimal 
"""
def binarios_divisibles_por_5(binarios):
    binarios_separado = binarios.split(",")
    resultado = []

    for binario in binarios_separado:
        numero_decimal = int(binario, 2)
        if numero_decimal % 5 == 0:
            resultado.append(binario)

    return ",".join(resultado)

binarios = input("Inserta valores en binario de 4 dígitos, separados por comas: ")
resultado = binarios_divisibles_por_5(binarios)
print(resultado)
"""