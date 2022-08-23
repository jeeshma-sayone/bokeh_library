from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# instantiating the figure object
graph = figure(title="Interactive legends - Example")


def show_graph():
    """
    In the above example, we will see Interactive legends.
    """
    x = [x for x in range(1, 11)]
    colors = ['red', 'green', 'blue', 'yellow']
    for i in range(2, 6):
        graph.line(x, [val * i for val in x], line_width=2, color=colors[i - 2],
                   alpha=0.8, legend_label='Multiples of {}'.format(i))

    graph.legend.location = "top_left"
    graph.legend.click_policy = "hide"

    # displaying the model
    return show(graph)


show_graph()
