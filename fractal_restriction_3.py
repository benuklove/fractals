''' Present an interactive function explorer with slider widgets.
Scrub the sliders to change the properties of the ``sin`` curve, or
type into the title text box to update the title of the plot.
Use the ``bokeh serve`` command to run the example by executing:
    bokeh serve sliders.py
at your command prompt. Then navigate to the URL
    http://localhost:5006/sliders
in your browser.
'''


from random import choice

from bokeh.io import curdoc
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import TextInput
from bokeh.plotting import figure


# Just for now, these points. Will generalize later:
points = {
    'ax': 0,
    'ay': 0,
    'bx': 0,
    'by': 10,
    'cx': 10,
    'cy': 10,
    'dx': 10,
    'dy': 0
}

last_target = choice(['a', 'b', 'c', 'd'])
last_x = points[last_target + 'x']
last_y = points[last_target + 'y']


def choose_next():
    next_target = choice(['a', 'b', 'c', 'd'])

    return next_target


def draw():
    global last_x, last_y, last_target

    flag = 0
    while flag == 0:
        next_target = choose_next()
        if abs(ord(next_target) - ord(last_target)) == 2:
            continue
        else:
            flag = 1

    last_target = next_target
    next_x = points[next_target + 'x']
    next_y = points[next_target + 'y']

    new_x = (next_x + last_x) / 2
    new_y = (next_y + last_y) / 2

    plot.circle(x=new_x, y=new_y, size=1, color='black')
    last_x = new_x
    last_y = new_y


def create_plot():
    # Set up plot
    plot = figure(plot_height=500, plot_width=500, title="Fractals",
                  tools="crosshair,pan,reset,save,wheel_zoom",
                  x_range=[0, 10], y_range=[0, 10])

    # plot.border_fill_color = 'black'
    # plot.background_fill_color = 'black'
    plot.outline_line_color = None
    plot.grid.grid_line_color = None

    curdoc().add_periodic_callback(draw, 0.001)

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
