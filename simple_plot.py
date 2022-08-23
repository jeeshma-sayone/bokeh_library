# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Bokeh Line Graph")

# the points to be plotted
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# plotting the line graph
graph.line(x, y)

# displaying the model
show(graph)

# In the above example, we have created a simple Plot with the Title as Bokeh Line Graph.
