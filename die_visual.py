""" A script to roll dice and display the results. """

from die import Die            # Import the "DIE" class
import plotly.express as px    # For plotting


# Create a six-sided die.
d6 = Die()                # No argument needed, default is 6 sides.

# Make some rolls of the die.
results = []              # An empty list to save the results

for roll_num in range( 1000 ):
    result = d6.roll()
    results.append( result )

# Analyze the results of the rolls - count how many times each side
# landed up.

frequencies = []

roll_results = range( 1, d6.num_sides+1 )
for value in roll_results:
    frequency = results.count( value )
    frequencies.append( frequency )

# Display the result of 100 rolls.
#print( results )
labels = list( range( 1, d6.num_sides+1 ) )
print( labels )
print( frequencies )

# Plot the results as a bar chart, in the default browser.
fig = px.bar( x=roll_results, y = frequencies )
fig.show()
