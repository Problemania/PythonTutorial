#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-
 
################################################################################ 
## Summary: simple Python program demonstrating arbitary argument lists for
## functions.
##
## * Example:
##     In [7]: toFileName("~", "Temp", lastPart="temp.txt")
##     Out[7]: '~/Temp/temp.txt'
################################################################################ 

def toFileName(*pathParts, lastPart="", separator="/"):
    path = separator.join(pathParts)
    res = separator.join((path, lastPart))
    return res


# Example:
res = toFileName("~", "Temp", lastPart="temp.txt")

print(res)

## END
