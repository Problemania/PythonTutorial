#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

##
## Summary: simple Python program to show the usage of tuple keyword argument
## and dictionary keyword argument.
##
## * *tupleArg is a tuple keyword argument
##
## * **dictArg is a dictionary keyword argument
##
## * Regular argument must preceed tuple and dictioanry key word arguments,
## so there is no ambiguity.
##

def cheeseshop(regularArg, *tupleArg, **dictArg):
    print("-- Do you have any", regularArg, "?")
    print("-- I'm sorry, we're all out of", regularArg)
    for arg in tupleArg: print(arg)
    print("-" * 40)
    keys = sorted(dictArg.keys())
    for kw in keys: print(kw, ":", dictArg[kw])

cheeseshop("Limburger",

	   # *tupleArg
	   "It's very runny, sir.",
	   "It's really very, VERY runny, sir.",

	   # **keywords
	   shopkeeper="Michael Palin",
	   client="John Cleese",
	   sketch="Cheese Shop Sketch")
# END
