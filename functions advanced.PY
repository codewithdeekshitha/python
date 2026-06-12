#functions advanced

 #variable length arguments
 
def add(*a): #*a is used bcz if u r calling a function and the positional arg is more than the parameter the *a is used 
     print(a) #type is tuple
add(1,2,23,456) 

def add(*numbers):
    return sum(numbers)    
print(add(2,3,4,1))

def student_info(**details): #**kwags :keyword arguments which is used to accept both keys and values 
    for key,values in details.items():
        print(f"{key}:{values}")
student_info(name="deekshitha",age=19,course="python")        

#lamda functions:  a lamda function is a small anonymous function that can take any number of  arguments but has only one expression

add = lambda a,b : a+b
print(add(2,3))    
 
double = lambda y: y*2
print(double(4)) 

students=[
    {"name":"deekshitha","marks":100},
    {"name":"darshan","marks":10}
]  

students.sort(key=lambda x: x["marks"],reverse=True)
print(students)

#recursion : it occurs when the function calls itself

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))

#nested function : it is a function defined inside another function.The inner function is only accessible within the outer function allowing more modular and controlled code execution

def calculate(a,b):
    def add():
        print(a+b)
    def sub():
        print(a-b)
    def mul():
        print(a*b)
    add()
    sub()
    mul()
calculate(10,20)
               
