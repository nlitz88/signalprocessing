import numpy as np
import matplotlib.pyplot as plt

# Goal: Plot efficiency as a function of p for different numbers of nodes N.

def efficiency(N, p):
    # Return the probability of the binomial random variable == 1 == a single node successfully transmitting.
    return N*p*((1-p)**(N-1))

# Plot efficiency vs p for a provided number of nodes, N. Returns array of efficiency values.
def for_each_efficiency(N, x_axis_arr):
    y = np.zeros(len(p_axis))
    # For each x in the range, calculate the efficiency.
    for i, p in enumerate(x_axis_arr):
        y[i] = efficiency(N, p)
    return y

# p_axis = probability value axis. f_p == the resulting efficiency.
p_axis = np.linspace(0, .5, num=100)
f_p_15 = for_each_efficiency(15, p_axis)
f_p_25 = for_each_efficiency(25, p_axis)
f_p_35 = for_each_efficiency(35, p_axis)

# Plot the resulting efficiency curves together.
plt.plot(p_axis, f_p_15, label="N=15")
plt.plot(p_axis, f_p_25, label="N=25")
plt.plot(p_axis, f_p_35, label="N=35")
# Configure the plot.
plt.xlabel("p")
plt.ylabel("efficiency")
plt.title("Efficiency vs p, Varying number of Nodes")
plt.xticks(np.linspace(0,.5, num=11))
plt.legend()
# plt.yticks(np.linspace(-1.5, 1.5, 7))
# Finally, show the plot.
plt.show()