#Write a program to demonstrate instance methods class methods and static methods.

class Student:

    # Class variable
    college = "Marwadi university"

    # Constructor
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    # Instance Method
    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)

    # Class Method
    @classmethod
    def show_college(cls):
        print("College:", cls.college)

    # Static Method
    @staticmethod
    def message():
        print("Welcome to Python Programming")


# Create object
s1 = Student("Bhargavi", 101)

# Calling Instance Method
s1.display()

# Calling Class Method
Student.show_college()

# Calling Static Method
Student.message()