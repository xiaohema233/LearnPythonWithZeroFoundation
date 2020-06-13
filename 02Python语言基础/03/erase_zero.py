# -*- coding:utf-8 -*-

"""
   @ 功能：模拟超市抹零结账行为
   @ author:无语
   @ create:2017-11-8

"""

money_all = 56.75 + 72.91 + 88.50 + 26.37 + 68.51  # 累加总计金额
money_all_str = str(money_all)                # 转换为字符串
print("商品总金额为：" + money_all_str)
money_real = int(money_all)                   # 进行抹零处理
money_real_str = str(money_real)              # 转换为字符串
print("实收金额为：" + money_real_str)
