#工厂模式
class CarFactory:
    def create_car(self,brand):
        if brand == "奔驰":
            return Benz
        elif brand =="宝马":
            return BMW()
        elif brand == "比亚迪":
            return BYD()
        else:
            return "不是品牌"
class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

m = CarFactory()
x = m.create_car("宝马")
print(x)