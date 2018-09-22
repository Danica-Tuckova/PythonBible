# function parameter = what we use in the function definition 
# name, age, likes = parameters

def about_1 (name, age, likes):
    sentence_1 = "Meet {}!. He is {} years old and he likes {}".format(name, age, likes)
    return(sentence_1)

# function arguments = what we pass to the function when we call her
# Jack, 23, Python = arguments
print(about_1("Jack", 23, "Python"))

# with defaullt value

def about_2(name, age, likes = "Python"):
    sentence_2 = "Meet {}!. He is {} years old and he likes {}".format(name, age, likes)
    return(sentence_2)

print(about_2("Jack", 23, "Footbal"))

def about_3(name = "Zein", age = 26, likes = "Python3"):
    sentence_3 = "Meet {}!. He is {} years old and he likes {}".format(name, age, likes)
    return(sentence_3)

print(about_3())


