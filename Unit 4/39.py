# Write data into a file
f = open("data.txt", "w")
f.write("Hello Bhargavi\n")
f.close()

# Append data
f = open("data.txt", "a")
f.write("Welcome to AI\n")
f.close()

# Read data
f = open("data.txt", "r")
print(f.read())
f.close()
