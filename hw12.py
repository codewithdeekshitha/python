#Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

l = ["dose","upitu","idli","payasa","bath"]
nl = [food.upper() for food in l]
print(nl)

#Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop

d={"rice": 300,
   "sugar": 100,
   "dal": 40,
   "chips": 50,
   "box": 150
   }

print(sum([price for price in d.values()]))

#Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.

students=[{"name": "Deekshitha", "age": 20, "marks": 85},
    {"name": "Aishu", "age": 21, "marks": 90},
    {"name": "Darshan", "age": 20, "marks": 88}]

for student in students:
  print(f"Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

#another method
for student in students:
   print(student["name"] "=" student["marks"])   

#Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.

d={"bengaluru": 100000000,
   "mangaluru": 54,
   "raichur": 33,
   "mysuru": 28
   }
print({key: values for key,values in d.items() if values<1000000})

#Write a Python program that takes a list of lists (a 2D list) as input and:

#Prints the entire matrix row by row.
#Prints the sum of each row in the matrix.

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in m:
    print(row)
print("\n the sum of  each row is:")  
for row in m:
    print(sum(row))  
