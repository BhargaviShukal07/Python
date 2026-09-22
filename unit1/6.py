#Write a program to illustrate the use of tuples and sets with basic operations.

#tuple
fruits = ("Apple","Mango","Kiwi")
print(fruits)
print("First Element:", fruits[1])
print("Len of tuple",len(fruits))


#SET
fruits= {"Apple", "Mango" , "Kiwi"}
print("Orignial set :", fruits)

#add
fruits.add("orange")
print(fruits)

# Remove an element
fruits.remove("Apple")
print("After Remove:", fruits)
