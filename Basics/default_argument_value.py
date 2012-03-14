#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

## Summary: simple example program to show default value assignment for
## function argument

## -----------------------------------------------------------------------------
## The list object is assigned to a default value
## and it only evaluates once.  The list object is mutated in the function.
def f1(a, l=[]):
    l.append(a)
    return(l)

## l is set to default value [] then 1 is appended to it by mutating the list.
print(f1(1)) # output: [1]

## l is [1] and the second 1 is appended to it
print(f1(1)) # output: [1, 1]

## l is [1, 1] and the third is appended to it
print(f1(1)) # output: [1, 1, 1]


## -----------------------------------------------------------------------------
## But using rebinding will not give 
def f2(a, b=1):
    b = b + 1 # rebinding, *not* mutation
    return(a+b)

## The default value assignment is evaluated b is set to default value 1, and a
## new integer object is created by b+1 and b was rebound to it by b = b+1.
print(f2(1)) # output: 3

## The default value assignment b=1 is not evaluated, but as the integer object
## that b was bound to hasn't mutated, it is still 1, a third integer object is
## created by b+1 and b was again rebound to it by b = b+1.
print(f2(1)) # output: 3

## The same thing happened again.
print(f2(1)) # output: 3


## -----------------------------------------------------------------------------
## Use None and condtional to avoid sharing the same object between different
## function calls.  l is set to None each time the function is called.
def f3(a, l=None):
    if l == None:
        print("l == None, so this is run!")
        l = []
    l.append(a)
    return(l)

## l is set to default value [] then 1 is appended to it by mutating the list.
print(f3(1)) # output: [1]

## l is [1] and the second 1 is appended to it
print(f3(1)) # output: [1]

## l is [1, 1] and the third is appended to it
print(f3(1)) # output: [1]

## END
