import numpy as np
from bokeh.plotting import figure, output_file, show

# creating the figure object
plot = figure(plot_width=300, plot_height=300)

plot.circle(x=[1, 2, 3], y=[3, 7, 5], size=20)

show(plot)
