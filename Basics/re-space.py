#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

## Summary: Find Unicode characters matching regexp '\r' (in re) and
## '[[:space:]]' in regex. Usage of char() and unichr().
## 
##

##
## also we go up to 0x10ffff (inclusive) because that's what help(unichr) says.
##
## * Python doc:
##     http://docs.python.org/library/functions.html#unichr
##
## * Remarks:
##   - c is Unicode code
## 
#unicodeChars = [unichr(c) for c in range(0x10FFFF+1)] # wide Python build
unicodeChars = [unichr(c) for c in range(0xFFFF+1)] # narrow Python build
str = ''.join(unicodeChars)

##
## Find characters matching `\s` with `re` module:
## * Output:
##     [u'\t', u'\n', u'\x0b', u'\x0c', u'\r', u' ']
##
import re
whiteSpaceChar=re.findall('\s',str)
print(whiteSpaceChar)

whiteSpaceCode=[ord(char) for char in whiteSpaceChar]
print(whiteSpaceCode)

##
## Find characters matching `[[:space:]]` with `regex` module:
##
## * Install regex package
##   - Macports:
##       $ sudo port install py27-regex
##
import regex
spaceChar=regex.findall("[[:space:]]",str)
print(spaceChar)

spaceCode=[ord(char) for char in spaceChar]
print(spaceCode)

