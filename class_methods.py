import random

class Pound():

# self = the name of object
# init creats a new object called self

    def __init__(self, rare = False):
        # self.rare = behaviour of object self - False
        self.rare = rare

        if self.rare:
            # if self. rare == True
            self.value = 1.25
        else:
            # if self.rare = False
            self.value = 1.00
        self.colour = "gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True    

    # from False to True
 
    # create a rush method which changes gold colour to greenish colour

    def rust(self):
        self.colour = "greenish"

    # create a clean method which clean our coins if they`re rusted      

    def clean(self):
        self.colour = "gold"

    # make coin flip randomly

    def flip(self):
        # have a list of choices True or False
        heads_options = [True, False]
        # take a random choice of these
        choice = random.choice(heads_options)
        self.heads = choice

    # create a destructor method

    def __del__(self):
        print("Coin Spent!")    


# vypis
coin1 = Pound(rare = True)
coin2 = Pound()
print(coin1.rare)
print(coin2.rare)
print(coin1.value)
print(coin2.value)


# vypis rust method
coin_1 = Pound()
coin_2 = Pound()
print(coin_1.colour)
print(coin_2.colour)

coin_1.rust()
print(coin_1.colour)

# vypis clean method
coin1 = Pound()
coin1.clean()
print(coin1.colour)

# vypis flip method
coin1 = Pound()
print(coin1.heads)

coin1.flip()
print(coin1.heads)

# vypis destructor method
coin1 = Pound()
del coin1
