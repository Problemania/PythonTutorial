#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
## One-character Unicdoe string
##   u'<unicode character>'
##   u'\u<unicode number>' ???

char1 = u'《'
print char1
print ord(char1)

strChinese = u'關'
print strChinese
print ord(strChinese)

currency = u'€'
print currency
print ord(currency)


charUnicode = u'\u6234' # hexadecimal number 0x6234
print charUnicode       # output: 戴
print ord(charUnicode)  # will print decimal 25140 which is equal to 0x6234

