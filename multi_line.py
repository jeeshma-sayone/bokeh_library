# importing the modules
from bokeh.plotting import figure, output_file, show


# instantiating the figure object
graph = figure(title="Bokeh Multi Line Graph")

# the points to be plotted
xs = [[1, 2, 3, 4, 5], [-4, -2, 0, 2, 4]]
ys = [[5, 3, 8, 0], [5, -4, 10, -2, 5]]

# plotting the graph
graph.multi_line(xs, ys)

# displaying the model
show(graph)
