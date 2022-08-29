from bokeh.io import output_file, show
from bokeh.layouts import row
from bokeh.plotting import figure


x = [1, 2, 3, 4, 5, 6]
y0 = x
y1 = [i * 2 for i in x]
y2 = [i ** 2 for i in x]

# create a new plot
s1 = figure(width=200, plot_height=200)
s1.circle(x, y0, size=10, alpha=0.5)

# create another one
s2 = figure(width=200, height=200)
s2.triangle(x, y1, size=10, alpha=0.5)

# create and another
s3 = figure(width=200, height=200)
s3.square(x, y2, size=10, alpha=0.5)

# put all the plots in a VBox
p = row(s1, s2, s3)

# show the results
show(p)
