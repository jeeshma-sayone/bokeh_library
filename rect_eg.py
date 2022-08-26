# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Bokeh Rectangle Graph", match_aspect=True)

# the points to be plotted
x = 0
y = 0
width = 10
height = 5

# plotting the graph
graph.rect(x, y, width, height)

# displaying the model
show(graph)
