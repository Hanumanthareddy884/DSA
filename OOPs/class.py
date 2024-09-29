# Class declare

class Student:
    count=0
    def __del__(self):
        print("rdd","Destructor") # This is destructor is excute lastly and automatically call

    def registration(self):
        print("reddy","Reg method")


    def __init__(self,name,age) :
        self.name = name
        self.age = age
        print("redd","Constructor") #This is excute first in becuse its constructor and automatically call

    def __str__(self):
        self.registration()
        return f"{self.name}({self.age})"
    
std = Student("Atharva",2)
print(std)