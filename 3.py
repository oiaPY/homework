# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran
'''
li = list([1, 2, 3])
print(li)
li.extend([11, 22, ])
# li.extend((11, 22, ))
print(li)
'''

# li = list([1, 2, 3])
# print(li)
# gat = li.pop(0)
# print(li)
# print(gat)

# li = list([1, 1, 2, 3])
# li.remove(1)
# print(li)

# li = list([1, 2, 3, 4, 5])
# print(li)
# li.reverse()
# print(li)

# dic1 = {'k1': 'v1', 'k2': 'v2'}
# print(dic1)
# dic2 = dict(k1='v1', k2='v2')
# print(dic2)

dic = dict(k1='v1', k2='v2')
# print(dic['k1'])
# print(dic['k2'])
# # print(dic['k3'])
print(dic.get('k1'))
print(dic.get('k2'))
print(dic.get("k3", "alex"))