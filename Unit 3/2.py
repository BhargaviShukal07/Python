#Write a program to illustrate the use of different data types and type casting.

# Different data types
integer_value = 10
float_value = 12.5
string_value = "Python"
boolean_value = True
complex_value = 3 + 4j

print("Integer:", integer_value)
print("Float:", float_value)
print("String:", string_value)
print("Boolean:", boolean_value)
print("Complex:", complex_value)

# Type casting
num = "25"

print("\nOriginal value:", num)
print("Type:", type(num))


num_int = int(num)
print("After converting to integer:", num_int)
print("Type:", type(num_int))


num_float = float(num_int)
print("After converting to float:", num_float)
print("Type:", type(num_float))


num_str = str(num_int)
print("After converting to string:", num_str)
print("Type:", type(num_str))