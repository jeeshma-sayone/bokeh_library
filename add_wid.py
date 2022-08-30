from bokeh.io import show
from bokeh.layouts import column
from bokeh.models import Button, CustomJS, CheckboxGroup, RadioGroup, Slider, Dropdown, TextInput, Select, Paragraph, \
    TextAreaInput, PasswordInput, Div, FileInput, DatePicker

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

# TextInput
text_input = TextInput(title='my label:', value='something')
# ----------- TextInput End -----------

# Select
select = Select(title="Option:", value="Blue",
                options=["Red", "Yellow", "Blue", "Green"])
# ----------- Select End -----------

# Paragraph
para = Paragraph(text="""Encryption is the process of converting
normal message (plaintext) into meaningless message (Cipher text).
Whereas Decryption is the process of converting meaningless message
(Cipher text) into its original form (Plaintext).""",
                 )
# ----------- Paragraph End -----------

# TextAreaInput
text_area = TextAreaInput(value="Write here",
                          rows=6, title="Label:")

# ----------- TextAreaInput End -----------

# PasswordInput
password = PasswordInput(placeholder="Enter password...")

# ----------- PasswordInput End -----------

# Div
div = Div(text="""<a href="https://www.python.org/">
Python</a> is <b>high level</b> programming language.
Its easy to learn because of its syntax.""")
# ----------- Div End -----------

# FileInput
file = FileInput()
# ----------- FileInput End -----------

# DatePicker
dp = DatePicker(title='Select date', value="2022-08-30",
                min_date="1947-01-01")
# ----------- DatePicker End -----------

# put all the plots in a VBox
screen = column(button, checkbox_group, radio_group, slider, dropdown, text_input, select, para, text_area, password,
                div, file, dp)

# show the results

show(screen)
