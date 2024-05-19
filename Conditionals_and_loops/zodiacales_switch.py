"""
38. Write a  Python program to display the astrological sign for a given date of birth.
Expected Output:

Input birthday: 15                                                      
Input month of birth (e.g. march, july etc): may                        
Your Astrological sign is : Taurus 
"""

dia=int(input("Ingresa el dia de tu nacimiento: "))
mes=input("Ingresa el mes de tu nacimiento: ")
signo=""


if mes=="enero":
    signo = 'Capricornio' if (dia < 20) else 'Acuario'    
elif mes=="febrero":
    signo = 'Acuario' if (dia < 19) else 'Piscis'        
elif mes=="marzo":
    signo = 'Piscis' if (dia < 21) else 'Aries'        
elif mes=="abril":
    signo = 'Aries' if (dia < 20) else 'Tauro'        
elif mes=="mayo":
    signo = 'Tauro' if (dia < 21) else 'Geminis'        
elif mes=="junio":
    signo = 'Geminis' if (dia < 21) else 'Cancer'        
elif mes=="julio":
    signo = 'Cancer' if (dia < 23) else 'Leo'        
elif mes=="agosto":
    signo = 'Leo' if (dia < 23) else 'Virgo'     
elif mes=="septiembre":
    signo = 'Virgo' if (dia < 23) else 'Libra'     
elif mes=="octubre":
    signo = 'Libra' if (dia < 23) else 'Escorpio'     
elif mes=="noviembre":
    signo = 'Escorpio' if (dia < 22) else 'Sagitario'     
elif mes=="diciembre":
    signo = 'Sagitario' if (dia < 22) else 'Capricornio'  
    
print("Tu signo zodiacal es: ",signo)