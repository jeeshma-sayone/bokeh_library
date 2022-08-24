# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title = "Bokeh Bar Graph")

# the points to be plotted
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

# height / thickness of the plot
height = 0.5

# plotting the bar graph
graph.hbar(x, right = y, height = height)

# displaying the model
show(graph)
