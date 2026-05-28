#while loop

is_failed=True
i=1 #attempt 
while is_failed :
    if i%2!=0:
        i=i+1
        continue #does not execute next set of code,goes back to the loop
    print(f"try {i} ")
    i=i+1
    if i>10:
        break #breaks the loop
    
print("better luck next time")    

is_failed=True
i=1
while is_failed and i<=10:
    print(f"try {i} ")
    i=i+1 
print("better luck next time") 
 

i=0
while i<=10:
    x=0
    while x<i:
        print("deek",end=" ")
        x+=1
print("")  
i+=1

pin="2024"
trials=1
while trials<=3:
    input_pin=input(f"trial-{trials} | pin ")
    trials+=1
    if input_pin==pin:
        print("correct")
    else:
        print("incorrect")    
    