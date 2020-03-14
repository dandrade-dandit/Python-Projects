import math
def BinarySearch(A, key, start, end):
    mid = math.floor((start + end) / 2)
    if A[mid] == key:
        return True
    else:
        if end <= start:
            return False
        else:
            if A[mid] > key:
                return BinarySearch(A, key, start, mid-1)
            else:
                return BinarySearch(A, key, mid+1, end)


# driver code to test the above code
if __name__ == '__main__':
    SampleArr = [4, 5, 7, 9, 13, 16, 14, 15, 19, 2] # must be sorted.
    key = 20
    SampleArr = sorted(SampleArr)
    print("The result for a Binary Search of " + str(key) + " is: " + str(BinarySearch(SampleArr, key, 0, len(SampleArr)-1)));
