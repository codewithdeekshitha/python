#operators

# 1. assigment operator
x=10
x+=100 #x=x+10 short form even for *,-etc
print(x) #peinting x=x+10

# 2.comparison operator
a=10
b=100
print(a==b) ##prints boolean value either true or false
print(a>b) #prints boolean value either true or false
print(a<b) ##prints boolean value either true or false
print(a!=b) #prints boolean value either true or false

# 3.logical operator
print(2>3 and 2<3) #if one is false then o/p is false
print(2>3 or 2<3) #if one true then o/p is true
print(not(2<3))

# 4.membership operator
list="python"
print("p" in list) #prints boolean value either true or false
print("b" not in list) #prints boolean value either true or false

#using logical in membership operator
s1="darshan"
s2="deekshitha"
print(("d" in s1)and("z" in s2)) #prints boolean value either true or false 
print(("d" in s1)or("z" in s2))  #prints boolean value either true or false
print(not("d" in s1))

# 5.bitwise operator
a=2 #binary value:010
b=5 #binary value:101
print(a&b)
print(a|b)
