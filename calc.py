while True:
    sz=int(input("请输入一个数字："))
    if sz > 10:
        print("数字太大了!")
    elif sz < 10:
        print("数字太小了!")
    elif sz == 10:
        print("数字刚刚好!")
        break