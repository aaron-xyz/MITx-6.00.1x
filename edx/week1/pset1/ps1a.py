num_vowels = 0
for letter in s:
    if letter in 'aeiou':
        num_vowels += 1
print("Number of vowels: " + str(num_vowels))
