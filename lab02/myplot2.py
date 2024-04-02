import matplotlib.pyplot as plt 
from collections import deque 
import random 

# Create a fixed-length deque of size 50 to store the data points 
data_points = deque(maxlen=50) 

# Create an empty plot 
fig, ax = plt.subplots() 
line, = ax.plot([]) 


# Set the x-axis and y-axis limits to 100 
ax.set_xlim(0, 100) 
ax.set_ylim(0, 100) 

# Iterate through 50 data points and update the plot 
for i in range(50): 
	# Generate and add data points to the deque 
	new_x = i 
	# generate a random number between 0 to 100 for y axis 
	new_y = random.randint(0, 100) 
	data_points.append((new_x, new_y)) 

	# Update the plot with the new data points 
	x_values = [x for x, y in data_points] 
	y_values = [y for x, y in data_points] 
	line.set_data(x_values, y_values) 
	# pause the plot for 0.01s before next point is shown 
	plt.pause(0.01) 

# Show the plot 
plt.show() 
