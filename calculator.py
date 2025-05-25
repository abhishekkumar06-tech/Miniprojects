#basic calculator

print("1 - Add",)
print("2 - Subtract")
print("3 - Multiply")
print("4 - Divide")
print("5 - square")
print("6 - remainder")
print("7 - root")
print("8 - power")

option = int(input("Choose an operation: "))

result = 0
if(option in [1,2,3,4,]):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3):
        result = num1 * num2
    elif(option == 4):
        result = num1 / num2
    elif(option == 5):
        num = float(input("Enter the number: "))
        result = num**2
if(option == 6):
     num1 = float(input("Enter numerator: "))
     num2 = float(input("Enter denominator: "))
     result = num1%num2 
     
if(option == 7):
     num1 = float(input("Enter the number: "))
     num2 = float(input("Enter the degree of the root: "))
     a = 1/num2
     result = num1**a

if(option == 8):
     num1 = float(input("Enter the number: "))
     num2 = float(input("Enter power of the nubmer: "))
     result = pow(num1,num2)

else:
    print("Invalid option entered")

print("The result of the operation is: ", float(round(result,2)))

