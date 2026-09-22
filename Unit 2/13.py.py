#Write a program to generate a multiplication table using a for loop.

num=(int(input("Enter Number:")))

for i in range(1,11):
    print(num,"*",i,"=",num*i)
