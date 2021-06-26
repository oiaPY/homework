# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran

#程序bug：这样每次就锁定第三次输入的用户，这肯定是不对的（假如第一次第二次输入A，第三次输入C
# ， 这样就会把C锁定了，这不是我们想要的），可以在加一个标志，某个用户输入一次，加1，加到三次，锁定这个用户

import sys

account_file='D:\match.txt'
locked_file='D:\locked.txt'

def deny_account(username):
    print('您的用户已被锁定！')
    with file(locked_file,'a') as deny_f:
        deny_f.write('\n'+username)
#
def main():
    retry_count = 0
    retry_limit = 3                                                   #循环次数
    while retry_count < retry_limit:                                  #用户最多重复登录

        username = input('\033[32;1m请输入用户名：\033[0m')           #引导用户输入用户名
        with file(locked_file,'r') as lock_f:
            #采用with的方式打开文件，防止忘记f.close()关闭文件
        '''
         另外一种用户名匹配方式
         lines = []
         for line in lock_f.readlines():
             lines.append(line.strip())
         if username in lines:
        '''
#判断用户名是不是在黑名单里
            for line in lock_f.readlines():
               if len(line)==0:
                 continue
               if username == line.strip():
                sys.exit('\033[32;1m用户 %s 已经被锁定！\033[0m'% username)

#判断用户名是否为空
        if len(username)==0:
            print('用户名不能为空，请重新输入')
            continue


        password = input('\033[32;1m请输入密码：\033[0m')                #引导用户输入密码
        with file(account_file,'r') as account_f:
            flag=False

            for line in account_f.readlines():
                user,pawd=line.strip().split()                            #将用户名和对应密码分开
                if username == user and password == pawd:                 #判断用户名和密码是否一致
                    print('Success!')
                    print('欢迎用户%s来到老男孩登录系统'%username)
                    flag=True
                    break                                                  #退出for循环
        if flag==False:
            if retry_count<2:
                print('您的用户名或密码有误，请重新输入！')
            retry_count+=1
        else:
            break                                                          #加标志位再判断一次是为了退出while循环
    else:
        deny_account(username)


if _name_=='_main_':
    main()
