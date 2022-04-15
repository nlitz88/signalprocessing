# Quick note: had to change vscode's interpreter to use the virtual environment's python binary instead of the system's python binary.
# It can therefore resolve the imports from the local venv!
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# 6B -- Plotting |X(w)|
w = np.linspace(-50,50, 201)
x_w = np.sinc((w)/(2*pi))
for i in range(len(x_w)):
    x_w[i] = abs(x_w[i])

# Setup plot for figure 1.
plt.figure(1)
plt.plot(w, x_w)
plt.axhline(0, color='black')
# plt.axvline(2*pi, color='black')
plt.xlabel("radian frequency, w")
plt.ylabel("|X(w)| == Magnitude of x(t)'s spectrum")
plt.title("|X(w)| vs frequency")
# plt.show()

# 6C -- Plotting |Y(w)|
y_w = np.sinc((w-pi)/(2*pi)) + np.sinc((w+pi)/(2*pi))
for i in range(len(y_w)):
    y_w[i] = abs(y_w[i])

# Setup plot for figure 2.
plt.figure(2)
plt.plot(w, y_w)
plt.xlabel("radian frequency, w")
plt.ylabel("|Y(w)| == Magnitude of y(t)'s spectrum")
plt.title("|Y(w)| vs frequency")
plt.show()