#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
 
################################################################################ 
## Summary: simple Python program demonstrating break and continue statement,
## and else clause on loops.
##
################################################################################ 


for n in range(2, 10):    # outer for loop
    # P1
    for x in range(2, n): # inner for loop
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break         # breaks out of inner for loop, go to P1
            # continue    # breaks the current iteration, go to P2

        # P2    
        else:
           # loop fell through without finding a factor
           print(n, 'is a prime number')


## END
