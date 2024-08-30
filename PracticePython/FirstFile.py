# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
# import sys
# print(sys.version)
#
# print("Hello ,World")
#
#
# if 5>2:
#     print("Five is greater than two!")
#Python Variables
# x=5
# y="Hello,World"

# print(type(x))
# print(type(y))  #This is comment
# print(x,y)
#
# x=str(3)
# y=int(3)
# z=float(3)
#
# print(x,y,z)
# print(type(x))
# print(type(y))
# print(type(z))
#
# a=4
# A="Sally"
#
# print(a,A)
#
# # Legal Vearible name
# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"
#
# #Camel Case
# myVariableName="Sam"
# x, y, z = "Orange", "Banana", "Cherry"
# print(x)
# print(y)
# print(z)
#
# fruits=["Apple","Mango","Banana"]
# x,y,z=fruits
# print(x)
# print(y)
# print(z)
#
# ###########
# x = "Python "
# y = "is "
# z = "awesome"
# print(x + y + z)

def variable_scope():
    global x
    x=10
    print(x)

variable_scope()
print(x)
