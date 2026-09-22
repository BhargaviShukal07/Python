 #Write a program to demonstrate recursion using factorial or Fibonacci series. 

 # Program to demonstrate recursion using factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number: "))

result = factorial(num)

print("Factorial of", num, "=", result)