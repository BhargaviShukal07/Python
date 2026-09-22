import os
import sys

# Display current working directory
print("Current Directory:", os.getcwd())

# Create a directory
folder = "MyFolder"

if not os.path.exists(folder):
    os.mkdir(folder)
    print("Directory created:", folder)
else:
    print("Directory already exists:", folder)

# Create a file inside the directory
file_path = os.path.join(folder, "sample.txt")

with open(file_path, "w") as file:
    file.write("Hello, this is a sample file.")

print("File created:", file_path)

# Check whether file exists
if os.path.exists(file_path):
    print("File exists.")

# Display directory contents
print("Directory contents:", os.listdir(folder))

# Display command-line arguments
print("Command-line arguments:", sys.argv)

# Display Python version
print("Python Version:", sys.version)
