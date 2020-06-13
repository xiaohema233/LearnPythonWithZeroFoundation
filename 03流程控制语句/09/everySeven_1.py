# -*- coding:utf-8 -*-

"""
   @ 功能：模拟逢七拍腿游戏
   @ author:无语
   @ create:2018-04-10

"""
total = 99  # 记录拍腿次数的变量
count = 0
for number in range(1, 100):  # 创建一个从1到100（不包括)的循环
    if number % 7 == 0 or str(number).endswith('7'):  # 判断是否为7的倍数
        count += 1
print("从1数到99共拍腿", count, "次。")  # 显示拍腿次数
