# Generator function
def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

# Main program
limit = int(input("Enter the limit: "))

print("Generated sequence:")
for num in generate_numbers(limit):
    print(num)
