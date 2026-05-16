first_name="deekshitha"
last_name="darshan"
full_name=first_name + " " + last_name #for space
print(full_name) 

#repetition
message="warning "
print(message*5) 

#string method
message="good morning! "
print(message.upper())#prints in capital letters
print(message.lower())#prints in small letters
print(message.strip()*3)#prints the output without space
print(message.replace("morning","night"))#replces a particualar string

name='''darshan said me "hi"
i said "hello"
    '''
print(name)    

message="hello hi"
print(len(message))#to count the number of characters including space

#accessing string
name="python"
print(name[1])

#string slicing
print(name[1:6])
print(name[:6])
print(name[-2]) #from reverse order
print(name[::2]) #[start:stop:step]

#escape sequence
name="darshan is \na good boy" #for next line
print(name)
name="darshan is \ta good boy" #for tab space
print(name)