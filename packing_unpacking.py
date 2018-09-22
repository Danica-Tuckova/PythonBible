# UNPACK ARGUMENTS 

#unpack numbers

print(1, 2, 3, 4, 5)

numbers = [1, 2, 3, 4, 5]
print(numbers)

numbers = [1, 2, 3, 4, 5]
print(*numbers)

# unpack strings

print("abc")

print("a", "b", "c")

print(*"abc")

# PACK ARGUMENTS 

def add(x, y):
    return x + y
print(add(10, 10))    

# for a lot of parameters (not only for two parameters)

def add_more(*numbers):
    total = 0
    for number in numbers:
        total = total + number
    return(total)

print(add_more(1, 2, 3, 4, 5))

# unpack dictionary into function

def about(name, age, likes):
    sentence = "Meet {}! He is {} years old and he likes {}".format(name, age, likes)
    return(sentence)

dictionary = {"name": "Zein", "age": 23, "likes": "Python"}

print(about(**dictionary))
# the same result will be when we use
print(about(name = "Zein", age = 23, likes = "Python"))

# exercise 1

# function with default values
def func(name = "John", age = "23"):
    print(name)
    print(age)

func()  

#
def func1(year, **kwargs):
    for a, b in kwargs.items():
        print("key: " + a)
        print("value: " + b)
    print("Year: " + str(year))

func1(1900, name = "David", age = "23")

def foo(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key, value))

foo(huda = "Female", Zein = "male")        