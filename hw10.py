#write a program that counts from 1 to 10 using a while loop.

i=1
while i<=10:
    print(i,end=" ")
    i=i+1

#Create a program that prints all odd numbers between 1 and 20 using a while loop.

i=1
while i<=20:
    if i%2==0:
        i=i+1
        continue
    print(i,end=" ")
    i=i+1
    
'''Write a program that simulates a bus ticket booking system. The bus has 8 seats. Each time a seat is booked, the available seats decrease. When there are no seats left, the loop stops and displays a message saying "All seats are booked."  
'''  
seats=8
while seats>0:
     print("available seats:",seats)
     
     book=input("book a seat (yes/no):")
    
     if book == "yes":
        seats=seats-1
        print("booked successfully!")
     elif book == "no":
        print("booking cancelled") 
     else:
        print("invalid input,please  enter (yes/no)")       
   
if seats == 0:
     print("no seats are available")   
     
'''Write a program that counts down from 10 to 1 using a while loop and prints "Happy New Year!" after the countdown is over.'''

import time
count = 10

while count >= 1:
    print(count)
    time.sleep(1) #make the control to wait for 1 sec and then continue
    count -= 1

print("Happy New Year!")               
