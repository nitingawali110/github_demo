input_string = "Testing2349"
numbers = ""

for char in input_string:
    if char.isdigit():
        numbers += char

print(numbers)  # Output: 2349


numbers = ""
for char in input_string:
    if char.isdigit():
        numbers=numbers+char

print("The Give String Having Numbers are :",numbers)

arr = [12, 35, 1, 10, 34, 1]
# Sort the array in ascending order
arr.sort()
# The second largest number is the second last element in the sorted array
second_largest = arr[-2]
print("Second largest number is:", second_largest)
print(arr)
print('__'*15)

# n=5
# for i in range(n):
#     for j in range (i+1):
#         print('*', end='')
#     print()
#
# print('__'*15)
#
# n=5
# for i in range(n):
#     for j in range (i,n):
#         print('*', end='')
#     print()
# print('__'*15)


n=5
for i in range(n):
    for j in range(i,n-1):
        print('',end='')
    for j in range(i+1):
        print('*',end='')
    print()

print('__'*15)

n = 5
for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(' ', end='')
    # Print stars
    for j in range(i + 1):
        print('*', end='')
    # Move to the next line
    print()
