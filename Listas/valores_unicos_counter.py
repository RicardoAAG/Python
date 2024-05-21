"""
224. Write a Python program to create a list with unique values filtered out.
Sample Output:
[2, 4]
"""

lista=[1, 2, 2, 2, 3, 4, 4, 5]
cache=[1, 2, 2, 2, 3, 4, 4, 5]
revisar=0
nueva=[]

for revisar in lista:
    cache.remove(revisar)
    if revisar in cache:
        if revisar not in nueva:
            nueva.append(revisar)
            
            
#otra manera de hacerlo
"""
# Import the 'Counter' class from the 'collections' module.
from collections import Counter

# Define a function called 'filter_unique' that takes a list 'lst' as an argument.
def filter_unique(lst):
  # Create a list of items and their corresponding counts using the 'Counter' class.
  # Filter this list to include only items with a count greater than 1.
  return [item for item, count in Counter(lst).items() if count > 1]

# Example: Filter out unique elements from a list.
print(filter_unique([1, 2, 2, 3, 4, 4, 5]))
"""