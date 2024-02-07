""" A simple plot of squared numbers. """

import matplotlib.pyplot as plt

squares = [ 1, 4, 9, 16, 25, 36 ]

fig, ax = plt.subplots()
ax.plot( squares, linewidth=3 )  # Plotting 'squares' with increased line thickness

# Set the chart title and axes labels.
ax.set_title( "Squared Numbers", fontsize=24 )
ax.set_xlabel( "Value", fontsize=14 )
ax.set_ylabel( "Square of Values", fontsize=14 )

# Set the size of the axis tics and their values
ax.tick_params( labelsize=14 )

plt.show()
