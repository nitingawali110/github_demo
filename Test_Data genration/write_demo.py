# Manual Steps to write a file
#1.Open notepad and create file
#2. Write in the file
#3. Close the file

#mode
#Read Mode:r
#Write Mode:w
#Append mode:a
#Read/Write:r+

f=open("E:\\NitinPythonProject\\writedemo.txt", "w")
f.write("This is first Line")
f.close()

f=open("E:\\NitinPythonProject\\writedemo1.txt", "a")
l=[65,60,674,65,68]
for items in l:
    f.write(str(items)+"\n")
f.close()


