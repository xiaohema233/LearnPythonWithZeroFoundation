def fun_bmi(person):
    """功能：根据身高和体重计算BMI指数
       person[0]：姓名
       person[1]：身高，单位：米
       person[2]：体重，单位：千克
    """
    personname = person[0]
    height = person[1]
    weight = person[2] + 10
    person[2] = person[2] + 5
    print(personname + "的身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")
    bmi = weight / (height * height)  # 用于计算BMI指数，公式为“体重/身高的平方”
    print(personname + "的BMI指数为：" + str(bmi))  # 输出BMI指数
    # 判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻 ~@_@~\n")
    if 18.5 <= bmi < 24.9:
        print("正常范围，注意保持 (-_-)\n")
    if 24.9 <= bmi < 29.9:
        print("您的体重过重 ~@_@~\n")
    if bmi >= 29.9:
        print("肥胖 ^@_@^\n")
    print("函数体内：", id(person))
    print("函数体内：", person)


# *****************************调用函数***********************************#
list_person = [["路人甲", 1.83, 60], ["路人乙", 1.60, 50]]
for item in list_person:
    fun_bmi(item)  # 计算BMI指数
    print("函数体外：", id(item))
print("函数调用完毕：", list_person)
