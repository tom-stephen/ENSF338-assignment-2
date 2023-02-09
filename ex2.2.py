import sys
sys.setrecursionlimit(20000)

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


#test the above sorting method with testdata.json
import json
import time
import matplotlib.pyplot as plt

with open('ex2.json') as f:
    data = json.load(f)

n_values = []
times = []

for n in data:
    n_values.append(len(n))
    start = time.time()
    func1(n, 0, len(n)-1)
    end = time.time()
    times.append(end - start)



########################################
## testing new data set ex2.5.json
with open('ex2.5.json') as f:
    data = json.load(f)

r_values = []
r_times = []

for n in data:
    r_values.append(len(n))
    start = time.time()
    func1(n, 0, len(n)-1)
    end = time.time()
    r_times.append(end - start)

#########################################


#print times
print(times)
print(r_times)
plt.plot(n_values, times, label='original')
plt.plot(r_values, r_times, label='improved')
plt.legend()
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.show()

