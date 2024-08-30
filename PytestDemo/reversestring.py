#Reverse a String
#Question: Write a function that takes a string as input and returns the string reversed.

def reverse_string(s):
    return s[::-1]

# Example
print(reverse_string("hello"))
#####other Method####
# Original string
original_string = "Hello, World!"

# Reversing the string using slicing
reversed_string = original_string[::-1]

# Printing the result
print("Original String:", original_string)
print("Reversed String:", reversed_string)

