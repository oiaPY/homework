# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran

f = open("user.txt", "w")
f.write("moziran")
f.write("\n3614")
# f.close()
f = open("user.txt", "r")
# f.write("moziran")
# f.write("\n361426491")
name = f.readline()
passwd = f.readline()
# print(type(name))
# print(type(passwd))
# print(name)
# print(passwd)
f.close()
for i in range(3):
    input_name = input("请输入你的用户名：")
    input_passwd = input("请输入你的密码：")
    # print(type(input_name))
    # print(type(input_passwd))

    # print(input_name)
    # print(input_passwd)
    if (name == input_name) and (passwd == input_passwd):
        print("欢迎进入系统！！")
        break
    else:
        print("你输入的用户名或密码错误！")
        continue
print("你的账户已被锁定，请稍后再试！")
