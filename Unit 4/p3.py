#Write a program to illustrate instance variables and class variables.

class Student:

    
    college = "Marwadi University"

    def __init__(self, name, rollno):
        
        self.name = name
        self.rollno = rollno

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("College:", Student.college)



s1 = Student("Bhargavi", 101)
s2 = Student("Keval", 102)


s1.display()
print()

s2.display()