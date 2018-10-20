# make a list of questions 
# pick a random one question from the list for the baby to use

# z balika random vybrat funkciu choice
import random 
questions = ["Why is the sky blue?", "Why is there a face on the moon?", "Where are all the dinosaurus?"]

question = random.choice(questions)

# baby`s question and get the answear
answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ").strip().lower()
print("Oh...Okay")    