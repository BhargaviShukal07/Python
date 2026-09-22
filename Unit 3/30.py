import re

# Read text file
with open("data.txt", "r") as file:
    text = file.read()

# Extract email addresses
emails = re.findall(r'[\w.-]+@[\w.-]+\.\w+', text)

# Extract phone numbers
phones = re.findall(r'\b\d{10}\b', text)

# Display extracted information
print("Email Addresses:")
for email in emails:
    print(email)

print("\nPhone Numbers:")
for phone in phones:
    print(phone)
