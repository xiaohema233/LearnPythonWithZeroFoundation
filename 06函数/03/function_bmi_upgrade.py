def fun_bmi_upgrade(*person):
    """功能：根据身高和体重计算BMI指数（升级版）
       *person：可变参数该参数中需要传递带3个元素的列表，
       分别为姓名、身高（单位：米）和体重（单位：千克）
    """
    for list_person in person:
        for item in list_person:
            person = item[0]  # 姓名
            height = item[1]  # 身高（单位：米）
            weight = item[2]  # 体重（单位：千克）
            print("\n" + "=" * 13, person, "=" * 13)
            print("身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")
            bmi = weight / (height * height)  # 用于计算BMI指数，公式为“体重/身高的平方”
            print("BMI指数：" + str(bmi))  # 输出BMI指数
            # 判断身材是否合理
            if bmi < 18.5:
                print("您的体重过轻 ~@_@~")
            if 18.5 <= bmi < 24.9:
                print("正常范围，注意保持 (-_-)")
            if 24.9 <= bmi < 29.9:
                print("您的体重过重 ~@_@~")
            if bmi >= 29.9:
                print("肥胖 ^@_@^")


# *****************************调用函数***********************************#
list_w = [('绮梦', 1.70, 65), ('零语', 1.77, 50), ('黛兰', 1.72, 66)]
list_m = [('梓轩', 1.80, 75), ('冷伊一', 1.75, 70)]
fun_bmi_upgrade(list_w, list_m)  # 调用函数指定可变参数
