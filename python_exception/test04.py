import traceback

#将异常保存到指定文件
try:
    print("step1")
    num = 1/0
except:
    with open("G:/a.txt","a") as f:
        traceback.print_exc(file=f)
