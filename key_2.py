students = {
    "male": ["Tom", "Charlie", "Harry", "Frank"],
    "female": ["Sarah", "Huda", "Samantha", "Emily", "Ela"]
}

# print only key
for key in students.keys():
    print(key)

# print the list 
for key in students.keys():
    print(students[key])

# go through all of these names and only print out the names which have a letter A in them
for key in students.keys():
    for name in students[key]:
        if "a" in name:
            print(name)      