while True:
    try:
        x = int(input("请输入一个数字"))
        print("请输入数字",x)
        if x ==88:
            print("退出程序")
            break
    except BaseException as e:#产生异常对象
        print("出现异常")
        print(e)



print("循环结束")