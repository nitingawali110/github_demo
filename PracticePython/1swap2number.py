num1=10
num2=20

print("Value of num1 before Swapping:",num1)
print("Value of num2 before Swapping:",num2)

temp=num1 #10
num1=num2 #20
num2=temp #10

print("Value of num1 after Swapping:",num1)
print("Value of num2 after  Swapping:",num2)

# You can take input from user

num1=input("Enter num1 Value:")
num2=input("Enter num2 Value:")

temp=num1 #10
num1=num2 #20
num2=temp #10

print("Value of num1 after Swapping:",num1)
print("Value of num2 after  Swapping:",num2)
print("---"*50)

# Second approach
num1=input("Enter num1 Value:")
num2=input("Enter num2 Value:")

num1,num2=num2,num1
print("Value of num1 after Swapping:",num1)
print("Value of num2 after  Swapping:",num2)
