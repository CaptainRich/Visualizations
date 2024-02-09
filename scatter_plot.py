""" A simple scatter plot of squared numbers. """

import matplotlib.pyplot as plt

# Define the data to be plotted.
x_values = range( 1, 1001 )
y_values = [x**2 for x in x_values ]   # list compression

# Try a built-in style. (The code 'plt.style.available' will list the styles.)
plt.style.use( 'seaborn-v0_8' )
fig, ax = plt.subplots()

# Set the size and color of the dots
#ax.scatter( x_values, y_values, color=(0,0.8,0), s=10 ) 

# Alternatively use a color map.
ax.scatter( x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=2 ) 

# Label the various plot elements.
ax.set_title( "Squared Numbers", fontsize=24 )
ax.set_xlabel( "Value", fontsize=14 )
ax.set_ylabel( "Square of Value", fontsize=14 )

# Set the size of the axis data values (tics).

ax.tick_params( labelsize=14 )

# Set the range of axis values.
ax.axis( [ 0, 1100, 0, 1_100_000 ] )

# Force the use of 'plain' numbers, avoid 'scientific notation'.
ax.ticklabel_format( style='plain' )


# Save the plot to a file, trimming the extra white-space.
plt.savefig( 'squares_plot.png', bbox_inches='tight' )

# Show the plot(s) on the screen.
plt.show()
