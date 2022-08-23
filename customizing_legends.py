# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Bokeh Line Graph")

# the points to be plotted
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# plotting the 1st line graph
graph.line(x, x, legend_label="Line 1")

# plotting the 2nd line graph with a
# different color
graph.line(y, x, legend_label="Line 2",
           line_color="green")

graph.legend.title = "Title of the legend"
graph.legend.location = "top_right"
graph.legend.label_text_font_size = "17pt"

# displaying the model
show(graph)
