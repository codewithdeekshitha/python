'''Create a dictionary to store information about 5 cities in Karnataka and their famous dishes.
Add a new city and its dish to the dictionary.
Update the dish for Bengaluru.
Remove one city from the dictionary.
Use the keys() method to print all city names in the dictionary.
Use the values() method to print all dishes
'''
d={
    "bengaluru": "biryani",
    "mandya":"sugar cane",
    "mysuru": "mysur pak",
    "manglore": "fish",
    "goa": "enne"
}
d["tirupathi"]="ladoo" #adding mew item to d
print(d)

d["bengaluru"]="bennedose" #updating bengaluru
print(d)

d.pop("goa")#removinge one city
print(d)

print(d.keys()) #printing all keys of d
print(d.values()) #printing all values of d

'''Create a dictionary to store details of two of your friends, including their names, favorite subject, and favorite food.
Access and print the favorite food of one friend.
'''
friends={
    "name": "deekshitha",
    "fav sub": "maths",
    "fav food": "nonvej"
}
friends2={
    "name": "aishu",
    "fav sub": "accounts",
    "fav food": "vej"
    
}
print(f"aishu's fav food is :{friends2["fav food"]}")