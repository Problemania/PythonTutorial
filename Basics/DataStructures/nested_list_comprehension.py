#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

################################################################################ 
## Summary: simple Python program demonstrating list comprehension.
################################################################################ 

array = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
print(array)
## => [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

## transpose a matrix
l = [[row[idx] for row in array] for idx in [0, 1, 2]]
print(l)
## => [[8, 3, 4], [1, 5, 9], [6, 7, 2]]

## take the subarray of rows 1 to 2, and columns 2 and 0, in that order
l = [[row1[j] for row1 in [[row[i] for row in array] for i in [2, 0]]] for j in [1, 2]]
print(l)
## => [[7, 3], [2, 4]]

## END
