import math

def binaryInsertionSort(arr_temp):
    for i in range(1, len(arr_temp)):
        val = arr_temp[i]
        j = binary_search(arr_temp, val, 0, i - 1)
        arr_temp = arr_temp[:j] + [val] + arr_temp[j:i] + arr_temp[i + 1:]
    return arr_temp


def binary_search(arr, val, start, end):
    # we need to distinugish whether we should insert
    # before or after the left boundary.
    # imagine [0] is the last step of the binary search
    # and we need to decide where to insert -1
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    # this occurs if we are moving beyond left's boundary
    # meaning the left boundary is the least position to
    # find a number greater than val
    if start > end:
        return start

    mid = math.floor((start + end) / 2)
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid


# Code to print the list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


# driver code to test the above code
if __name__ == '__main__':
    myArr = [17, 7, 13, 8, 12, 2, 14, 9, 6, 11, 4, 1, 15, 3, 10, 5, 16]

    arr = myArr.copy()
    arr = binaryInsertionSort(arr)
    print("Sorted array using Binary Insertion Sort is: ", end="\n")
    printList(arr)
