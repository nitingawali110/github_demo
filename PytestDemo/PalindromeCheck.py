#Palindrome Check

def is_palindrome(s):
    return s==s[::-1]

# example
print(is_palindrome("racecar"))
print(is_palindrome("hello"))

# Input string
input_string = "madam"

# Check if the string is the same forwards and backwards
is_palindrome = input_string == input_string[::-1]

# Print the result
if is_palindrome:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
