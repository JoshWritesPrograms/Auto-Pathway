import matplotlib.pyplot as plt
fig, ax = plt.subplots()

# This graph is modeled such that one unit on the chart
# is one 8 to 5 step (22.5 inches).
# Measured in steps, a football field is
# 160 along the x axis and 80 along the y axis.
# High school hashes would be at y = 28 and y = 52.
# There are 8 steps between every yard line.

# Define initial graph boundaries

plt.xlim(0, 160)
plt.ylim(0, 80)
ax.set_aspect(1)

# Draw yard lines

for i in range(1,21):
    ax.axvline(x = i * 8)

# Draw hash lines

ax.axhline(y = 28, ls = '--')
ax.axhline(y = 52, ls = '--')

# Label yard lines (Offset slightly left)

for i in range(2, 12, 2):
    # From 10 to 50
    ax.text(i * 8, 14, str(i * 5), fontsize = 'small')
    ax.text(i * 8, 68, str(i * 5), fontsize = 'small')

for i in range(12, 20, 2):
    # From 40 to 10
    ax.text(i * 8, 14, str(100 - i * 5), fontsize = 'small')
    ax.text(i * 8, 68, str(100 - i * 5), fontsize = 'small')

# Draw major grid (4 step intervals)

ax.set_xticks(range(0, 160, 4))
ax.set_yticks(range(0, 80, 4))
ax.grid(which = 'major',
        visible = True,
        linewidth = 1)

# Draw minor grid (1 step intervals)

ax.set_xticks(range(0, 160, 1), minor = True)
ax.set_yticks(range(0, 80, 1), minor = True)
ax.grid(which = 'minor',
        visible = True,
        linewidth = 0.5,
        alpha=.25)

# Hide ticks

ax.axes.xaxis.set_ticks([])
ax.axes.yaxis.set_ticks([])

# Show chart

plt.show()