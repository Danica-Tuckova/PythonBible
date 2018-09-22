original = input("Please enter a sentence").strip().lower()

words = original.split()

new_words = []

for word in words:
    # if the first letter of the word is vowel
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    # if the fisrt letter of the word isn`t vowel
    else:  
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            # but if it is a vowel - stop looping through
            else:
                break
        cons = word[:vowel_position] 
        the_rest = word[vowel_position:]
        new_word = the_rest + cons + "ya"
        new_words.append(new_word)
#stick words togehter
output = " ".join(new_words)
print(output)

