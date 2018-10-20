known_user = ["Klare", "Bob", "Jack", "Dory"]

while True:
    name = input("What is your name? :").strip().capitalize()
    if name in known_user:
        gender = input("What is your gender? (woman/man)?: ").strip().lower()
        if gender == "woman":
            remove = input("Would you like to be remove from the list Mrs {}? (yes/no)".format(name))
            if remove == "yes":
                known_user.remove(name)
            elif remove == "no":
                print(("Okay Mrs {}, you will stay in the database").format(name))
        elif gender == "man":
            remove = input("Would you like to be remove from the list Mr {}? (yes/no)".format(name))
            if remove == "yes":
                known_user.remove(name)
            elif remove == "no":
                print(("Okay Mr {}, you will stay in the database").format(name))
    else:
        print("Sorry, you are not on the list")
        add = input("Would you like to be added to the system? (yes/no) ").strip().lower()
        if add == "yes":
            known_user.append(name)
        elif add == "no": 
            print("No worries, see you around")   
