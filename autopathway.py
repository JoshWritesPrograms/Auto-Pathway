import dotprocessing as dp
import field
from tkinter import *

# Main function (triggered by button)

def generate_pathway():
    h_dots = dp.generate_h_dots(x_input.get('1.0', 'end-1c'))
    v_dots = dp.generate_v_dots(y_input.get('1.0', 'end-1c'))
    
    labels = numb_input.get('1.0', 'end-1c')
    labels = labels.split('\n')

    h_dots.pop()
    v_dots.pop()
    labels.pop()

    h_coords = []
    v_coords = []
    
    
    
    for position in h_dots:
        h_coords.append(dp.decode_x_coordinate(position))
    
    for position in v_dots:
        v_coords.append(dp.decode_y_coordinate(position))
    
    # try:
    field.football_field(h_coords, v_coords, labels,
    do_auto_zoom.get(), do_arrows.get(), line_color.get())
    # except:
    #     throw_error()
        

# Initialize main window

window = Tk()
window.title('Auto Pathway')
window.resizable(False, False)

Label(window,
      text = 'Copy and paste directly from your drill sheet'
      ).grid(row = 0, column = 1, sticky = N)

# Window that will appear when an error occurs

def throw_error():
    error_window = Toplevel(window)
    error_window.geometry('400x100')
    error_window.title('Error :(')
    Label(error_window,
    text = 'Something went wrong and a pathway was unable to be created'
    ).grid(row = 0, column = 0)

# Draw and label the text boxes for user input

Label(window, text = 'Labels').grid(row = 1, column = 0)
numb_input = Text(window, width = 20, height = 20)
numb_input.grid(row = 2, column = 0)

Label(window, text = 'Side 1 - Side 2').grid(row = 1, column = 1)
x_input = Text(window, width = 20, height = 20)
x_input.grid(row = 2, column = 1)

Label(window, text = 'Front - Back').grid(row = 1, column = 2)
y_input = Text(window, width = 20, height = 20)
y_input.grid(row = 2, column = 2)

# Customization checkboxes

do_auto_zoom = BooleanVar(window)
do_arrows = BooleanVar(window)

do_auto_zoom.set(True)
do_arrows.set(True)

check_auto_zoom = Checkbutton(window,
                             text = 'Auto Zoom',
                             onvalue = True,
                             offvalue = False,
                             variable = do_auto_zoom)
check_auto_zoom.grid(row = 3, column = 0, sticky = 'W')

check_arrows = Checkbutton(window,
                           text = 'Show Arrows',
                           onvalue = True,
                           offvalue = False,
                           variable = do_arrows)
check_arrows.grid(row = 4, column = 0, sticky = 'W')

# Customization drop-down menus:

valid_colors = ['Black',
                'Red',
                'Orange',
                'Yellow',
                'Green',
                'Blue',
                'Purple']

line_color = StringVar(window)
line_color.set('Blue')

Label(window, text = 'Line Color:'
     ).grid(row = 4, column = 1, sticky = 'E')

color_selection = OptionMenu(window, line_color, *valid_colors)
color_selection.grid(row = 4,column = 2, sticky='ew')

# Go button

Button(window,
       text = 'Generate',
       width = 6,
       command = generate_pathway
       ).grid(row = 5, column = 1)

window.mainloop()