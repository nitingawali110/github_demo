#

for i in range(1,11):
    if i==5:
        break
    print(i) # 1 2 3 4


print("---"*20)

for i in range(1,11):
    if i==5 or i==8:
        continue
    print(i) # 1 2 3 4


print("---"*20)

# Use break in while loop statement

i=1

while i<10:
    if i==5 :
        i+=1
        continue
    print(i)
    i+=1
