# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Bokeh Multiple Polygons Graph")

# the points to be plotted
xs = [[[[1, 1, 3, 4]]]]
ys = [[[[1, 3, 2, 1]]]]

# plotting the graph
graph.multi_polygons(xs, ys)

# displaying the model
show(graph)
