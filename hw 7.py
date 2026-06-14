'''Tuple Operations:

Create a tuple with 5 elements.
Try to modify one of the elements. What happens?
Perform slicing on the tuple to extract the second and third elements.
Concatenate the tuple with another tuple.
'''
t=(10,20,30,40,50) #creating tuple
t[0]=100 #it is not possiblle bcz tuples are immutable
print(t[1:3])
t1=(60,10) #it just concatinates with t so o/p=10,20,30,40,50,60,10
print(t+t1)

'''Set Operations:

Create two sets: one with your favorite fruits and another with your friend’s favorite fruits.
Find the union, intersection, and difference between the two sets.
Add a new fruit to your set.
Remove a fruit from your set using both remove() and discard(). What happens when the fruit doesn’t exist?
'''
s1={"apple","banana","goa"} #creating set
s2={"orange","kiwi","dragon"}
print(s1 | s2) #uniopn 
print(s1 & s2) #and 
print(s1-s2) #difference
s1.add("licchi")
print(s1)
s1.discard("kiwi")
print(s1)

'''Tuple and Set Comparison:

Create a list of elements and convert it into both a tuple and a set.
Print both the tuple and the set.
Try to add new elements to the tuple and set. What differences do you observe?
'''
l=[1,2,3,4]
s=set(l)
t=tuple(l)
print(s,t)
s.add(5)
#we cannot add anything or remove from tuple bcz it is immutable
