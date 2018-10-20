from random import choice

list = []

while len(list) < 5:
    new_member = input("add new name").strip()
    list.append(new_member)
print("We are full")
print(list)    

random_name = choice(list)
print(new_member)

    for new_member in list:
        if "a" in new_member:
            print(new_member)