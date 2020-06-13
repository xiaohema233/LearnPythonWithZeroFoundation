str1 = "千山鸟飞绝"
str2 = "万径人踪灭"
str3 = "孤舟蓑笠翁"
str4 = "独钓寒江雪"
verse = [list(str1), list(str2), list(str3), list(str4)]   # 定义一个二维列表
print("\n-- 横版 --\n")
for i in range(4):                                 # 循环古诗的每一行
    for j in range(5):                             # 循环每一行的每个字（列）
        if j == 4:                                  # 如果是一行中的最后一个字
            print(verse[i][j])                      # 换行输出
        else:
            print(verse[i][j], end="")             # 不换行输出

verse.reverse()                                      # 对列表进行逆序排列
print("\n-- 竖版 --\n")
for i in range(5):                                   # 循环每一行的每个字（列）
    for j in range(4):                               # 循环新逆序排列后的第一行
        if j == 3:                                    # 如果是最后一行
            print(verse[j][i])                       # 换行输出
        else:
            print(verse[j][i], end="")              # 不换行输出
