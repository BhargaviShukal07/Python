#Write a program to illustrate variable scope using local global and nonlocal variables.


x = 10       

def outer():
    y = 20   

    def inner():
        nonlocal y
        y = 30       
        z = 40       

        print("Global variable =", x)
        print("Nonlocal variable =", y)
        print("Local variable =", z)

    inner()
    print("Value of y after inner function =", y)

outer()

print("Global variable outside function =", x)