#Create student class that takes name & marks of 3 subjects as argumented in constructor.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
            print("Avg of your marks is:",sum/3)

s1=Student("Laiba",[98,87,84]) 
s1.get_avg()       