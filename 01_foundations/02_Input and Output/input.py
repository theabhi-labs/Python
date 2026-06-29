# input() user se input lene ke liye use hota hai.

name = input("enter your name")
print(name)

# input() hamesha string return karta hai.

# Integer Input
age = int(input("Enter age: "))

print(age)
print(type(age))

# Float Input
salary = float(input("Salary: "))

# Boolean Input
# Python me direct bool(input()) use nahi karna chahiye.
value = bool(input())
# Agar user False bhi likhe to output True aayega kyunki non-empty string truthy hoti hai.

value = input("Enter True or False: ")
is_valid = value.lower() == "true"
print(is_valid)

# Taking Multiple Inputs
name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")

print(name, age, city)

# Ek line me
a, b = input("Enter two numbers: ").split()
print(a)
print(b)

# Integers

a, b = map(int, input().split())
print(a + b)