#Write a program to illustrate method resolution order and magic methods

class A:
    def show(self):
        print("Method from class A")


class B(A):
    def show(self):
        print("Method from class B")


class C(A):
    def show(self):
        print("Method from class C")


class D(B, C):
    pass


# Method Resolution Order (MRO)
obj = D()

print("Method Resolution Order:")
print(D.mro())

print("\nCalling show() method:")
obj.show()


# Magic methods
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"


student = Student("Rahul", 20)

print("\nMagic Method __str__():")
print(student)
