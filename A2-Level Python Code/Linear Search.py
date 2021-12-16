# Linear Search.py
array = [9, 7, 6, 1, 2, 3, 0, 4, 5, 8]
search_value = 9

for i in range(len(array)):
    if array[i] == search_value:
        print(f"Value found at index {i}")
        break

if array[i] != search_value:
    print(f"Value not found")