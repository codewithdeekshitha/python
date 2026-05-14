#Simple Greeting Program: Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
name=input("enter your name: ")
age=input("enter your age: ")
print(f"hello {name}! you are {age} years old")



#String Manipulation Exercise: Write a Python program that:

'''Takes a sentence as input from the user.
Prints the sentence in all uppercase and lowercase.
Replaces all spaces with underscores.
Removes leading and trailing whitespace.'''

sentence=input("enter a sentence: ")
print(sentence)
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ","_"))
print(sentence.strip()*2)

#Asks the user for a string.
#Prints how many characters are in the string, excluding spaces.
text=input("enter a string: ")
a=text.replace(" ","")
b=len(a)
print("number of characters(excluding space ): ",b)

n="hello \n\tworld "
print(n)