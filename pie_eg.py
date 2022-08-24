# importing the modules
from bokeh.plotting import figure, show

# instantiating the figure object
graph = figure(title="Bokeh Pie Chart")

# center of the pie chart
x = 0
y = 0

# radius of the glyphs
radius = 1

# starting angle values
start_angle = [0, 1.8, 2.5,
               3.7, 5.6]

# ending angle values
end_angle = [1.8, 2.5, 3.7,
             5.6, 0]

# color of the wedges
color = ["violet", "blue", "green",
         "yellow", "red"]

# plotting the graph
graph.wedge(x, y, radius,
            start_angle,
            end_angle,
            color=color)

# displaying the graph
show(graph)
