class Student:
    #驼峰命名

    def __init__(self,name,score):
        #self 必须为第一参数
        self.name = name
        self.score = score

    def say_score(self):
        #self必须为第一参数
        print("{0}的分数是{1}".format(self.name,self.score))


S1 = Student("高琪",18)
S1.say_score()


S1.age = 30


