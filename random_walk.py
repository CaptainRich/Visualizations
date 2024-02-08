""" A script illustrating the generation of random-walk data. """

from random import choice

class RandomWalk:
    """ A class to generate random walks. """

    def __init__( self, num_points=5000 ):
        """ Initialize the attributes of the random walk. """
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk( self ):
        """ Compute all the points in the random walk. """

        # Keep taking steps (adding points) until the walk reaches 
        # the desired length (num_points).
        while len( self.x_values ) < self.num_points:

            # Decide which direction to go, and how far to go.
            x_direction = choice( [-1, 1] )
            x_distance  = choice( [0, 1, 2, 3, 4, 5, 6] )
            x_step      = x_direction * x_distance

            y_direction = choice( [-1, 1] )
            y_distance  = choice( [0, 1, 2, 3, 4, 5, 6] )
            y_step      = y_direction * y_distance      

            # Determine the new position (add the movement to the last position).
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            # Save this new position in the list
            self.x_values.append(x)
            self.y_values.append(y)   
               