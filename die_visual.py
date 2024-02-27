""" A script to roll dice and display the results. """

from die import Die            # Import the "DIE" class
import plotly.express as px    # For plotting


# Create a six-sided die.
d6_1 = Die()                # No argument needed, default is 6 sides.
d6_2 = Die()                # A second die

# Make some rolls of the die.
results = []              # An empty list to save the results

for roll_num in range( 1000 ):
    result = d6_1.roll() + d6_2.roll()   # Roll both dice
    results.append( result )

# Analyze the results of the rolls - count how many times each side
# landed up.

frequencies = []
max_result  = d6_1.num_sides + d6_2.num_sides

roll_results = range( 2, max_result+1 )
for value in roll_results:
    frequency = results.count( value )
    frequencies.append( frequency )

# Display the result of 100 rolls.
#print( results )
labels = list( range( 1, max_result+1 ) )
print( labels )
print( frequencies )

# Plot the results as a bar chart, in the default browser.
title = "Results of Rolling 2 Six-Sided Die, 1000 times"
labels = { 'x': 'Result', 'y': 'Frequency of Result' }
fig = px.bar( x=roll_results, y = frequencies, title=title, labels=labels )
fig.update_layout( xaxis_dtick=1 )   # Setting to label every bar on the x-axis

# Save the plot to a file before invoking the browser.
fig.write_html( 'die_visual_result.html' )

# Invoke the browser to show the visualization.
fig.show()
