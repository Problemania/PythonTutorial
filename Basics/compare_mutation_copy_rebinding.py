#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
## Summary: Simple example Python program to show the difference between
## 1) mutation, 2) making a copy of an object, and 3) rebinding.
##
## Output:
## [1, 2, 3, 4]
## [1, 2, 3, 4]
## [1, 2, 3, 4]
## [1, 2, 3, 4]
## [1, 2, 3, 4]
## [1, 2, 3]
## [1, 2, 3, 4]
## [1, 2, 3]

## Mutation:
## a.append(4) mutates the same list object that both a and b were referring to.
a = [1, 2, 3]
b = a # aliasing b and a, as both now point/refer to the same list object [1,2,3]
a.append(4)
print(a)  # output: [1, 2, 3, 4]
print(b)  # output: [1, 2, 3, 4]


## Alternatively, assignment operator such as += can be used to do list mutation
## in-place:
## a += [4] uses assignment operator += which combines operator + and assignment =
## but, it mutates the list object in-place rather than creates a new list object
## and rebind a:
##
a = [1, 2, 3]
b = a
# a = a + [4] # uncomment this line and comment the next to see difference   
a += [4]  # should this line be a = a + [4], b will be left as [1,2,3]
print(a)  # output: [1, 2, 3, 4]
print(b)  # output: [1, 2, 3, 4]


##
## Making a copy:
## a[:] created a copy of the first list object and bound b to it, hence
## although a.append(4) mutated the first list object, it didn't affect
## b.
a = [1, 2, 3]
b = a[:]
a.append(4)
print(a)  # output: [1, 2, 3, 4]
print(b)  # output: [1, 2, 3]

##
## Rebinding:
## a + [4,] creates a new list object and a = a + [4,] rebinds a to the new
## list object, while b was left bound to the first list object [1, 2, 3].
a = [1, 2, 3]
b = a
a = a + [4,]
print(a)  # output: [1, 2, 3, 4]
print(b)  # output: [1, 2, 3]



## END
