# tuples and sets

gender=("male","female","others","female") #bcz it cannot be changed
print(gender)
print(len(gender))
print(gender[1:])#indexing is there in tuple bcz it is ordered
print(gender.count("female")) #counts how many times particualar tuple is repeated
print(gender.index("female")) #index of particular tuple

#tuple concatenation
t1=(1,2,3)
t2=(4,5,6)
x=t1+t2
print(x*3) #tuple repetition
print(1 in t1) #checking membership

#sets
s={22,2,460}
print(s) #set is unordered and there is no indexing 
s2=set((1,2))#creating tuple inside set
print(type(s2))
#s3={} #dont lev empty like ths bcz it is dict instead write s=set()

s11={1,2,3}
s22={3,4,5}
print(s11 | s22) #union and pipe '|' symbol is used
print(s11 & s22) #intersection and '&'symbol is used
print(s11-s22) #difference

#set methods
s={1,2,3}
s.add(4)
#s.remove(10) it shows error so instead use
s.discard(10)
print(s)
print(s.pop()) #removes random element
print(s.clear())
 


































