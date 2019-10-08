# !/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: moziran

# 这是一个购物商城程序
# 商品展示
# Product = {'1': ['a', 50], '2': ['b', 70], '3': ['c', 90], '4': ['d', 100], }
Product = {'a': 50, 'b':  70, 'c': 90, 'd':  100, }
print(Product)
# 个人账户余额
Account_Balance = 300
Cart_Price = 0

# 购买商品，先建立一个空的购物车,初始价格为0
Cart_dic = []
Cart_Flag = True
Cart = input("请加入你选择的商品编号(若已完成添加请输入0)：")
while Cart_Flag:
    if Cart == str(0):     #这里0 是默认int型，要转换成str才能比较
        break
    else:
        print(Product[Cart])
        Cart_Price = Cart_Price + Product[Cart]


        Cart_dic.append(Cart)
        Cart = input("请加入你选择的商品编号(若已完成添加请输入0)：")
print('请确认您购买的商品是：'+str(Cart_dic))

if Cart_Price > Account_Balance:
    print('余额不足，请充值！')
else:
    Account_Balance = Account_Balance - Cart_Price
    print("交易成功,账户余额为" + str(Account_Balance))


# Cart_Price = 0
# for m in Product.values():
#     Cart_Price = Cart_Price + m
# # print(Cart_Price)
# if Cart_Price > Account_Balance:
#     print('余额不足，请充值！')
# else:
#     Account_Balance = Account_Balance - Cart_Price
#     print("交易成功,账户余额为" + str(Account_Balance))



