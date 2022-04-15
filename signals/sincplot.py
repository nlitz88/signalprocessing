import numpy as np
import matplotlib.pyplot as plt
from math import pi

w = np.linspace(-20000*pi, 20000*pi, 100000)
x_w = np.sinc(w)
for idx, x in enumerate(x_w):
    x_w[idx] = 20000*x_w[idx] / (x_w[idx]/20000)

plt.plot(w, x_w)
plt.xlabel("w == radian Frequency")
plt.ylabel("|X(w)| == Magnitude")
plt.title("Sinc")
# plt.xlim(-1/(20000*pi), 1/(20000*pi))
plt.xlim(-100, 100)
# plt.xticks(np.linspace(-.001,.001, num=11))
plt.ylim(19999, 1999.9999)
# plt.yticks(np.linspace(-.2, -.5, 20))
# plt.legend()
# Finally, show the plot.
plt.show()
print(x_w[1])