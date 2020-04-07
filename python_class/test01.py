class Student:
    #驼峰命名
    count = 0
    def __init__(self,name,score):
        #self 必须为第一参数
        self.name = name
        self.score = score
        Student.count = Student.count+1
    def say_score(self):
        #self必须为第一参数
        print("{0}的分数是{1}".format(self.name,self.score))


S1 = Student("高琪",180)
S1.say_score()
S1.age = 30
S2 = Student("茅尧舜",100)
S3 = Student("xx",200)
print("一共创建{0}个Student对象".format(Student.count))


