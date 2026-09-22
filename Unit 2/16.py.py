# Write a program to demonstrate iterators and iterables in Python.

# Iterable
fruits = ["banana", "mango", "cherry"]

print("Iterable:")

for n in fruits:
    print(n)

# Creating an Iterator
iterator = iter(fruits)

print("\nIterator:")

print(next(iterator))
print(next(iterator))
print(next(iterator))