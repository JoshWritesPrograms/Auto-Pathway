import matplotlib
matplotlib.use('tkagg') # Needed for Tkinter compatability

import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# This graph is modeled such that one unit on the chart
# is one 8 to 5 step (22.5 inches).
# Measured in steps, a football field is
# 160 along the x axis and 80 along the y axis.
# High school hashes would be at y = 28 and y = 52.
# There are 8 steps between every yard line.

def football_field(x_coordinates: list, y_coordinates: list,
                   do_auto_zoom: bool = True, do_arrows: bool = True,
                   line_color: str = 'red'):

    # Draw ard lines

    for i in range(1,21):
        ax.axvline(x = i * 8)

    # Draw hash lines

    ax.axhline(y = 28, ls = '--')
    ax.axhline(y = 52, ls = '--')

    # Label yard lines

    for i in range(2, 12, 2):
        # From 10 to 50
        ax.text(i * 8, 14, str(i * 5), fontsize = 'small')
        ax.text(i * 8, 68, str(i * 5), fontsize = 'small')

    for i in range(12, 20, 2):
        # From 40 to 10
        ax.text(i * 8, 14, str(100 - i * 5), fontsize = 'small')
        ax.text(i * 8, 68, str(100 - i * 5), fontsize = 'small')

    # Graph the points

    plt.plot(x_coordinates, y_coordinates, marker = '.', color = line_color)

    # Draw direction arrows 

    if do_arrows:
        for i in range(0, len(x_coordinates) - 1):
            plt.quiver(x_coordinates[i], 
            y_coordinates[i],
            x_coordinates[i+1] - x_coordinates[i],
            y_coordinates[i+1] - y_coordinates[i])
    

        
    # Draw major grid (4 step intervals)

    ax.set_xticks(range(0, 160, 4))
    ax.set_yticks(range(0, 80, 4))
    ax.grid(which = 'major',
            b = True,
            visible = True,
            linewidth = 1,
            alpha = 0.5)

    # Draw minor grid (1 step intervals)

    ax.set_xticks(range(0, 160, 1), minor = True)
    ax.set_yticks(range(0, 80, 1), minor = True)
    ax.grid(which = 'minor',
            visible = True,
            linewidth = 0.5,
            alpha = 0.25)
    
    # Hide ticks

    ax.axes.xaxis.set_ticklabels([])
    ax.axes.yaxis.set_ticklabels([])

    # Define boundaries

    if do_auto_zoom:
        plt.xlim(min(x_coordinates) - 8, max(x_coordinates) + 8)
        plt.ylim(min(y_coordinates) - 8, max(y_coordinates) + 8)
    else:
        plt.xlim(0, 160)
        plt.ylim(0, 80)

    ax.set_aspect(1)


    plt.show()


if __name__ == '__main__':
    print('This module is not meant to be executed as a program.')