# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran

name = "aeiou"
passwd ="12345"
trantab = str.maketrans(name, passwd)
str = "This is a string example....wow!!!"
print(str.translate(trantab))
bytearray.translate()
# Name = name.upper()
# Name = name.capitalize()\




