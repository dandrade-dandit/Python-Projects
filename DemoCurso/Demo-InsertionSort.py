
def insertionSort (arr):

    for  i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# driver code to test the above code
if __name__ == '__main__':
    myArr = [17, 7, 13, 8, 12, 2, 14, 9, 6, 11, 4, 1, 15, 3, 10, 5, 16]

    arr = myArr.copy()
    insertionSort(arr)
    print("Sorted array using Insertion Sort is: ", end="\n")
    printList(arr)

