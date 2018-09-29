# create class
class Pound():
    value = 1.00
    colour = "gold"
    num_edges = 1
    diameter = 22.5 #mm
    thickness = 3.15 #mm
    heads = True

# creat object coin1

coin1 = Pound()
print(coin1.value)
print(coin1.colour)
    # change value of colour
coin1.colour = "red"
print(coin1.colour)
    # change value of value
coin1.value = 1.25    

# creat another object called coin2

coin2 = Pound()

# chcek colour

# coin 1 has a new colour - red
print(coin1.colour)
# coin2 has original colour - gold
print(coin2.colour)

# check value
print(coin1.value)
print(coin2.value)