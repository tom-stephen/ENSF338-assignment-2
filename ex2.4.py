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


## faster quick sort
import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    middle = [x for x in arr if x == pivot]
    return quick_sort(low) + middle + quick_sort(high)


## bonous insert sort
def insertionSort(A, size):
    i, key, j = 0, 0, 0
    for i in range(size):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key


import json
import time
import matplotlib.pyplot as plt
import numpy as np

### test the QUICKSORT method with testdata.json
with open('testdata.json') as f:
    data = json.load(f)

n_values_1 = []
quick_sort_times = []

for n in data:
    n_values_1.append(len(n))
    start = time.time()
    quick_sort(n)
    end = time.time()
    quick_sort_times.append(end - start)

### test the ORIGINAL SORT method with testdata.json
n_values_2 = []
original_sort_times = []

with open('testdata.json') as f:
    data_2 = json.load(f)

for n in data_2:
    n_values_2.append(len(n))
    start = time.time()
    func1(n, 0, len(n)-1)
    end = time.time()
    original_sort_times.append(end - start)

#print times
print(quick_sort_times)
print(original_sort_times)
plt.plot(n_values_2, original_sort_times, label='original')
plt.plot(n_values_1, quick_sort_times, label='quick sort')
plt.legend()
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.show()

