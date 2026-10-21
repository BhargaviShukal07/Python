#Write a program to implement single multilevel and multiple inheritance.

# -------------------------------
# 1. Single Inheritance
# -------------------------------

class Parent:
    def show_parent(self):
        print("This is Parent class")


class Child(Parent):
    def show_child(self):
        print("This is Child class")


print("Single Inheritance:")
obj1 = Child()
obj1.show_parent()
obj1.show_child()


# -------------------------------
# 2. Multilevel Inheritance
# -------------------------------

class GrandParent:
    def show_grandparent(self):
        print("This is GrandParent class")


class Parent2(GrandParent):
    def show_parent2(self):
        print("This is Parent class")


class Child2(Parent2):
    def show_child2(self):
        print("This is Child class")


print("\nMultilevel Inheritance:")
obj2 = Child2()
obj2.show_grandparent()
obj2.show_parent2()
obj2.show_child2()


# -------------------------------
# 3. Multiple Inheritance
# -------------------------------

class Father:
    def show_father(self):
        print("This is Father class")


class Mother:
    def show_mother(self):
        print("This is Mother class")


class Son(Father, Mother):
    def show_son(self):
        print("This is Son class")


print("\nMultiple Inheritance:")
obj3 = Son()
obj3.show_father()
obj3.show_mother()
obj3.show_son()