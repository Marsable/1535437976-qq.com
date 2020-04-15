#coding = utf-8
def Exception():
    try:
        a = input("请输入除数")
        b = input("请输入被除数")
        c = float(a)/float(b)
        # return 1
    except ZeroDivisionError:
        print("被除数不能是0")
        return 1
    except BaseException as e:
        print(e)
        return 1
    else:
        print(c)
        return 1
    finally:
        print("无论发生什么")
        return 1
Exception()