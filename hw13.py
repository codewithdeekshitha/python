# Greet Function: Write a function greet() that takes no arguments and prints a greeting message.

def greet():
    print("hello world!")
greet()

# parameterized Greet: Write a function greet_user() that takes a name as input and prints a custom greeting.   

def greet(name):
    print(f"hello {name}! welcome to my home")
    
greet("darshan")    

# Sum Function: Write a function add_numbers(a, b) that returns the sum of two numbers. Call this function with different values.

def add_num(a,b):
    return a+b

print("sum =", add_num(10, 20))
print("sum =", add_num(5, 5))