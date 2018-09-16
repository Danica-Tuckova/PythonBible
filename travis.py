known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgia", "Harry"]

while True:
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()

    # known user

    if name in known_users:
       print("Hello {}!".format(name))
       remove = input("Would you like to be removed from the system (yes/no)?: ").strip().lower()
       if remove == "yes":
          known_users.remove(name)
       elif remove == "no":
          print("No problem. I did not want you to leave anyway!")

    # unknown user

    else:
        print("Hmmm I don`t think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (yes/no)?: ").strip().lower()
        if add_me == "yes":
           known_users.append(name)
        elif add_me == "no":
           print ("No worries, see you around!")
            
