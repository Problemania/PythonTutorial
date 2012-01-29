#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

for n in range(10):
    r = random.randrange(6,15) # get random int in [0,10)
    print("n = ", n, ", r = ", r)
    if r == n:                 # skip iteration if r == n 
        print("run continue")
        continue               
    if r < n:                  # exit the loop if r < n
        print("run break")
        break                  
    print("completed interation and avoided continue/break")
else:                          # else branch is run only if all iterations in for loop completed without break
    print("loop was never broken as r was larger than n in all interations!\n")
if n<9:                        # this will always be run after the for loop
    print("loop broken before the last iteration! \n")
