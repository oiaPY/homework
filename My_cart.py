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

# 结算确认模块
Cart_Claim = input("是否确认？(y or n)：")
# 结算确认无误，现金收讫
if Cart_Claim == 'y':
    if Cart_Price > Account_Balance:
        print('余额不足，请充值！')
    else:
        Account_Balance = Account_Balance - Cart_Price
        print("交易成功,账户余额为" + str(Account_Balance))
# 结算确认不通过，顾客仍需要添加或者删除购物车商品
else:
    Cart_decision = input("请选择添加还是删除商品（add or del）：")
# 结算仍有需要添加的商品，返回添加
    if
    while Cart_Claim == 'n' and Cart_decision == 'add':
        Cart_Flag = True
        Cart = input("请添加你需要的商品编号(若已完成添加请输入0)：")
        while Cart_Flag:
            if Cart == str(0):
                break
            else:
                print(Product[Cart])
                Cart_Price = Cart_Price + Product[Cart]
                Cart_dic.append(Cart)
                Cart = input("请添加你需要的商品编号(若已完成添加请输入0)：")
        print('请确认您购买的商品是：' + str(Cart_dic))
        Cart_Claim = input("是否确认？(y or n)：")
    if Cart_Price > Account_Balance:
        print('余额不足，请充值！')
    else:
        Account_Balance = Account_Balance - Cart_Price
        print("交易成功,账户余额为" + str(Account_Balance))


#   else:
#       print("您的输入有误，请重新输入。/n")
#       print()


# Cart_Price = 0
# for m in Product.values():
#     Cart_Price = Cart_Price + m
# # print(Cart_Price)
# if Cart_Price > Account_Balance:
#     print('余额不足，请充值！')
# else:
#     Account_Balance = Account_Balance - Cart_Price
#     print("交易成功,账户余额为" + str(Account_Balance))



