students = {"Alice":26, "Bob":27, "Claire":17, "Dan":21, "Emma": 22}

#make list
students1 = {
    "Alice": ["ID0001", 26, "A"],
    "Bob": ["ID0002", 27, "B"],
    "Claire": ["ID0003", 17, "C"],
    "Dan": ["ID0004", 21, "D"],
    "Emma": ["ID0005", 22, "E"],
}

# get all of the Claire`s data
print(students1 ["Claire"])

# get only Claire`s ID
print(students1 ["Claire"][0])

# get Dan`s age and grade
print(students1 ["Dan"][1:]) 

# make dictionary
students2 = {
    "Alice": {"id":"ID0001", "age":26, "grade":"A"},
    "Bob": {"id":"ID0002", "age":27, "grade":"B"},
    "Claire": {"id":"ID0003", "age":17, "grade":"c"},
    "Dan": {"id":"ID0004", "age":21, "grade":"D"},
    "Emma": {"id":"ID0005", "age":22, "grade":"E"}
}

# get Dan`s age
print(students2["Dan"]["age"])

#get Emmma`s id and grade
print(students2["Emma"]["id"], students2["Emma"]["grade"])