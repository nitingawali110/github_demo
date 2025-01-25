#1.Reverse a String
# Input
s = "Interview"

# Reverse the string using slicing
reversed_string = s[::-1]

# Output
print(f"Reversed string: {reversed_string}")

#2. Find the Largest Element in a List
# Input list
lst = [3, 5, 1, 9, 2]

# Find the largest element using max()
largest = max(lst)

# Output
print(f"Largest number: {largest}")

#3. Check if a String is a Palindrome
# Input string
s = "radar"

# Check if the string is equal to its reverse
is_palindrome = s == s[::-1]

# Output
print(f"Is palindrome: {is_palindrome}")

#4. Find Factorial of a Number
# Input number
n = 5

# Initialize factorial
factorial = 1

# Calculate factorial
for i in range(1, n + 1):
    factorial *= i

# Output
print(f"Factorial of {n}: {factorial}")

#5. Remove Duplicates from a List
# Input list
lst = [1, 2, 3, 1, 2, 4, 5]

# Convert to set and back to list to remove duplicates
unique_lst = list(set(lst))

# Output
print(f"List without duplicates: {unique_lst}")

#6. Fibonacci Sequence
n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(8):  # We already printed the first two numbers
    n1, n2 = n2, n1 + n2
    print(n2)

#7. Count Vowels in a String
# Input string
s = "Hello World"

# Set of vowels
vowels = 'aeiouAEIOU'

# Count the number of vowels
vowel_count = sum(1 for char in s if char in vowels)
# Iterate over each character in the string
for char in s:
    if char in vowels:  # Check if the character is a vowel
        vowel_count += 1  # Increment the counter if it's a vowel

# Output
print(f"Number of vowels: {vowel_count}")


#8. Merge Two Sorted Lists
# Input lists
list1 = [1, 3, 5]
list2 = [2, 4, 6]

# Merge the lists and sort
merged_list = sorted(list1 + list2)

# Output
print(f"Merged list: {merged_list}")

#9. Find the Second Largest Element in a List
# Input list
lst = [1, 3, 4, 5, 0, 2, 5, 5]

# Remove duplicates and sort the list
unique_lst = list(set(lst))
unique_lst.sort()

# Output the second largest element
if len(unique_lst) >= 2:
    print(f"Second largest number: {unique_lst[-2]}")
else:
    print("Not enough unique elements.")

#10.Check if Two Strings are Anagrams
# Input strings
str1 = "listen"
str2 = "silent"

# Check if sorted versions of the strings are equal
are_anagrams = sorted(str1) == sorted(str2)

# Output
print(f"Are anagrams: {are_anagrams}")


# Remove First value 20 X = [10, 20, 30, 40, 20, 40, 50, 20]
def remove_first_occurrence(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            del lst[i]
            break  # Exit the loop after removing the first occurrence
    return lst

# Example usage
X = [10, 20, 30, 40, 20, 40, 50, 20]
value_to_remove = 20
updated_list = remove_first_occurrence(X, value_to_remove)
print(updated_list)

#You can create a dictionary by using elements from the list x as keys and elements from the list y as values. Here's how to do it:
x = [1, 4, 5, 8]
y = [20, 50, 10, 40, 80]
# Create a dictionary using zip to pair elements from x and y
dictionary = dict(zip(x, y))
print(dictionary)

#Remove duplicate characters from a string
str = "Hello World"
result = ""

for char in str:
    if char not in result:
        result += char

print(result)

