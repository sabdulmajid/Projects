# Bubble Sort.py
array = [9, 7, 6, 1, 2, 3, 0, 4, 5, 8]

for i in range(len(array)):
    for j in range(len(array) - 1):
        if array[j] > array[j + 1]:
            temporary = array[j]
            array[j] = array[j + 1]
            array[j + 1] = temporary
    
print(array)

