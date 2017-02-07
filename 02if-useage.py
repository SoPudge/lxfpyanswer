# -*- coding: utf-8 -*-
#本文档显示if关键字用法及他的几个方法
#小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
    #低于18.5：过轻
    #18.5-25：正常
    #25-28：过重
    #28-32：肥胖
    #高于32：严重肥胖

height = float(input('请输入您的体重（KG）：'))
weight = float(input('请输入您的身高（M）：'))
#这里前面必须用float来定义输入的值为浮点，如果用int的话，只能输入整数，而用int或者float转换一次的原因是input的内容是str，必须转换成数字才能计算
bmi = weight/height/height
print(bmi)
if bmi < 18:
    print('体重过轻')
elif bmi <= 25:
    print('正常')
elif bmi <= 28:
    print('过重')
elif bmi <= 32:
    print('肥胖')
else:
    print('严重肥胖')
