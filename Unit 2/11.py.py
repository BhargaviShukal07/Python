#Write a program to demonstrate conditional statements using if if-else and if-elif-else.

num =(int(input("Enter number:")))

if num>0:
    print("number is positive")

#if else statement
    if num%2==0:
        print("Number is even")
    else:
        print("Number is odd")

#if-elif-else statement

        marks=(int(input("Enter  Marks:")))

        if marks>=90:
            print("Grade A")
        elif marks>=75:
            print("Grade B")
        elif marks>=50:
            print("Grade C")
        else:
            print("Fail")
