# print(10 > 5)
# print(10 < 5)

# print(True + 20)
# print(False == 0)

# print(bool("NISHISHUI"))
# print(bool(0))

# month = input()
# month = float()
# print(type(month))

# a = 2
# n = '2'
# print(a, type(a))
# print(n,type(n))

# 请在此处编写代码
# age = 20
# height = 1.75
# name = "张三"
# cheng = True
# print("年龄：",age ,type(age))
# print("姓名：",name ,type(name))
# print("身高：",height ,type(height))
# print("成年：", cheng,type(cheng))
# 预期输出示例：
# 年龄: 20, 类型: <class 'int'>
# 身高: 1.75, 类型: <class 'float'>
# 名字: 张三, 类型: <class 'str'>
# 成年: True, 类型: <class 'bool'>

#字符串拼接
# print("hi\n" * 5)
# print("ho"+"llo")

# print(None == 0)
# print(None == '')
# print(None == [])


# print(52 // 255)#取整除运算符

#取余
# print(9%3) #被除数被除数整除时，余数为0
# print(255 % 355) #被除数小于除数时，余数就是被除数本身

# n = 3
# n = n + 9
# m = n - 5
# n = n * 2
# n = n / 6
# m = m + (n // 2)
# m = m - (n % 1)
# n = (n ** 2)
# print(n ,m)


# num = 1
# num += 2 #num=3
# num -= 1 #2
# num *= 6 #12
# num /= 2 #6.0
# num //= 2 #3.0
# num +=14 #17.0
# num %= 5 #2.0
# num **=2 #4
# print(num)


# x = 20
# y = "5.0"
# print(x == y)
# print(x!=y)
# print(x != y)

# print(ord("h"))
# print(ord("a"))
# print(ord("o"))
# print(ord("好"))
# print(ord("人"))
# print(ord("隆"))
# print(chr(22909),chr(20154),chr(38534))


# 判断 a 是否大于 b，输出比较结果
# 判断 a 是否大于 10 且 b 小于 10，输出逻辑结果
# a = 17
# b = 5
# print("a>7的结果时：",a > b)
# z = a > 10 and b < 10
# print(z)



# 用 input() 接收学生成绩（整数）
# 判断成绩是否在 0-100 之间，如果不是则输出"成绩输入有误"
# 根据成绩输出对应等级
# while True:
#     chengji = float(input("请输入你的成绩："))
#     if 0 < chengji <= 100:
#         print("输入正确")
#         if chengji>90:
#             print("你的成绩优秀")
#         elif chengji>90:
#             print("你的成绩良好")
#         elif chengji<60:
#             print("你的成绩不好")
#     else:    
#         print("输入有误，请重新输入！")


#逻辑或
# print(67 % 5 > 3 or 'string' == '0' or 41 or (2 ** 3 // 2) > 66)

# print(12 < 1 and 0 or 23 > 1)#True
# print(20 or 10>12 and 20 < 210 or 52 < 53)#2True
# print(84 != 73 and not 22 > 22 or 31== 27 and '张三' == '李四' or 18 >20)
# print(84 != 73 and not 22 > 22 or 31== 27 and '张三' == '李四' or 18 >20)
#True and not False or False and False False
#Ture
# print(0 or 12 < 13 and 12)#12
# print(84 != 73 and (not 22> 22 or 31 == 27)and '张三' == '李四' or 18 > 20)
# print(84 != 73 and (not 22> 22 or 31 == 27)and '张三' == '李四' or 18 > 20)
#Ture and False or False
#Ture

# x = input("请输入你的账号：")
# y = int(input("请输入你的密码："))
# if x != "hb123":
#     print("你的账号错误")
# if y != 123:
#     print("你的密码错误")
# else:
#     print("你的密码正确")

# z = int(input(""))
# x = '奇数' if z%2 == 0 else '偶数'
# print(x)

# num = 12
# if num >0:
#     if num == 0:
#         print('等于0')
#     else:
#         print('大于0')
# else:
#     print('小于0')

# age = int(input('请输入你的年龄：'))
# while age>0:
    
#     if age < 18:
#         print('未成年人')
#     elif age <35:
#         print('青年人')
#     elif age <55:
#         print('中年人')
#     else:
#         print('老年人')
#     break

# ticket=False
# my_object = False
# if ticket:
#     print("可以进去安检")
#     if my_object:
#         print("带了违禁物品需要没收")
#     else:
#         print("可以进去候车了!")
# else:
#     print("没有购票,请先购票")


# 题目：根据要求定义变量并输出类型
"""
1. 定义一个整数变量 age，值为 25
2. 定义一个浮点数变量 height，值为 1.68
3. 定义一个字符串变量 name，值为 "王小明"
4. 定义一个布尔变量 is_working，值为 True
5. 分别打印每个变量的值和类型
"""

# 请在此处编写代码

# age = 25
# height = float(1.68)
# name = '小明'
# is_working = True
# print(type(age))
# print(type(height))
# print(type(name))
# print(type(is_working))


"""
1. 将字符串 "123" 转换为整数，并乘以 2，输出结果
2. 将整数 45 转换为字符串，并与 "岁" 拼接，输出结果
3. 将整数 10 转换为浮点数，并除以 3，输出结果
4. 将浮点数 3.14 转换为整数，输出结果（观察发生了什么）
"""

# 请在此处编写代码
# num = int("123") * 2
# print(num)
# num_str = str(45)
# print(num_str + '岁')
# num_float = float(10) / 3
# print(num_float)
# num_int = int(3.14)
# print(num_int)

""""
1. 定义长 length = 12.5，宽 width = 8
2. 计算面积（长 × 宽），并输出
3. 计算周长（（长 + 宽）× 2），并输出
"""

# 请在此处编写代码
# length = float(12.5)
# width = 8
# print(length * width)
# print((length + width) * 2) 

"""
定义 a = 15，b = 20，c = 15
分别判断并输出以下比较结果：
1. a 是否等于 c
2. a 是否大于 b
3. a 是否小于等于 b
4. a 是否不等于 b
"""
# a =15
# b = 20
# c = 15
# print(f"a == c：{a == c}")      # True
# print(f"a > b：{a > b}")        # False
# print(f"a <= b：{a <= b}")      # True
# print(f"a != b：{a != b}")
# if a == c:
#     print('等于c')
# else:
#     print('不等于c')
# if a > b:
#     print('大于b')
# elif a == b:
#     print('等于b')
# else:
#     print('小于b')

"""
用户输入年龄和月薪，判断是否符合以下条件：
- 年龄在 22 到 35 岁之间（包含边界）
- 月薪大于 8000
两个条件都满足才能通过筛选
"""
# age = int(input('请输入你的年龄：'))
# num = int(input('请输入你的工资：'))
# if 22 <= age <= 35 and num > 8000:
#     print('恭喜你')
# else:
#     print('你不行')

"""
现有 x = 10，依次执行以下操作，每次操作后输出 x 的值：
1. x 增加 5
2. x 乘以 2
3. x 除以 3（整数除法）
4. x 对 4 取余
"""
"""x = 10
x += 5
print(x)
x *= 2
print(x)
x //= 3
print(x)
x %= 4
print(x)"""

"""
输入一个整数，判断它是奇数还是偶数，并输出结果。
提示：能被 2 整除的是偶数，否则是奇数。
"""
# num = int(input('请输入一个整数：'))

# if num % 2 == 0:
#     print('偶数')
# else:
#     print('奇数')

# 题目：判断季节
"""
输入月份（1-12），输出对应的季节：
- 春季：3、4、5月
- 夏季：6、7、8月
- 秋季：9、10、11月
- 冬季：12、1、2月
如果输入不在 1-12 范围内，提示输入错误。
"""
# mouth = int(input('请输入现在几月：'))
# if 3 <= mouth <= 5:
#     print('现在是春季')
# elif 6 <= mouth <= 8:
#     print('现在是夏季')
# elif 9 <= mouth <= 11:
#     print('现在是秋季')
# elif 12 <= mouth <= 2:
#     print('现在是冬季')
# else:
#     print('你输错了')

"""
电影院购票规则：
- 普通票价 50 元
- 儿童（12岁以下）：半价
- 老人（65岁以上）：免费
- 学生（凭学生证）：7折

要求：输入年龄，询问是否有学生证（输入 y 或 n），计算应付金额。
"""
# age = int(input('请输入您的年龄：'))
# price = 50
# if  age > 12:
#     print(f'你的年龄大于12，不能半价')
#     yes = input('是否有学生证（输入 y 或 n）')
#     if yes == 'y':
#         print(f'七折{price*0.7}')
#     else:
#         print('不能七折')
# elif age >= 65:
#     print('免费')
# else:
#     print(f'未满12，可以半价，你需要付{price/2}')

"""
税率规则：
- 月薪 ≤ 5000：免税
- 5000 < 月薪 ≤ 8000：超出5000的部分按 3% 纳税
- 8000 < 月薪 ≤ 17000：超出8000的部分按 10% 纳税
- 月薪 > 17000：超出17000的部分按 20% 纳税

要求：输入月薪，计算应缴纳的税费和税后收入。
"""
# salary = int(input('请输入你的工资：'))
# if 5000 > salary:
#     print('免税')
# else:
#     if salary <= 8000:
#         print(f'你的工资应缴纳{salary * 0.03},税后收入为{salary-(salary * 0.03)}')
#     else:
#         if salary <= 17000:
#             print(f'你的工资应缴纳{salary * 0.1},税后收入为{salary-(salary * 0.1)}')
#         else:
#             print(f'你的工资应缴纳{salary * 0.2},税后收入为{salary-(salary * 0.2)}')

"""
预设账号和密码：
- 用户名：admin
- 密码：123456

要求：
1. 输入用户名和密码
2. 如果用户名错误，提示"用户名不存在"
3. 如果用户名正确但密码错误，提示"密码错误"
4. 如果都正确，提示"登录成功"
"""
# username = "admin"
# password = 123456

# while True:
#     zhanghao = input('请输入你的账号：')
#     shu_password = int(input('请输入密码：'))
#     if zhanghao == username and shu_password == password:
#         print('登陆成功')
#         break
#     else:
#         if zhanghao == username:
#             print('你的账号正确')
#             if shu_password == password:
#                 print('你的密码正确')
#             else:
#                 print('你的密码错误')
#         else:
#             print('你的账号错误')
    
    
    