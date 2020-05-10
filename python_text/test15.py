import os

allfile = []
def getAllFiles(path,level):
    chiledFiles = os.listdir(path)
    for file in chiledFiles:
        # print(file)
        filepath = os.path.join(path,file)
        if os.path.isdir(filepath):
            getAllFiles(filepath,level+1)
        allfile.append("\t"*level+filepath)

getAllFiles("./",0)