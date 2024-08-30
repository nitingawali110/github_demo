def are_anagram(s1,s2):
    return sorted(s1)==sorted(s2)

# example
print(are_anagram("listen","silent"))
print(are_anagram("hello","world"))

