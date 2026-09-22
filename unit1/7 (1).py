#Write a program to create a dictionary and demonstrate dictionary methods and iteration.

# Creating a dictionary
student = {
    "name": "Bhargavi",
    "age": 20,
    "course": "MCA",
    "marks": 85
}

print("Original Dictionary:")
print(student)

# keys() method
print("\nKeys:")
print(student.keys())

# values() method
print("\nValues:")
print(student.values())

# items() method
print("\nKey-Value pairs:")
print(student.items())

# get() method
print("\nName:", student.get("name"))

# update() method
student.update({"marks": 90})
print("\nAfter update():")
print(student)

# Adding a new key-value pair
student["city"] = "Rajkot"
print("\nAfter adding city:")
print(student)

# pop() method
student.pop("age")
print("\nAfter pop('age'):")
print(student)

# Iterating through dictionary
print("\nIterating through dictionary:")

for key, value in student.items():
    print(key, ":", value)

# Checking if a key exists
if "name" in student:
    print("\n'name' key exists in the dictionary.")

# Length of dictionary
print("\nLength of dictionary:", len(student))
