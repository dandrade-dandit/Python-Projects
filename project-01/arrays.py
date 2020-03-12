import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3])

# printing original array
print("The new created array is : ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")

print("\r")

arr2 = {1, 2, 3}

print('Fim')