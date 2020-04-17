import os
from os import path

# print(path.isabs())
path = os.getcwd()
list_file = os.walk(path)
# print(list(list_file))
for dirpath,dirname,filename in list_file:
    for dir in dirname:
        print(os.path.join(dirpath,dir))
    for file in filename:
        print(os.path.join(dirpath,file))
