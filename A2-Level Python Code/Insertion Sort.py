# Insertion Sort.py
array = [9, 7, 6, 1, 2, 3, 0, 4, 5, 8]

for Pointer in range(len(array)):
    
    ItemToBeInserted = array[Pointer]
    CurrentItem = Pointer - 1 # The second index - to point to the previous element than the first index.
    
    while (array[CurrentItem] > ItemToBeInserted and CurrentItem > -1):
        array[CurrentItem + 1] = array[CurrentItem] # Move the current item further down the list.
        CurrentItem = CurrentItem - 1 # Look at the item above.
    array[CurrentItem + 1] = ItemToBeInserted # Insert item.

print(array)
