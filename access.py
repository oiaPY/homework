# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran

# 创建存放用户信息的txt文件，并写入用户名和密码，分列两行
f = open("user.txt", "w")
f.write("moziran")
f.write("\n3614")
# f.close()

# 打开文件，分别读两行的内容，并存到两个变量中，用于之后的比较
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

# 执行for循环，三次退出，提示用户账号密码锁定
for i in range(3):
    #input获取用户输入
    input_name = input("请输入你的用户名：")
    input_passwd = input("请输入你的密码：")
    # print(type(input_name))
    # print(type(input_passwd))
    # print(input_name)
    # print(input_passwd)
    #判定用户名和密码是否和用户信息文件中的一致（一致输出欢迎信息；不一致提示用户名或密码错误）
    if (name == input_name) and (passwd == input_passwd):
        print("欢迎进入系统！！")
        break
    else:
        print("你输入的用户名或密码错误！")
        continue
# 循环结束提示用户账号被锁定
print("你的账户已被锁定，请稍后再试！")
