first_name = "Arun"
last_name = 'Motori'

location = str("Pune")

print(type(first_name))
print(first_name[0])
print(first_name[1])
print(first_name[2])
print(first_name[3])

for c in first_name:
    print(c)

print(len(first_name))

print("--" * 20)

for i in range(len(first_name)):
    print(first_name[i])

print("nitin" in first_name)

print(first_name.upper())

name = "   Nitin Gawali  "

print(name.strip())
print("--"*30)
name = "Arun Motori"
word=name.split()
print(word[1])

