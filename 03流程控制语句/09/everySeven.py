# -*- coding:utf-8 -*-

"""
   @ 功能：模拟逢七拍腿游戏
   @ author:无语
   @ create:2018-04-10

"""
total = 99  # 记录拍腿次数的变量
for number in range(1, 100):  # 创建一个从1到100（不包括)的循环
    if number % 7 == 0:  # 判断是否为7的倍数
        continue  # 继续下一次循环
    else:
        string = str(number)  # 将数值转换为字符串
        if string.endswith('7'):  # 判断是否以数字7结尾
            continue  # 继续下一次循环
    total -= 1  # 可拍腿次数-1
print("从1数到99共拍腿", total, "次。")  # 显示拍腿次数
