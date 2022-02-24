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

# Define the main function that I am plotting y[n].
def y_n(n, d):
    sig = (1/3)*y_n(n, -1)

# main section. Define time range with upper and lower limits.
LL = 0
UL = 100
# Creates np.array with values 0, to 100, with step 1. This serves as our discrete time axis.
n = np.arange(LL, UL+1, 1)

# Now, generate a basic unit step signal.
unit = unit_step(n, 4)

# Then, plot using matplotlib.
# The stem function creates a stem plot. Draws lines perpendicular to a baseline
# at each location, locks.
plt.stem(n, unit)
# So, we're plotting the nth value of unit at the nth loc.

