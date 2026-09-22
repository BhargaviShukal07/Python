#Write a program to find the sum of digits of a number using a while loop.

num=int(input("Enter a number :"))
total=0

while num>0:
    total += num%10
    num = num // 10
print("Sum of digit:",total)
