# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

    # Driver code to test above


# Python program for implementation of MergeSort
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        L = arr[:mid]  # Dividing the array elements
        R = arr[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# To heapify subtree rooted at index i.
# n is size of heap
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l

        # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r

        # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap

        # Heapify the root.
        heapify(arr, n, largest)

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)

    # Function to do insertion sort
def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Code to swap two elements in the list
def swap(arr, frm, to):
    temp = arr[frm]
    arr[frm] = arr[to]
    arr[to] = temp

def bubbleSort(arr):
    for outer in range(len(arr)-1, -1, -1):
        for inner in range(0, outer):
            if arr[inner] > arr[inner+1]:
                swap(arr, inner, inner+1)

def selectionSort(arr):
    for outer in range(0, len(arr)):
        min = outer
        for inner in range (outer+1, len(arr)):
            if arr[inner] < arr[min]:
                min = inner
        swap(arr, outer, min)

# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

# driver code to test the above code
if __name__ == '__main__':
    myArr = [17, 7, 13, 8, 12, 2, 14, 9, 6, 11, 4, 1, 15, 3, 10, 5, 16]

    print ("Given array is", end="\n")
    printList(myArr)

    arr = myArr.copy()
    bubbleSort(arr)
    print("Sorted array using Bubble Sort is: ", end="\n")
    printList(arr)

    arr = myArr.copy()
    selectionSort(arr)
    print("Sorted array using Selection Sort is: ", end="\n")
    printList(arr)

    arr = myArr.copy()
    insertionSort(arr)
    print("Sorted array using Insertion Sort is: ", end="\n")
    printList(arr)

    arr = myArr.copy()
    mergeSort(arr)
    print("Sorted array using Merge Sort is: ", end="\n")
    printList(arr)

    arr = myArr.copy()
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("Sorted array using Quick Sort is: ", end="\n")
    printList(arr)

    arr = myArr.copy()
    heapSort(arr)
    print("Sorted array using Heap Sort is: ", end="\n")
    printList(arr)

