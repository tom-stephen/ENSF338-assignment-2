def fib1(n): #(slow verson)
    if n == 1 or n == 0:
        return n
    else:
        return fib1(n-1) + fib1(n-2)

cache = {}
def fib2(n):
    if n == 1 or n == 0: 
        return n           
    else:                   
        if n in cache:      
            return cache[n]
        else:              
            cache[n] = fib2(n-1) + fib2(n-2)   
            return cache[n]

#Time the original code and your improved version, for all integers between 0 and 35, and plot the results
import time
import matplotlib.pyplot as plt
import numpy as np

n_values = range(0, 36)
original_times = []
improved_times = []

for n in n_values:
    start = time.time()
    fib1(n)
    end = time.time()
    original_times.append(end - start)

    start = time.time()
    fib2(n)
    end = time.time()
    improved_times.append(end - start)

import matplotlib.pyplot as plt

plt.plot(n_values, original_times, label='Original')
plt.plot(n_values, improved_times, label='Improved')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.show()
