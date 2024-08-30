# input String
input_string="Hello world"
# Initialing the count to 0
vowel_count=0
#define vowel
vowels="aeiou"
# couting logic
for char in input_string:
    if char.lower()in vowels:
        vowel_count+=1

print("Number of vowels in the string",vowel_count)
