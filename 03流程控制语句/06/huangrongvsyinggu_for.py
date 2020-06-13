# -*- coding:utf-8 -*-

"""
   @ 功能：助力瑛姑 ②：for循环版解题法
   @ author:无语
   @ create:2017-11-13

"""

print("今有物不知其数，三三数之剩二，五五数之剩三，七七数之剩二，问几何？\n")
for number in range(1000):
    if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:  # 判断是否符合条件
        print("答曰：这个数是", number)  # 输出符合条件的数
