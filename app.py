# This is a sample Python code that demonstrates a few basic concepts.

# 1. Printing a string
print("Hello, world!")

# 2. Defining variables and performing calculations
name = "Alice"
age = 30
year_of_birth = 2023 - age

print(f"My name is {name} and I was born in {year_of_birth}.")

# 3. Using a loop to iterate through a list
fruits = ["apple", "banana", "cherry"]

print("My favorite fruits are:")
for fruit in fruits:
    print(fruit)

# 4. Defining a function
def greet(person):
    return f"Hello, {person}!"

greeting = greet("Bob")
print(greeting)

# 5. Conditional statement (if/else)
temperature = 25

if temperature > 20:
    print("It's a warm day.")
else:
    print("It's a bit chilly.")

# 6. Working with user input
city = input("Enter your favorite city: ")
print(f"So, you like {city}!")


# 7.  A slightly more complex example: calculating the factorial of a number.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")


# 8. Demonstrating a try-except block for error handling

try:
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")