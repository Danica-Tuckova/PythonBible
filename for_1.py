# print numbers form 1 to 10
# RANGE FUNCTION
for number in range(1, 11):
    print(number)

for number1 in range(1, 11, 2):
    print(number1)

# print string "abcd" 

for letter in "abcd":
    print(letter)

# go through a piece of text ("Hello") and count the amount of vowels (a, e, i, o, u)
# and number of consonants 

vowels = 0
consonants = 0

for letter in "He llo":
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == ' ':
        pass
    else:
        consonants = consonants + 1
print("There are {} vowels".format(vowels))
print("There are {} consonants".format(consonants))            