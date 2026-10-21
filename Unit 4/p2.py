#Write a program to demonstrate constructor and destructor usage.

class Student:

  
    def __init__(self):
        print("Constructor is called")
        self.name = "Bhargavi"

    
    def __del__(self):
        print("Destructor is called")


    def display(self):
        print("Student Name:", self.name)


s1 = Student()


s1.display()


del s1