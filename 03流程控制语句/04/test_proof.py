# -*- coding:utf-8 -*-

"""
   @ 功能：判断是否为酒驾
   @ author:无语
   @ create:2018-04-09

"""
print("\n为了您和他人的安全，严禁酒后开车！\n")
proof = int(input("请输入每100毫升血液的酒精含量："))  # 获取用户输入的酒精含量，并转换为整型
if proof < 20:  # 酒精含量小于20，不构成饮酒行为
    print("\n您还不构成饮酒行为，可以开车，但要注意安全!")
else:  # 酒精含量大于等于20，已经是饮酒行为
    if 80 > proof >= 20:  # 酒精含量大于等于20，但小于80，属于酒后驾驶
        print("\n已经达到酒后驾驶标准，请不要开车！")
    else:  # 酒精含量大于等于80，属于醉酒驾驶
        print("\n已经达到醉酒驾驶标准，千万不要开车！")
