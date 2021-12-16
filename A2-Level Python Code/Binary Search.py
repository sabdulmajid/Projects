# Binary Search.py
array = [9, 7, 6, 1, 2, 3, 0, 4, 5, 8]
search_value = 5
found = False
searchFailed = False
First = 0
Last = len(array)

while found != True and searchFailed != True:
    Middle = (First + Last) // 2
    if array[Middle] == search_value:
        found = True
    elif First >= Last:
        searchFailed = True
    elif array[Middle] > search_value:
        Last = Middle - 1
    else: 
        First = Middle + 1

if found == True:
    print(f"Value found at index {Middle}")
else:
    print(f"Value not found")
