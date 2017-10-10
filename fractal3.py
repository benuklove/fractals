"""

    Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve --show fractal3.py
    at your command prompt.
    This will open a new window (or tab) in your browser at
    http://localhost:5006/fractal3
    It will keep running until ctrl + c.

"""


from random import choice

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import TextInput
from bokeh.plotting import figure


# Just for now, these points. Will generalize later:
points = {
    'ax': 0,
    'ay': 0,
    'bx': 5,
    'by': 10,
    'cx': 10,
    'cy': 0
}

last_target = choice(['a', 'b', 'c'])
last_x = points[last_target + 'x']
last_y = points[last_target + 'y']


def draw():
    global last_x, last_y

    next_target = choice(['a', 'b', 'c'])
    next_x = points[next_target + 'x']
    next_y = points[next_target + 'y']

    new_x = (next_x + last_x) / 2
    new_y = (next_y + last_y) / 2

    plot.circle(x=new_x, y=new_y, size=1, fill_color='blue')
    last_x = new_x
    last_y = new_y


def create_plot():
    # Set up plot
    plot = figure(plot_height=600, plot_width=600, title="Fractals",
                  tools="crosshair,pan,reset,save,wheel_zoom",
                  x_range=[0, 10], y_range=[0, 10])

    plot.border_fill_color = 'black'
    plot.background_fill_color = 'black'
    plot.outline_line_color = None
    plot.grid.grid_line_color = None

    curdoc().add_periodic_callback(draw, 0.0001)

    return plot


plot = create_plot()


# Set up widgets
text = TextInput(title="title", value='Fractals')


# Set up callbacks
def update_title(attrname, old, new):
    plot.title.text = text.value


text.on_change('value', update_title)


# Set up layouts and add to document
inputs = widgetbox(text)
layout = row(inputs, plot)

curdoc().add_root(layout)
curdoc().title = "Fractals"
