#Write a program to define and use user-defined functions with different types of arguments.

# User-defined functions with different types of arguments

# 1. Positional Arguments
def add(a, b):
    print("Addition =", a + b)

add(10, 20)


# 2. Keyword Arguments
def student(name, age):
    print("Name =", name)
    print("Age =", age)

student(age=20, name="Bhargavi")


# 3. Default Arguments
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Bhargavi")


# 4. Variable-Length Arguments (*args)
def total(*numbers):
    print("Total =", sum(numbers))

total(10, 20, 30, 40)


# 5. Keyword Variable-Length Arguments (**kwargs)
def details(**data):
    for key, value in data.items():
        print(key, "=", value)

details(name="Bhargavi", age=20, course="BCA")