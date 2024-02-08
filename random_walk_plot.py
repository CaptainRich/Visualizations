""" A script to plot a random walk. """

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    # Generate the random walk.
    rw = RandomWalk()        # an instance of RandomWalk
    rw.fill_walk()

    # Plot the resulting random walk points.
    plt.style.use( 'classic' )
    fig, ax = plt.subplots()

    ax.scatter( rw.x_values, rw.y_values, s=5 )
    ax.set_aspect( 'equal' )

    plt.show()

    # Prompt to determine if execution should stop.
    answer = input( "Generate another or quit? (a/q)" )
    if answer == 'q':
        break
