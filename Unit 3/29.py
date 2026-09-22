import re

text = "Python is easy. Python is powerful. I love Python."

# 1. match()
result = re.match(r"Python", text)

if result:
    print("match(): Pattern found at the beginning")
    print("Matched:", result.group())
else:
    print("match(): Pattern not found")


# 2. search()
result = re.search(r"powerful", text)

if result:
    print("search(): Pattern found")
    print("Matched:", result.group())
else:
    print("search(): Pattern not found")


# 3. findall()
result = re.findall(r"Python", text)

print("findall(): All matches:", result)
print("Number of matches:", len(result))
