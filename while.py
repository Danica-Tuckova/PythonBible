# print out the numbers form 1 to 10

    # 1. Sposob bez While Loop

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

    # 2. Sposob pomocou While Loop

number = 1 
while number <= 10:
    print(number)
    number = number + 1

# even numbers (parne cisla)

number2 = 1
while number2 <= 100:
    if number2 % 2 == 0:
        print(number2)
    number2 = number2 + 1    

# odd numbers (neparne cisla)

number3 = 1
while number3 <= 100:
    if number3 % 2 != 0:
        print(number3)
    number3 = number3 + 1

# ask user for a bunch of names up to max of 3 members

L = []
while len(L) < 3:
    new_name = input("Please add new name").strip().capitalize()
    L.append(new_name)

print("Sorry list is full")
print(L)

# cisla delitelne 3 a 5 
number4 = 1
while number4 <= 100:
    if number4 % 3 == 0 and number4 % 5 == 0:
        print(number4)
    number4 = number4 + 1

