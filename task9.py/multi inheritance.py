#Multi-level inheritance:
class Car:
    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stop")
class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
c1=Fortuner("electric")
c1.start()
print(c1.type)                         