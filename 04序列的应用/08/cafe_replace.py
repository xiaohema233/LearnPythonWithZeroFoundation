coffeename = ('蓝山', '卡布奇诺', '曼特宁', '摩卡', '麝香猫', '哥伦比亚')  # 定义元组

# 执行下面的代码将抛出异常
coffeename[4] = '拿铁'  # 将“麝香猫”替换为“拿铁”
print(coffeename)

# 下面的代码可以正常执行
##coffeename = ('蓝山','卡布奇诺','曼特宁','摩卡','拿铁','哥伦比亚')   # 对元组进行重新赋值
##print("新元组",coffeename)
