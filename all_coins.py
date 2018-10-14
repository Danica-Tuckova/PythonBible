import random 
# make general abstract class called Coin 

class Coin:
    def __init__(self, rare = False, clean = True, heads = True, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

    # rare 
        if self.is_rare:
          self.value = self.original_value * 1,25
        else:
            self.value = self.original_value

    # clean
        if self.is_clean:
             self.colour = self.clean_colour
        else:
             self.colour = self.rusty_colour

    # rust method
    def rust(self):
        self.colour = self.rusty_colour

    # clean method
    def clean(self):
        self.colour = self.clean_colour

    # flip method 
    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    # make Pound class inherited from the Coin class (from the parent class)

class Pound(Coin):
    def __init__(self):
        # make dictionary data 
        data = {
            "original value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish",
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        # need access the parent's class
        # **data = unpack data from dictionary called Pound into keywords
        # **kwargs = pack it down back into another dictionary called kwargs
        super().__init__(**data)      
                                           