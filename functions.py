#functions: it is a reusable block of code that performs a  specific task when called.functions are useful to organize code,make it reusable and reduce redundancy

def greet(): #defining function
    print("hello good morning")
    
greet() #calling function

#function parameters: parameters are variable used to pass data into a function

def marriage(boy,girl="trading"): #parameters
    print(f"boy is {boy}")
    print(f"girl is {girl}")
    print(f"{boy} marries {girl}")
marriage("darshan","deekshitha") #positional arguments
marriage("darshan","me")
marriage(boy="darshi",girl="deekshi") #keywords arguments
marriage("darshan")#girl is not called so default parameter is used and it is specifed in parameters so it is called as default

def tables(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
        
tables(2)
tables(5)

#returning value from a function

def func(num):
    return int(str(num)*3)
a=100
b=func(2)
c=a + b
print(c)

#local and global variable
def func():
    x="chandan" #local var
    print("hello world")
    print(y)
y="darshan" #global var

print(y)        