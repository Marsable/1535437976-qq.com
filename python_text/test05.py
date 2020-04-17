# a = ["我爱你\n","中国\n"]
# b = enumerate(a)#枚举每个元素
# print(a)
# print(list(b))
with open(r"G:\a.txt","r") as f:
    lines = f.readlines()
    lines = [line.rstrip()+"#"+str(index) for index,line in enumerate(lines)]
with open(r"G:\a.txt","w") as f:
    f.writelines(lines)