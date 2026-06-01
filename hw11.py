#Write a for loop that prints all multiples of 3 between 1 and 30.

for i in range(1,31):
    print(f"3X{i}={3*i}")
    
#Write a program using a for loop that calculates the sum of numbers from 1 to 10.

sum=0
for i in range(1,11):
    sum+=i
print("sum=",sum)      

#Write a program that takes your name as input and prints each letter of your name using a for loop.

name=input("enter your name:")
for letter in name:
    print(letter)
 
#Write a program that counts how many vowels are in a given string using a for loop.
  
text = input("enter a string:")
count = 0
for ch in text:
    if ch.lower() in "aeiou":
        count += 1

print("Number of vowels =", count)    