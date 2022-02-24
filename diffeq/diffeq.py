import numpy as np
import matplotlib.pyplot as plt

# unit step function. Returns a unit step signal as array of signal values,
# provided an axis array (axis) and time shift (d).
def unit_step(axis, d):
    res_sig = np.zeros(len(axis))
    for n in axis:
        if n < d:
            res_sig[n] = 0
        else:
            res_sig[n] = 1
    return res_sig

# Discrete time unit impulse (delta) signal. Returns a unit impulse signal as an
# array of signal values, provided an axis array (axis) and timeshift (d).
def unit_imp(axis, d):
    res_sig = np.zeros(len(axis))
    for n in axis:
        if n != d:
            res_sig[n] = 0
        else:
            res_sig[n] = 1
    return res_sig

# Unit step functional value: This just returns the functional value of a unit step
# signal at a sample n. Time shifts should be applied directly to n.
def unit_step_val(n):
    if n < 0:
        return 0
    else:
        return 1

# Similarly, a unit impulse signal value function. Returns functional value of discrete
# time delta signal at sample number n.
def unit_imp_val(n):
    if n != 0:
        return 0
    else:
        return 1

# Define the main function that I am plotting y[n]. This function calculates the functional
# value of the signal y[n] for every n it is provided. It returns the value of y at n.
def y_n(n, y_arr):
    # Initial conditions for y
    if n == -1 or n == -2:
        return 2
    # Otherwise, return the value of y according to the formula.
    return (1/3)*y_arr[n-1] - (1/2)*y_arr[n-2] + unit_imp_val(n) + unit_step_val(n-50)

# main section. Define time range with upper and lower limits.
LL = 0
UL = 100
# Creates np.array with values 0, to 100, with step 1. This serves as our discrete time axis.
n_axis = np.arange(LL, UL+1, 1)

y = np.zeros(len(n_axis))
# Now, we'll generate the signal y[n] as a parallel numpy array.
for n in n_axis:
    y[n] = y_n(n, y)
# Then, plot each y value at the corresponding n value from n_axis.
plt.stem(n_axis, y)
# Configure the plot.
plt.xlabel("n")
plt.ylabel("y[n]")
plt.title("#10 - Recursively Solving Given Difference Eq")
# plt.xticks(n)
plt.yticks(np.linspace(0.0, 2.0, 5))
# Finally, show the plot.
plt.show()

# Now, generate a basic unit step signal.
# unit = unit_step(n, 4)
# Then, plot using matplotlib.
# The stem function creates a stem plot. Draws lines perpendicular to a baseline
# at each location, locks.
# plt.stem(n, unit)
# So, we're plotting the nth value of unit at the nth loc.