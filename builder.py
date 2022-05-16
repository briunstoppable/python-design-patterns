# Crafted with supporting information from https://refactoring.guru/design-patterns/builder/python/example

# Usage examples: 
#    The Builder pattern is a well-known pattern in Python world. 
# It’s especially useful when you need to create an object with lots of possible configuration options.
# Identification: 
#    The Builder pattern can be recognized in a class,  which has a single creation method 
# and several methods to configure the resulting object. 
# Builder methods often support chaining 
# Example: 
#    someBuilder.setValueA(1).setValueB(2).create()).

# Let's use a builder to customize a laptop object. 
# We could then export this as JSON and store it in a database with a customer profile until they're ready to order.

import json

class Laptop():
    '''The Product'''
    def __init__(self):
        self.has_gpu = False
        self.has_4k = False
        self.edu_sku = False
        self.ram_size = None
        self.proc_frequency = None
        self.screen_size = None

# Single Responsibility, anyone?

    def add_gpu(self):
        self.has_gpu = True

    def add_4k(self):
        self.has_4k = True

    def set_edu_sku(self):
        self.edu_sku = True

    def set_ram_size(self, size):
        self.fuel = size
 
    def set_proc_frequency(self, freq):
        self.freq = freq

    def set_secreen_size(self, screen):
        self.screen = screen

    #Returning information about car
    def __str__(self):
    #    json.dumps() - TODO:: WE'LL COME BACK AFTER DINNER!
        return 

