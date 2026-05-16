"""Logical Operator Practice: Write a Python program that takes two numbers as input from the user and checks if:
'''
Both numbers are greater than 10 (using and).
At least one of the numbers is less than 5 (using or).
The first number is not greater than the second (using not).
'''
num1=int(input("enter num1: "))
num2=int(input("enter num2: "))
print((num1>10)and(num2>10))
print((num1<5)and(num2<5))
print(not(num2>10))

'''Comparison Operator Challenge: Create a Python program that asks the user for their age and prints:

"You are an adult" if the age is greater than or equal to 18.
"You are a minor" if the age is less than 18.
Use >= and < comparison operators.'''
age=int(input("enter your age>> "))
if age>=18:
    print("you are adult")
if age<18:
    print("you are minor")
    
'''Takes a string as input from the user.
Checks if the letter 'a' is in the string (using in).
Checks if the string doesn't contain the word "Python" (using not in).
'''

x=input("enter a string: ")
if "a" in x:
    print("a is present in string")
else:
    print("a is not in the string") 
if "python" in x:
    print("python is in the string")
else:
    print("python is not in the string" )"""
    
a=3 #011
b=2 #010
print(a&b) #010
print(a|b) #011             
    
    