"""
26. Write a Python program to create a histogram from a given list of integers.
"""

def histograma(lista):
    for i in lista:
        print(i,"ඞ"*i)
    return("Histograma\n")
    
print(histograma([6,2,9,0]))

print(histograma([1,2,3,4]))