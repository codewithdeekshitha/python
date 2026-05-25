# if-elif-else

x=10
if x==10:
    print("yes x is 10")
    
x=19
if x%2==0:
    print("x is an even number")
else:
    print("x is an odd number")
    
signal=input("enter the colour of signal: ")
if signal=="red":
    print("stop")
elif signal=="yellow":
    print("ready")
else:
    print("go")    
    
#logical operators in if statements
att=75
is_teacher_friend=True
if att<=65 or is_teacher_friend:
    print("exam is given")
else:
    print("no exam is given")    
    
#checking bus ticket

gender=input("enter your gender>> ")
age=int(input("enter your age>> "))
is_conductor_frnd=True
if gender=="female":
    print("ticket is free")
else:    
    if age>=65 and is_conductor_frnd:
        print("u get a free ticket")
    elif age<=5:
        print("u get a half ticket")
    else:
        print("you should pay a full fare")                   
