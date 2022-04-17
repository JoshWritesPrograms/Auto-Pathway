# Converts text copied and pasted from the PDF into
# a list of raw coords to be decoded.

def generate_h_dots(raw_text: str) -> list:
    h_dots = []

    raw_text = raw_text.strip('\n')
    h_dots = raw_text.split('yd ln')
    return h_dots

def generate_v_dots(raw_text: str) -> list:
    v_dots = []

    raw_text = raw_text.replace('line', '(HS)')
    raw_text = raw_text.strip('\n')
    v_dots = raw_text.split('(HS)')
    
    return v_dots

# Extracts the numbers from a string

def extract_numbers(string: str) -> list:
    number_list = []
    for n in string.split():
        try:
            number_list.append(float(n))
        except ValueError:
            pass
    return number_list

# Converts dots to cartesian coordinates

def decode_x_coordinate(x_position: str) -> float:
    x_coordinate = float(0)

    x_numbers = extract_numbers(x_position)

    if 'Side 1' in x_position:
        x_coordinate += (x_numbers[1] / 5) * 8

        if 'inside' in x_position:
            x_coordinate += x_numbers[0]
        elif 'outside' in x_position:
            x_coordinate -= x_numbers[0]
        else:
            pass
    
    elif 'Side 2' in x_position:
        x_coordinate += 160.00
        x_coordinate -= (x_numbers[1] / 5) * 8

        if 'inside' in x_position:
            x_coordinate -= x_numbers[0]
        elif 'outside' in x_position:
            x_coordinate += x_numbers[0]
        else:
            pass
    
    return x_coordinate


def decode_y_coordinate(y_position: str) -> float:
    y_coordinate = float(0)

    y_numbers = extract_numbers(y_position)

    if 'Front side' in y_position:
        pass
    elif 'Front Hash' in y_position:
        y_coordinate += 28
    elif 'Back Hash' in y_position:
        y_coordinate += 52
    else:
        y_coordinate += 80

    if 'front' in y_position:
        y_coordinate -= y_numbers[0]
    elif 'behind' in y_position:
        y_coordinate += y_numbers[0]
    else:
        pass

    return y_coordinate


if __name__ == '__main__':
    print('This module is not meant to be executed as a program.')