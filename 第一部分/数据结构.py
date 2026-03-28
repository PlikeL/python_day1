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
num = 200
while num >= 200 and num <= 250:
    num += 1
    if num % 2 == 0:
        print(f'{num} 是偶数')
