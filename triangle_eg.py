# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Bokeh Triangle Graph")

# the points to be plotted
x = 1
y = 1

# plotting the graph
graph.triangle(x, y, size=150)

# displaying the model
show(graph)
