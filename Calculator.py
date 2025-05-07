print("1 - Add")
print("2 - Subract")
print("3 - Multiply")
print("4 - Divide")
option = int(input("Choose an operation: "))

if (option in[1,2,3,4]):
    num1= int(input("Enter first number "))
    num2= int(input("Enter second number "))
    
    if (option==1):
        results= num1 + num2
    elif(option==2):
        results= num1 - num2
    elif(option==3):
        results= (num1) * (num2)
    else:
        results = num1//num2

else:
    print("invalid operation entered")
    
print("The result of the operation is {}".format(results))