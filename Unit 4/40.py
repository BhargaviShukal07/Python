f = open("data2.txt", "w+")
f.write("Hello Bhargavi")

print("Position:", f.tell())

f.seek(0)
print("Data:", f.read())

f.seek(6)
print("Position:", f.tell())
print("Data:", f.read())

f.close()
