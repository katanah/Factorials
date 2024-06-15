from math import floor
from timeit import default_timer as dt

def timer(func, x):
    start = dt()
    func(x)
    end = dt()
    return end-start

# slightly less efficient 
def find_constant1(n):
    numerator = 1.0
    denominator = 1.0
    middle = 1.       # this is the middle number of the nth row of pascal triangle
    
    for i in range(1, n+1):
        if i % 2 == 0:
            middle *= 2
        else:
            middle *= numerator/denominator
            numerator += 2
            denominator += 1
    
    return middle

#currently best method
def find_constant(n):
    numerator = 1.
    denominator = 1.
    end = n - floor(n/2)
    middle = 2**(n-end)

    for i in range(1, end+1):
        middle *= numerator / denominator
        numerator += 2
        denominator += 1

    return int(middle)   


"""
The following formula is being implemented 

if n is odd then n! = c *  ((n-1)/2)! * ((n+1)/2)!
"""

def two_pointer_factorial(n):
    if n < 2:
        return n
     
    if n % 2 == 0:
        if n == 2:
            return n
        
        # Inits variables
        last =  n//2 * (n//2+1)
        prev = n
        ans = prev * last
        incr = 2
        
        #first iteration
        last -= incr
        n -= 2
        prev += n
        incr += 2
        
        while last > prev:
            ans *= prev * last
            last -= incr
            n -= 2
            prev += n
            incr += 2
            
        return ans if last != prev else ans * last

    else:
        return n*two_pointer_factorial(n-1)

def factorial(n):
    if n % 2 == 0:
        return n * factorial(n-1)
    else:
        a = two_pointer_factorial((n-1)//2)
        b = (n+1)//2 * a
        c = find_constant(n)
        
        return a*b*c
    

x = 1000

print(f'Decomposition > {timer(factorial, x)}')
print(f'Two Pointers  > {timer(two_pointer_factorial, x)}')