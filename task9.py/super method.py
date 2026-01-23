#Super method:
class Car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car start")
    @staticmethod
    def stop():
        print("car stop")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        self.type=type
        super().start()
c1=ToyotaCar("prius","electric")
print(c1.type)        