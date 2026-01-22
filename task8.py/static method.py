#Static method.
class Student:
    def __init__(self,name):
        self.name=name
    @staticmethod
    def hello():
        print("hello")
s1=Student("Laiba")        
s1.hello()






