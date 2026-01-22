#Parameterized constructor.
class Students:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database")
s1=Students("Laiba") 
print(s1.name)
s2=Students("Emaan") 
print(s2.name)
s3=Students("Mehwish")
print(s3.name)      