#super()

class A:
    def say(self):
        print("A",self)

class B(A):
    def say(self):
        # A.say(self)
        super().say()
        print("B",self)

B().say()