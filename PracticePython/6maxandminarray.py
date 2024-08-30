arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

max = arr[0]
n = len(arr)

for i in range(1, n):
    if arr[i] > max:
        max=arr[i]

print(max)

# Min Number
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

min=arr[0]

n=len(arr)

for i in range(1,n):
    if arr[i]<min:
        min=arr[i]

print(min)


























