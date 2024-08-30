# #swap first and last element in list
#
# #Method1
# mylist=[12,35,9,56,24]
# size=len(mylist)
#
# temp=mylist[0]
# mylist[0]=mylist[size-1]
# mylist[size-1]=temp
#
# print(mylist)
#
# #method2
# mylist=[12,35,9,56,24]
# mylist[0],mylist[-1]=mylist[-1],mylist[0]
# print(mylist)



list1 = [1, 2, 3]
list1.append(4)
print(list1)  # Output: [1, 2, 3, [4, 5]]

list2 = [1, 2, 3]
list2.extend([4, 5])
print(list2)  # Output: [1, 2, 3, 4, 5]

# Using a for loop
squares = []
for i in range(10):
    squares.append(i**2)

# Using a list comprehension
squares = [i**2 for i in range(10)]
print(squares)
