"""list = ['看书', '听歌', '看电影', 123, 456, True, ['吃饭', '睡觉']]
# print(list)
# print(type(list))
# print(list[3])
# print(list[6][1])
# print(list[0:2])
# print(list[2:5:2])
# print(list[0::2])
print(len(list))
print('看书' in list)# True
print(135 not in list)# True
print('睡觉' in list)# False
print('睡觉' in list[6])# True"""

# month = input('请输入月份：')
# if month in [3, 4, 5]:
#     print('春季')
# elif month in [6, 7, 8]:
#     print('夏季')
# elif month in [9, 10, 11]:
#     print('秋季')
# else:
#     print('冬季')

# if month in '345':
#     print('春季')

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list3 = list1 + list2
# print(list3)
# li = []
# l2 = list()
# print(li)
# print(l2)

# li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# print(li[0])
# li[0] = int(li[0])
# print(li)
# print(li)

# x = 0
# while x < len(li):
#     li[x] = int(li[x])
#     x += 1
# print(li)
              
# for x in len(li):
#     li[x] = int(li[x])
#     x += 1
# print(li)
# while 0 <= 100:
#     num = int(input('请输入一个整数：'))
#     if num == 5:
#         print('答对了')
#         break
#     elif num < 5:
#         print('你输入的数太小了')
#     else:
#         print('你输入的数太大了')
# num = 200
# while num >= 200 and num <= 250:
#     num += 1
#     if num % 2 == 0:
#         print(f'{num} 是偶数')


# for num in range(1,10):
#     for i in range(1,10):
#         print(f'{i} * {num} = {i*num}', end='\n')
# x = 1
# y = 0
# while x < 101:
#     y = y + x
#     x += 1
# print(y)

# x = 0
# for i in range(101):
#     x = x + i
#     if i % 2 == 0:
#         x = x - i
# print(x)

# x = 0
# for i in range(101):
#     if i % 2 == 0:
#         x = x + i
# print(x)


# while True:
#     x = int(input('请输入一个整数：'))
#     if x > 0:
#         print('*\n' * x)
# x = 0
# y = 0
# while x < 100:
#     x +=1
#     y = y + x
# print(y)

# x = 1
# while x < 51:
#     x += 1
#     if x % 2 == 0:
#         print(x)

# for i in range(10,0,-1):
#     print(i)
# x = 11
# while 1 < x < 12:
#     x -= 1
#     print(x)

# x = int(input('请输入一个整数：'))
# while x > 0:
#     print('*\n' * x)
#     break

#送玫瑰花表白
# i = 1
# while i <= 99:
#     print(f'第{i}天表白')
#     j = 1
#     while j <= 10:
#         print(f'第{j}朵玫瑰')
#         j += 1
    
#     if i == 99:
#         print('表白成功了！')
#     i += 1

#九九乘法表
# i = 1
# for i in range(1, 10):
#     for j in range(1,i + 1):
#         print(f'{j} * {i} = {j*i}', end='\t')
#     print('')
# i = 1
# while i < 10:
#     j =1
#     while j < i + 1:
#         print(f'{j} * {i} = {j*i}', end='\t')
#         j += 1
#     i +=1
#     print('')

# i = 9
# while i > 0:
#     for j in range(1, i+1):
#         print(f'{j} * {i} = {j*i}', end='\t')
#     i -=1
#     print('')


# for i in range(9,0,-1):
    
#     x = 1
#     while x <= i:
#         print(f'{i} * {x} = {i*x}', end='\t')
#         x += 1
    
#     print('')  

# i %= 0，i是1到1000的数，求能被7整除的数
# i= 1
# while i < 1000:
#     i += 1
#     if i % 7 == 0:
#         print(i)

# 1到20的阶乘和
# i = 1
# x = 1
# y = 0
# while i <= 20:
#     x = x * i
#     y = y + x
#     i += 1
# print(y)
#
# li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# j = 0
# for i in li:
#     li[j] = int(i)
#     j += 1
# print(li)
# i = 0
# while i < len(li):
#     li[i] = int(li[i])
#     i += 1
# print(li) 

#append增加
# li = [1, 2, 3]
# li.append("4")
# print(li)

# li = ['1', '2', '3', '4', '5', '6', '7']
# li_1 = []
# i =0
# while i < len(li):
#     li_1.append(int(li[i]))
#     i += 1
# print(li_1)

# #extend分散增加
# li = ['1', '2']
# li.extend([3, 4])
# print(li)
# #insert指定位置增加
# li.insert(4, '5')
# print(li)
# #remove删除
# li.remove(4)

# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# for i in li[3:]:
#     li.remove(i)
# print(li)
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# l2 = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# for i in l2:
#     if i == 9:
#         li.remove(i)
# print(li)

# l3 = []
# for i in li:
#     if i != 9:
#         l3.append(i)
# print(l3)

#列表：pop():默认删除最后一个元素，也可以指定位置删除
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# print(li.pop(-3))

#del删除
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# del li[3]
# print(li)
# del li
# print(li)

#修改列表元素
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# li[3] = 4
# print(li)

#查询列表元素
#（1）index：返回元素第一次出现的索引位置，如果元素不存在会报错
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# print(li.index(9))

#（2）count：返回元素在列表中出现的次数
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# print(li.count(9))

# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# for i in range(li.count(9)):
#     li.remove(9)
# print(li)

# num = li.count(9)
# i = 0
# while i < num:
#     li.remove(9)
#     i += 1
# print(li)

#排序，sort：默认升序，reverse=True降序
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# li.sort()
# print(li)
# li.sort(reverse=True)
# print(li)

#sorted：返回一个新的排序后的列表，原列表不变
#sorted(iterable, key=None, reverse=False)
# li = ["1", "2", "3", "9", "9", "9", "56", "69", "7", "8", "9"]
# # li2 = sorted(li, reverse=True)
# # print(li2)
# li2 = sorted(li, key=len)
# print(li2)

#reverse：返回一个反转后的列表，原列表不变
# li = [1, 2, 3, 9, 9, 9, 5, 6, 7, 8, 9]
# li.reverse()
# print(li)

#isinstance：判断一个对象是否是某个类型的实例，返回True或False
#1.检查单个类型，判断一个变量是否是字符串类型，
# x = 'hello world'
# print(isinstance(x, str))# True
# print(isinstance(x, int))# False

# x = [1, 2, 3]
# print(isinstance(x, list))# True
# print(isinstance(x, tuple))# False

# s = [1, 2, 3, 4, 5]
# s.extend(['a', 'b', 'c'])
# print(s)

# s = [1, 2, 3, 4, 5]
# s.insert(5,6)#指定一个位置增加
# print(s)

# s = [1, 2, 3, 4, 5]
# s[4:] = [6, 7, 8]#指定一个位置增加
# print(s)

# list1 = [1, 2, 8, 9]
# list2 = [3, 4, 5, 6, 7]
# list1[2:2] = list2#指定一个位置增加
# print(list1)



# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{j} * {i} = {j*i}', end='\t')
#     print('')

# i = 9
# while i > 0:
#     j = i
#     while j > 0:
#         print(f'{j} * {i} = {j*i}', end='\t')
#         j = j - 1
#     i = i - 1
#     print('')

#输出一个数，判断这个数是否为质数
num = int(input('请输入一个整数：'))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} 不是质数')
            break
    else:
        print(f'{num} 是质数')
