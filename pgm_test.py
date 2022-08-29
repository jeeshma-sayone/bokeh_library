from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import Button, CustomJS, CheckboxGroup, RadioGroup, Slider, Dropdown

# Button
button = Button(label="BUTTON")
button.js_on_click(CustomJS(
    code="console.log('button: click!', this.toString())"))
# ----------- Button End -----------

# Checkbox
L = ["First", "Second", "Third"]

# the active parameter sets checks the selected value
# by default
checkbox_group = CheckboxGroup(labels=L, active=[0, 2])
checkbox_group.js_on_click(CustomJS(code="""
    console.log('checkbox_group: active=' + this.active, this.toString())
"""))
# ----------- Checkbox End -----------

# RadioGroup
# the active parameter sets checks the selected value
# by default
radio_group = RadioGroup(labels=L, active=1)

radio_group.js_on_click(CustomJS(code="""
    console.log('radio_group: active=' + this.active, this.toString())
"""))
# ----------- RadioGroup End -----------

# Slider
slider = Slider(start=1, end=20, value=1, step=2, title="Slider")

slider.js_on_change("value", CustomJS(code="""
    console.log('slider: value=' + this.value, this.toString())
"""))
# ----------- Slider End ---------

# Dropdown
menu = [("First", "First"), ("Second", "Second"), ("Third", "Third")]

dropdown = Dropdown(label="Dropdown Menu", button_type="success", menu=menu)

dropdown.js_on_event("menu_item_click", CustomJS(
    code="console.log('dropdown: ' + this.item, this.toString())"))
# ----------- Dropdown End ---------

# put all the plots in a VBox
screen = column(button, checkbox_group, radio_group, slider, dropdown,)

# show the results

show(screen)
