"""
29. Write a Python program that prints out all colors from color_list_1 that are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

color_list_3 = set([])

for x in color_list_1:
    if x not in color_list_2:
        color_list_3.add(x)
        
#Otro metodo de hacerlo
"""color_list_3=color_list_1.difference(color_list_2)"""
        
print(color_list_3)