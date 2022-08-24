# Implementation of bokeh function
import numpy as np
from bokeh.plotting import figure, output_file, show

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 5, 2, 4]
y2 = [1, 2, 2, 3, 6]

# instantiating the figure object
graph = figure(plot_width=300, plot_height=300)

# area plot
graph.varea(x=x, y1=y1, y2=y2, fill_color="green")

show(graph)
