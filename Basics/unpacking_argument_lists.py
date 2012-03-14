#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
 
################################################################################ 
## Summary: simple Python program demonstrating unpacking argument lists for
## functions.
################################################################################ 

argsList = [1, 'a', [1, 2], (3, 4)]

argsTuple = (1, 'a', [1, 2], (3, 4))

def func1(*args):
    print(args)

    
func1(*argsList)

func1(*argsTuple)

argsDictionary = {"arg1": 1, "arg2": 'a', "arg3": [1,2], "arg4": (3,4)}

def func2(arg1, arg2, arg3=[2,3], arg4=(5,6)):
    print(arg1, arg2, arg3, arg4)

    
def func3(**args):
    print(args)

    
func2(**argsDictionary)
func3(**argsDictionary)
    
## END
