# Matplotlib is a popular open-source data visualization library for Python. It provides a wide range of tools for creating static, animated, and interactive visualizations in Python.

# Matplotlib provides a wide range of functionality for creating different types of plots and visualizations. Some of the key features of Matplotlib include:
# Line plots: used to plot continuous data as a series of connected points.
# Scatter plots: used to plot data points as individual dots or markers.
# Bar charts: used to plot categorical data as bars.
# Histograms: used to plot the distribution of a set of continuous data.
# Heatmaps: used to plot data as a color-coded grid.
# Contour plots: used to plot data as a series of contours or lines.

#line plot
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
# plt.plot(x,  y)
# plt.xlabel('x')
# plt.ylabel('sin(x)')
# plt.title('Line plot pf sin(x)')
# plt.show()

#scatter plot
# import  matplotlib.pyplot as plt
# import numpy as np
# x = np.random.randn(100)
# y = np.random.randn(100)
# plt.scatter(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Scatter plot of random data')
# plt.show()

#bar chart
# import matplotlib.pyplot as plt
# x = ['Apples', 'Bananas', 'Oranges']
# y =  [10, 15, 7]
# plt.bar(x, y)
# plt.xlabel('Fruits')
# plt.ylabel('Quantity')
# plt.title('Bar chart of fruits')
# plt.show()

#histogram
# import matplotlib.pyplot as plt
# import numpy as np
# data =  np.random.randn(1000)
# plt.hist(data, bins=30, density=True)
# plt.xlabel('Value')
# plt.ylabel('Probability')
# plt.title('Histogram of random data')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

# Create a figure and a 2x2 grid of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))  # 2 rows, 2 columns

# Plot on the first subplot (top-left)
axs[0, 0].plot(x, y1, 'r-', label='sin(x)')
axs[0, 0].set_title('Sine Function')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')
axs[0, 0].legend()

# Plot on the second subplot (top-right)
axs[0, 1].plot(x, y2, 'g-', label='cos(x)')
axs[0, 1].set_title('Cosine Function')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')
axs[0, 1].legend()

# Plot on the third subplot (bottom-left)
axs[1, 0].plot(x, y3, 'b-', label='tan(x)')
axs[1, 0].set_title('Tangent Function')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')
axs[1, 0].legend()
axs[1, 0].set_ylim([-10, 10])  # Limit y-axis to avoid extreme values

# Plot on the fourth subplot (bottom-right)
axs[1, 1].plot(x, y4, 'm-', label='exp(x/10)')
axs[1, 1].set_title('Exponential Function')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('y')
axs[1, 1].legend()

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()

