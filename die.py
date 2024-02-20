""" A script to simulate rolling dice. """

from random import randint

class Die:
    """ A class representing a single die. """

    def __init__( self, num_sides=6 ):
        """ Default to a six-sided die. """
        self.num_sides = num_sides


    def roll( self ):
        """ Simulate a roll by returning a random value between 1 and 
            num_sides. """
        
        return randint( 1, self.num_sides )
    
