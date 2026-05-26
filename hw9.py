'''Write a program to check if someone is eligible for a bus pass. If they are below 5 years, the bus pass is free. If they are 60 years or older, they get a senior citizen discount. Otherwise, they pay the full price.
'''
age=int(input("enter your age>> "))
if age<5:
    print("bus pass is free")
elif age>=60:
    print(" you get a senior citizen discount") 
else:
    print("you pay a full price")
    
'''Create a program that checks the time of day (24-hour format) and prints whether it's time for breakfast, lunch, or dinner.
Breakfast: 8 AM
Lunch: 1 PM
Dinner: 8 PM
If none of these times, print "It's not meal time."
'''
time=int(input("enter the time in 24 hr format>> "))
if time==8:
    print("its breakfast time")
elif time==13:
    print("its lunch time")
elif time==20:
    print("its dinner time")
else:
    print("its not a meal time")   
    
'''Write a program that checks whether a person is eligible for a library membership. If they are under 18, they get a student membership. If they are 60 or older, they get a senior citizen membership. Otherwise, they get a regular membership.
'''
age=int(input("enter your age>> "))
if age<18:
    print("you get a student membership") 
elif age>=60:
    print("you get a senior citizen membership ")        
else:
    print("you get a regular membership")                 