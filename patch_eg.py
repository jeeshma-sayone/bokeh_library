# importing the modules
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import magma
import random

# instantiating the figure object
graph = figure(title="Bokeh Patch Plo")

# points to be plotted
x = [n for n in range(256)]
y = [random.random() + 1 for n in range(256)]

# plotting the graph
graph.patch(x, y)

# displaying the model
show(graph)
