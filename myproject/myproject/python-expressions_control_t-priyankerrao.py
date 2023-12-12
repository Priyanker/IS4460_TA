a = True
b = False
print(a)  # Outputs: True
print(b)  # Outputs: False

true_value = int(True)
false_value = int(False)
print(true_value)  # Outputs: 1
print(false_value)  # Outputs: 0

# Here '42' is a literal.
number = 42
print(number)

# The order in which operations are processed: (), **, *, /, +, -
result = 10 + 2 * 3
print(result)  # Outputs: 16 (Multiplication is done first)

# Relational operators compare values
print(5 > 3)  # Outputs: True
print(5 < 3)  # Outputs: False

# Equality operator compares the value or equality of two objects
print("apple" == "apple")  # Outputs: True
print("apple" == "orange")  # Outputs: False

# Comparison operator compares two values
print(5 > 3)  # Outputs: True
print(5 < 3)  # Outputs: False

# IF statement to check a condition
age = 20
if age >= 18:
    print("You are an adult.")

temperature = 30
if temperature > 25:
    print("It's a warm day.")
else:
    print("It's not so warm today.")

score = 75
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'D'
print(f"Student grade: {grade}")

age = 20
access = "Granted" if age >= 18 else "Denied"
print(f"Access {access}.")
