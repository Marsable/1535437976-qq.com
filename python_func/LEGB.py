#测试LEGB
str = "global str"
def outer():

    str = "outer"
    def inner():
        #先内后外
        # str = "inner"

        print(str)
    inner()

outer()