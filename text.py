name="Beau"
print(type(name))
#you can also use isintance to check the data type luke the one below
age=29
print(isinstance(age,float))
print(isinstance(age,int))
#it is possible to also change from one data type to another using the data type converter below
age = int("29")
print(age)
num= "20"
inte= int(num)
print(inte) #this is known as casting

#mathematical operations
exp= 4**2 #16
div= 4/2 #this gives 2. When you use //, it rounds it off incase there is a decimal
rem= 5%2

age = 8
age +=8
print(age)
 
#an or returns the secondd value to be true only if the first is false
print(0 or 1) ##1
print(False or 'hey') ##hey
print('hi' or 'hey') ##hi
print([] or False) ##False

#for an or operator, it returns the first if the first is false, else the second

#The use of strings
print("beau".upper())
print("BaysY".lower())
print("derrick mensah".title())

print(""""Kojo 
      
   is
   
   49 years
    
    old""")
