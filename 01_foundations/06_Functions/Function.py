def greet():
    print("Hello")
    print("Welcome to Python")

greet()    


# function with parameters
def greet(name):
    print(f"Hello {name}")
greet("Abhishek")    
greet("Monu")

# Multiple Parameters

def add(a, b):
    print(a + b)
add(10, 20)

# Return Statement
def add(a, b):
    return a + b

result = add(10, 5)
print(result)



def square(num):
    return num * num

ans = square(6)
print(ans)

# Default Parameters

def greet(name="guest"):
    print(f"Hello {name}")

greet()
greet("Abhi")    

# Keyword Arguments

def student(name, age):
    print(name, age)

student(age=20, name="Abhishek")    

# Variable Scope -> Local Variable

def demo():
    x = 10
    print(x)

demo()

# Global Variable

x = 100

def demo():
    print(x)

demo()

# Lambda Function (Short Function)
square = lambda x: x * x

print(square(5))

# Recursion

def countdown(n):
    if n == 0:
        return

    print(n)
    countdown(n-1)

nums = [10, 20, 30, 40]

for index, value in enumerate(nums):
    print(index, value)