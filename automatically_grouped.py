from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# instantiating the figure object
graph = figure(title="Automatic Grouping - Example", x_range=(0.5, 2.5), y_range=(0.5, 2.5))


def show_graph():
    """
    In the above example, we will see , Automatic Grouping can be used when we want to group
    multiple legend items to be grouped into one.
    """
    source = ColumnDataSource(dict(
        x=[1, 1, 2, 2, 1.5],
        y=[1, 2, 1, 2, 1.5],
        color=['red', 'red', 'red', 'red', 'blue'],
        label=['corner', 'corner', 'corner', 'corner', 'center']
    ))
    graph.circle(x='x', y='y', radius=0.05, color='color',
                 legend_group='label', source=source)

    # output_file("AutomaticGrouping.html")

    # displaying the model
    return show(graph)


show_graph()

