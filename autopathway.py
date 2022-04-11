import dotprocessing as dp
import field
from tkinter import *

# Initialize main window

window = Tk()

window.title('Auto Pathway')

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

Label(window, text = 'Side 1 - Side 2').grid(row = 1, column = 0)
x_input = Text(window, width = 20, height = 20)
x_input.grid(row = 2, column = 0)

Label(window, text = 'Front - Back').grid(row = 1, column = 2)
y_input = Text(window, width = 20, height = 20)
y_input.grid(row = 2, column = 2)

# Main function (triggered by button)

def generate_pathway():
    h_dots = dp.generate_h_dots(x_input.get('1.0', 'end-1c'))
    v_dots = dp.generate_v_dots(y_input.get('1.0', 'end-1c'))
    
    h_dots.pop()
    v_dots.pop()
    
    h_coords = []
    v_coords = []
    
    for position in h_dots:
        h_coords.append(dp.decode_x_coordinate(position))
    
    for position in v_dots:
        v_coords.append(dp.decode_y_coordinate(position))
    
    try:
        field.football_field(h_coords, v_coords)
    except:
        throw_error()


Button(window,
       text = 'Generate',
       width = 6,
       command = generate_pathway
       ).grid(row = 3, column = 1)

window.mainloop()