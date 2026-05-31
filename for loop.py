#for loop

for i in range(1,11):
    print(i,end=" ")
print()
    
    
bag=["book","pen","eraser","pencil"]
for item in bag:
    print(item,end=" ") 
print()   
    
for i in range(1,11,2): #[start,stop,step]
    print(i,end=" ")
print()       
    
#looping over strings   

name="deek"
for index, letter in enumerate(name): #here index,letter in called unpacking
    print(letter*(index+1))
    
l=[2,3,4,5]
for index,num in enumerate(l):
    print(f"{num} is in {index}th index")

for num in l:
    print(num,end=" ")
    if num == 4:
        break         
else:
    print("all printed")   #else is not printed bcz break is there so the loop is broken
print()     

#using for loop in dict

d={"name": "darshan", "age": 19, "salary":100000}
for key,value in d.items():
    print(key," ",value)    
    
#nested loops
for i in range(2,11):
    for j in range(1,11):
        print(f"{i}X{j}={i*j}")
