#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

def fib(n):  # print Fibonacci series
    """Print a Fibonacci series up to n."""
    t1, t2 = 0, 1
    while t2 < n:
        print(t2, end=' ')
        t1, t2 = t2, t1 + t2
    print()
    
fib(10000)

## END
