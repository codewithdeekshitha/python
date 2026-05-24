#lists

items=["soup",1,True,[1,2,3],34.2] #it can be int,string,float,and other
print(items[-2]) #accessing
items.pop() #removes the last item
items.pop(0) #eemoves the first item
print(items)
items.append("snacks") #adds the item at the end
print(items)
items.remove(True) #to remove a particular item
print(items)
items.insert(1,"bru")#adds item to the particular pasition
items[0]="sunrise" #replaces the item in a particular index
print(items)
print(items.index("sunrise")) #0
print(items.count("bru")) #how many times the item ios repeated

#slicing of list
l=[1,2,4,3,5,6]
print(l[0:5:2]) #[start:stop:step]
#same as string slicing
print(len(l)) #prints how many characters are there in l
print(sorted(l)) #prints the sorther elemets in ascending order
print(sum(l)) #prints the sum of l

#nested list
m=[[0,1],[2,3]] #matrix format 
print(m[1][0])

