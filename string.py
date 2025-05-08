
text = input("Enter a string: ")
consonants = "abc"

count = 0
for char in text:
    if char in consonants:
        count += 1
print("Number of vowels in the string:", count)
