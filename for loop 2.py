#for loop in lists

l=[1,23,43,534,32]
total = 0
for num in l:
    print(total,end=" ")
    total+=num #total=total+num
print(total)    
    
l=[1,23,43,534,32]
dl=[]
for num in l:
    dl.append(num*2) #append=list method used to add one item at the end of a list
    print(dl)    

d={"aishu": 23,"deek":24, "darshi": 25} #for loop in dictionary
for student,marks in d.items(): #items is used when u want both keys and values
    print(f"{student} = {marks}")

#for loop in range

students=["deekshitha","aishu","darshan"]
marks=[30,40,50]
student_marks={}
for index,student in enumerate(students): #enumerate prints the index as well as the value of the index 
    student_marks[student]=marks[index]
print(student_marks)    

#easy method
students=["deekshitha","aishu","darshan"]
marks=[30,40,50]
student_marks={}
for i in range(3):
    student_marks[students[i]] = marks[i]
print(student_marks) 

#list comprehension    
l=[1,2,3,4,5]
#dl=[expression for item in c0llection]
dl=[item*2 for item in l]    
print(dl)    

l=[x for x in range(1,11)]
print(l)
dl=[x**2 for x in l if x%2==0] #to print even expressions 
print(dl)

#list comprehension on strings
l=["deekshitha","darshan"]
cl=[x[1] for x in l] #to access the letter of that position
print(cl)

#dictionary comprehnsion
names=["deekshitha","darshan"]
d={name:len(name) for name in names}
print(d)

cp={
    "bengaluru": 65,
    "mysuru": 11,
    "goa":22,
    "pondi":2
    }
lc={key:values for key,values in cp.items() if values>10}
print(lc)

#string split
s="this is human"
l=s.split() #converts every words into list
print(l)

x=input("enter a list of integer: ").split()
l=[int(num) for num in x]
print(l)
