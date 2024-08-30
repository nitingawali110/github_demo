# Input number
number="123456789"
sum_of_digit=0
for char in number:
    sum_of_digit+=int(char)

print("The sum of digit is:",sum_of_digit)

##Other method
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

# Example usage:
print(sum_of_digits(1234))  # Output: 10


