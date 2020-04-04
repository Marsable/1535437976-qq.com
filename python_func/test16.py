def printName(isChinese,name,familyName):
    #第一位则是函数名，后面为变量
    def inner_print(a,b):
        print("{0}{1}".format(a,b))

    if isChinese:
        inner_print(familyName,name)
    else:
        inner_print(name,familyName)

printName(True,"尧舜","茅")
printName(False,"mys","MYS")