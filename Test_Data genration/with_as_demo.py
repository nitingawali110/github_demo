# fw=open("demofile.txt","w")
# fw.write("1st line")
# fw.close()
#
# fr=open("demofile.txt","r")
# fr.read()
# fr.close()

# with open("demofile.txt","w") as fw:
#     fw.write("This line is from with opertaions nitin")
#
# with open("demofile.txt","r") as fr:
#     print(fr.read())

fruits=["Apple","Banana","Cherry"]
for x in fruits:
    print(x)
    if x=="Banana":
        break
print("---"*15)

for x in fruits:
    if x=="Banana":
        break
    print(x)

print("---"*15)

for x in range (6):
    print(x)
print("-While-")

thislist=["Apple","Banana","Cherry"]
i=0
while i< len(thislist):
    print(thislist[i])
    i=i+1

