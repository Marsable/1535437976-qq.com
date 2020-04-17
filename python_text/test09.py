import csv

with open("x.csv", "r") as f:
    a = csv.reader(f)
    # print(list(a))
    for row in a:
        print(row)

with open("a.csv", "w") as f:
    b = csv.writer(f)
    b.writerow(["ID","姓名","年龄"])
    b.writerow
