#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

################################################################################ 
## Summary: simple Python program demonstrating list comprehension.
################################################################################ 

l = [(x, y) for x in [1, 2, 3] for y in [3, 4, 5] if x != y]

print(l)


## flatten a depth-2 list by list comprehension with two 'for'

array = [[1, 2], [3, 4, 5]]

l = [elem for sublist in array for elem in sublist]

print(l)

array = [(1, 2), (3, 4, 5)]

l = [elem for sublist in array for elem in sublist]

print(l)

## END
