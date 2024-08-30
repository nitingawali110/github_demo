mylist = ["geeks", "for", "geeks","geeks","geeks"]

word = "geeks"
n = 3

count = 0
for i in range(0, len(mylist)-1):
    if mylist[i] == word:
        count=count+1
        if count==n:
            del mylist[i]

print(mylist)


#################
# How to search Element in alist

mylist=[1,6,3,5,7]

ele=5

if(ele in mylist):
    print("element found")
else:
    print("element not found")

