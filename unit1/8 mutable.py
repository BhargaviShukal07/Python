#Write a program to explain mutable and immutable objects in Python.

# Mutable Object - List
list1 = [10, 20, 30]
print("Original list:", list1)

list1[0] = 100
print("After changing list:", list1)

# Immutable Object - Tuple
tuple1 = (10, 20, 30)
print("\nOriginal tuple:", tuple1)

# Trying to change a tuple element
# tuple1[0] = 100   # This will give TypeError

# Immutable Object - Integer
a = 10
print("\nOriginal value of a:", a)

a = 20
print("After changing a:", a)

print("\nConclusion:")
print("List is a mutable object because its values can be changed.")
print("Tuple and Integer are immutable objects because their values cannot be changed.")
