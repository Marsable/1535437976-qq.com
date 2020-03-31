Salary =[]
sum = 0
num = 0
while num <4:
    salary = input("请输入薪资：")
    # if salary == "Q":
    #     print("录入成功")
    #     break;
    if float(salary)<0:
        print("输入错误，重新输入")
        continue;
    # if num >4:
    #     print("已全部录入4名员工的薪资")
    #     break;

    if num <4:
        # else:
        # num += 1
        Salary.append(float(salary))
        sum += float(salary)
    num += 1
print("已全部录入4名员工的薪资")
print(Salary)
print(sum/num)