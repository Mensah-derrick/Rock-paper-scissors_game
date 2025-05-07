name = "Kwame"
print(name)
print(len(name))
print("we" in name) #this is for finding the truth of string values in strings
name= 'Be\nau' #\n is for creating a new line
print(name)

note= 'beau'
print(name[0]) #For finding specific characters in strings. Its called indexong
print(name[1:3]) #this is called slicing
print(name[:2])

#Booleans 
done = True
if done:  #bools can be used with if statements
    print("Yes")
else:
    print("No")
#all nummbers will return true but if it is empty, it will return false
#you can replace done with "" or "beau" to check
book_red= True
book_green = False
book= any([book_red, book_green])
book= all([book_red, book_green])

#Number data types
#complex
num1= 2+3j
num= complex(2,3)
print(num.real, num.imag)

#Built in functions
abs(5.5)
abs(-5.5)
print(round(5.5))
print(round(5.467, 1)) #returns value to 1dp

#enums
from enum import Enum
class State(Enum):
    INACTIVE =0
    ACTIVE=1
print(State.ACTIVE.value)
print(State(1))
print(list(State))
print(len(State))

# User input
#age = input()
#print("Your age is "+age)

#Control statements
condition = True 
if condition== True:
    print("The condition is true")
    
#Lists
dogs = ["Roger", "Syd", "Lerry", 1, True]
print("Roger" in dogs) #finding items in list
print(dogs[0])
dogs[2]= "Beau" #For updating a list
print(dogs)
print(dogs[-1])
print(dogs[2:4])
print(len(dogs))

dogs.append("Derry") #append is for adding a new object to the list or .extend(["Judah", 5])
print(dogs)
dogs.remove("Roger")
print(dogs)
print(dogs.pop)

dogs.insert(2, "Test")
print(dogs)
dogs[1:1] = ["Car","Chair"]
print(dogs)

#Sorting a list
bro = ["Car", "Dog","Abass", "bob"] #It sorts out capital letters before small ones
bro.sort()
print(bro)
brocopy= bro[:] #this is to maintain a copy of the list
print(brocopy)
#to fix this we can
bro.sort(key=str.lower)
print(bro)

#Tuples
#allow you to create immutable list of objects
names=("Roger", "Syd", "Kerry")
print(sorted(names))

#Dictionaries
dog={"name": "Roger"} #Key is name, value is Roger. Roger can hav several key valu
print(dog["name"])
#you can also change the values
dog["name"] = "Syd"
print(dog)
print(dog.get("name"))
