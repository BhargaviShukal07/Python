#Write a program to demonstrate the use of break continue and pass statements.

#break
for i in range(1,6):
    if i==3:
        break
    print(i)

#continue

for i in range(1,6):
    if i==4:
        continue
    print(i)

#Pass statement
for i in range(1,6):
    if i==2:
        pass
    print(i)
