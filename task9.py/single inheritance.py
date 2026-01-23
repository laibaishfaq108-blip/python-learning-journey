#Single inheritance:
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name
c1=ToyotaCar("Fortuner")
c2=ToyotaCar("Prius")
print(c1.name)
print(c2.name) 
print(c1.stop())                   