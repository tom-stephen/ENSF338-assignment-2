import sys
sys.setrecursionlimit(20000)

#original quick sort
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)
def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
        array[start], array[high] = array[high], array[start]
    return high

import random
# quick sort using a random number as the pivot
def quickSort(A, size):
    if size <= 1:
        return A
    else:
        pivot = random.randint(0, size)
        A[0], A[pivot] = A[pivot], A[0]
        i, key, j = 0, 0, 0
        for i in range(size):
            key = A[i]
            j = i-1
            while j >= 0 and A[j] > key:
                A[j + 1] = A[j]
                j = j - 1
            A[j + 1] = key
    # return A

import json
import time
import matplotlib.pyplot as plt


###################################################################
### test the QUICKSORT method with testdata.json
with open('ex2.json','r') as f:
    data = json.load(f)

n_values_1 = []
quick_sort_times = []
# new_data = []

for n in data:
    n_values_1.append(len(n))
    start = time.time()
    # new = quickSort(n,len(n)-1)
    quickSort(n,len(n)-1)
    end = time.time()
    quick_sort_times.append(end - start)
    # new_data.append(new)

#dump new data to json file
# with open('test_dump.json', 'w') as f:
#     json.dump(new_data, f)


###################################################################
### test the ORIGINAL SORT method with testdata.json
n_values_2 = []
original_sort_times = []

with open('ex2.json','r') as f:
    data_2 = json.load(f)

for n in data_2:
    n_values_2.append(len(n))
    start = time.time()
    func1(n, 0, len(n)-1)
    end = time.time()
    original_sort_times.append(end - start)


###################################################################
#print times
print(quick_sort_times)
print(original_sort_times)
plt.plot(n_values_1, quick_sort_times, label='quick sort')
plt.plot(n_values_2, original_sort_times, label='original')
plt.legend()
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.show()

