# Print the list of numbers
for i in range (1,10):
    print(i)


print("--"*50)
# Print the sum of the natural number
n=10 # example input
sum=0

for i in range (1,n+1):
    sum=sum+i

print("sum of first",n,"natural numberes is:",sum)
print("--"*50)

# Factorial of a Number

n=5
factorial=1

for i in range (1,n+1):
    factorial*=i

print("Factorial is :",factorial)
print("--"*50)

## Print Even and odd number

for i in range (1,10,2):
    print(i)

print("--"*50)
for i in range (0,10,2):
    print(i)

num = 7  # Example input
for i in range(1, 11):
    print(num, 'x', i, '=', num * i)
