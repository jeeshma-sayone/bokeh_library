# importing the modules
from bokeh.plotting import figure, output_file, show

# instantiating the figure object
graph = figure(title="Annotations and Legends - Example")


def show_graph():
    """
    In the above example, we have plotted two different lines with
    a legend that imply states that which is line 1 and which is line 2.
    The color in the legends is also differentiated by the color.
    """

    # the points to be plotted
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]

    # plotting the 1st line graph
    graph.line(x, x, legend_label="Line 1")

    # plotting the 2nd line graph with a
    # different color
    graph.line(y, x, legend_label="Line 2",
               line_color="green")

    # displaying the model
    return show(graph)


show_graph()
