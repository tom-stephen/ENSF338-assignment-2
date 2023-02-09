##insert sort
def insertionSort(A, size):
    i, key, j = 0, 0, 0
    for i in range(size):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
