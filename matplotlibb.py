# Matplotlib is a popular open-source data visualization library for Python. It provides a wide range of tools for creating static, animated, and interactive visualizations in Python.

# Matplotlib provides a wide range of functionality for creating different types of plots and visualizations. Some of the key features of Matplotlib include:
# Line plots: used to plot continuous data as a series of connected points.
# Scatter plots: used to plot data points as individual dots or markers.
# Bar charts: used to plot categorical data as bars.
# Histograms: used to plot the distribution of a set of continuous data.
# Heatmaps: used to plot data as a color-coded grid.
# Contour plots: used to plot data as a series of contours or lines.

#line plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x,  y)
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Line plot pf sin(x)')
plt.show()

#scatter plot
import  matplotlib.pyplot as plt
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter plot of random data')
plt.show()






