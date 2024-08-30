# 0 1 1 2 3 5 8 13 21 34

n1=0
n2=1

print(n1)
print(n2)

for i in range(2,10):
    sum=n1+n2
    print(sum) # 1
    n1=n2
    n2=sum

print(sum)
print("----"*30)
#############################################

n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(8):  # We already printed the first two numbers
    n1, n2 = n2, n1 + n2
    print(n2)
