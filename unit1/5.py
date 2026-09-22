#Write a program to create and manipulate lists using indexing slicing and list comprehensions.

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

#indexing
print("First element:", numbers[0])
print("Last element:", numbers[4])

#slicing
print(numbers[0:4])
print("Reverse List:", numbers[::-1])
print("Reverse List:", numbers[-3::-1])

#append
numbers.append(60)
print(numbers)

#remove
numbers.remove(10)
print(numbers)

#pop
numbers.pop(3)
print(numbers)
