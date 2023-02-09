import cProfile

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


