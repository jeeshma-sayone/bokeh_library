# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Bokeh Oval Graph")

# the points to be plotted
x = [1, 2, 3, 4, 5]
y = [i * 2 for i in x]

# plotting the graph
graph.oval(x, y,
           height=0.5,
           width=1)

# displaying the model
show(graph)
