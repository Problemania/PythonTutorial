#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

## * Summary: Find Unicode characters matching regexp '\r' (in re) and
## '[[:space:]]' in regex. Usage of char() and unichr().
## 
## * Python doc:
##   - http://docs.python.org/library/functions.html#unichr
##   - http://docs.python.org/library/functions.html#ord
##   - http://docs.python.org/library/functions.html#xrange
##
## * Non-break space
##   - http://en.wikipedia.org/wiki/Non-breaking_space
##
##

##
## * Remarks:
##   - c is Unicode code
##   - xrange() is advantageous than range() since most elements aren't used
## 

#unicodeChars = [unichr(c) for c in range(0x10FFFF+1)] # wide Python build
#unicodeChars = [unichr(c) for c in range(0xFFFF+1)] # narrow Python build
import sys
str = u''.join(unichr(c) for c in xrange(sys.maxunicode+1)) # generic, with sys
print "sys.maxunicode = ", sys.maxunicode, " = ", hex(sys.maxunicode)

##
## Find characters matching `\s` with `re` module:
## * Output:
##     [u'\t', u'\n', u'\x0b', u'\x0c', u'\r', u' ']
##
print("Use re:")
import re
whiteSpaceChar=re.findall(r'\s',str)
print "Whitespace characters matching \s using re: ", whiteSpaceChar

## Include Non-break space
allWhiteSpaceChar=re.findall(r'\s', str, re.UNICODE)
print "Whitespace characters matching \s using re.UNICODE: ", allWhiteSpaceChar


from unicodedata import name
print "Unicode ordinal, ", "Unicode string literal, ", "Unicode character name"
for char in allWhiteSpaceChar:
  print ord(char), repr(char), name(char, '')









##
## Find characters matching `[[:space:]]` with `regex` module:
##
## * Install regex package
##   - Macports:
##       $ sudo port install py27-regex
##
print("\n\nUse regex:")
import regex
spaceChar=regex.findall("[[:space:]]",str)
print(spaceChar)

spaceCode=[ord(char) for char in spaceChar]
print(spaceCode)

