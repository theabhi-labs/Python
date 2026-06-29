# Python 3.6+ ka sabse recommended method.

# f"text {variable}"

Name = "Abhishek"
print(f"My Name is {Name}")

# Multiple Variables

name = "Abhishek"
age = 20
print(f"My name is {name} and I am {age} years old.")

# Expressions
a = 10
b = 20

print(f"Sum = {a + b}")

# Formatting Decimal
pi = 3.14159265

print(f"{pi:.2f}")

# Padding
num = 7
print(f"{num:05}")

# Alignment
word = "Python"

print(f"|{word:<10}|")
print(f"|{word:^10}|")
print(f"|{word:>10}|")