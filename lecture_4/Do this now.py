VOWELS = "aeiou"


number_of_vowels = 0
name = input("get user name:")
letters = len(name)
for char in name:
    if char.lower() in VOWELS:
        number_of_vowels += 1


print("out of {} letters, {} has {} vowels".format(letters, name, number_of_vowels))
