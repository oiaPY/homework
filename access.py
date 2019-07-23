# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran

f = open("user.txt", "r+")
f.write("moziran")
f.write("\n361426491")
name = f.readline()
code = f.readline()
print(name)
print(code)
f.close()
