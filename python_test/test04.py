# 定义发动机类 Motor、底盘类 Chassis、座椅类 Seat，车辆外壳类 Shell，并使用组合
# 关系定义汽车类。其他要求如下：
# 定义汽车的 run()方法，里面需要调用 Motor 类的 work()方法，也需要调用座椅类 Seat 的 work()方法，也需要调用底盘类 Chassis 的 work()方法。
class Car:
    def __init__(self,motor,seat,chassis):
        self.motor = motor
        self.seat = seat
        self.chassis = chassis
    def run(self):
        self.motor.work()
        self.seat.work()
        self.chassis.work()
        print("走你！")
class Motor:
    def work(self):
        print("发动机")
class Chassis:
    def work(self):
        print("底盘")
class Seat:
    def work(self):
        print("座位")
class Shell:
    pass

c1 = Car(Motor(),Chassis(),Seat())
c1.run()
