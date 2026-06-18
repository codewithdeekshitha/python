#dictionary

birthday={                   #dictionary
    "darshan": "24-11-2006",    #key: value
    "deekshitha": "20-03-2007", #key: value
    "aishu": "17-11-2008"       #key: value
}
meaning={
    "pen": "used to write",    #key: value
    "books": "used to read",   #key: valu 
    "chair": "used to sit"     #key: value
}
print(birthday["darshan"]) #accessing dictionary
print(birthday.get("aishu"))
print(birthday.get("shwetha","not found")) #for safe accessing
birthday["prasad"]="20-07-1978" #adding value in run time
print(birthday)
birthday["deekshitha"]="20-03-2003" #updating the value
print(birthday)
birthday.pop("aishu") #to remove particular data use key
print(birthday)
del birthday["deekshitha"] #another way of deleting
print(birthday)

#dictionary methods
print(birthday.keys()) #to get only keys
print(birthday.values()) #to get only valuess
print(birthday.items())

new_item={"bed": " used to sleep"}
meaning.update(new_item)
print(meaning)
 #list cannot be used in dict but we can use int,string,float,boolean
 
d1={
     "name": "sugar",
     "weight": 1,
     "price": 50
 }
d2={
     "name": "ghee",
     "weight": 2,
     "price": 150
 }
print(f"total weight:{d1["weight"]+d2["weight"]}")#to get the total weight from d1 and d2
