# This is how you write a comment in Python. It's ignored by the interpreter.
# print("This line is commented out and won't run.")

# String literal
print("Hello, World!")

# Integer literal
print(42)

# Float literal
print(3.14159)

# Boolean literal
print(True)


first_name = "Luke"
last_name = "Skywalker"
age = 19
force_sensitive = True

# Print the variables
print(first_name)
print(last_name)
print("Age:", age)
print("Force Sensitive:", force_sensitive)

# Variable assignment
character_name = "Darth Vader"  # A string variable
lightsaber_color = "red"  # Another string variable
empire_rank = "Sith Lord"  # And another string variable

# Print the variables
print("Character Name:", character_name)
print("Lightsaber Color:", lightsaber_color)
print("Empire Rank:", empire_rank)


# String concatenation example
greeting = "Hello"
name = "Han Solo"
message = greeting + ", " + name + "! Welcome back to the Millennium Falcon."

# Print the concatenated string
print(message)  # Output: Hello, Han Solo! Welcome back to the Millennium Falcon.



# String concatenation using f-strings for better readability
name = "Leia"
title = "Princess"
greeting = f"Hello, {title} {name}!"
print(greeting)


# Converting an integer to a string and slicing
big_number = 123456789
first_five_digits = str(big_number)[:5]
print(f"The first five digits are: {first_five_digits}")


# Function with parameters to calculate the area of a rectangle
def calculate_area(width, height):
    return width * height

# Call the function with positional and named arguments
area = calculate_area(5, 3)
print(f"The area is: {area}")

# Named arguments can be out of order
another_area = calculate_area(height=8, width=2)
print(f"Another area: {another_area}")

# A function to say hello
def say_hello(username):
    message = f"Welcome, {username}!"
    return message

# Call the function and print the result
user_greeting = say_hello("Chewbacca")
print(user_greeting)
