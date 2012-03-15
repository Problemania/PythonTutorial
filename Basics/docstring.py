#!/usr/bin/env python3.2
# -*- coding: utf-8 -*-

################################################################################ 
## Summary: simple Python program demonstrating documentation string,
## specifically, using multiple lines.
##
## * Example:
## $ ./docstring.py
## This is the documentation string.
## 
##     This is the first paragraph of extensive documentation.
## 
##     This is the second paragraph.
################################################################################ 

def noop(arg):
    """This is the documentation string.

    This is the first paragraph of extensive documentation.

    This is the second paragraph."""

    pass


print(noop.__doc__)


## END
