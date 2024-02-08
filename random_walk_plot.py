""" A script to plot a random walk. """

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    # Generate the random walk.
    rw = RandomWalk( 10_000 )        # an instance of RandomWalk, default is 5000 points
    rw.fill_walk()

    # Plot the resulting random walk points.
    plt.style.use( 'classic' )
    fig, ax = plt.subplots( figsize=( 12, 9 ) )   # Plot is 12" by 9".

    # Adjust the color of the points and implement a color-map to show
    # the order the points were generated.
    point_numbers = range( rw.num_points )

    #ax.scatter( rw.x_values, rw.y_values, s=5 )
    ax.scatter( rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
                edgecolors='none', s=4 )
    ax.set_aspect( 'equal' )

    # Emphasize the starting/ending points of the walk.
    ax.scatter( 0, 0, c='green', edgecolors='none', s=25 )
    ax.scatter( rw.x_values[-1], rw.y_values[-1], c='red', 
                edgecolors='none', s=25 )
    
    # Remove the x/y axis, since they are not needed.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    # Prompt to determine if execution should stop.
    answer = input( "Generate another or quit? (a/q)" )
    if answer == 'q':
        break
