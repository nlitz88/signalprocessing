from math import exp
import numpy as np
import matplotlib.pyplot as plt

def delay(between, load):
    return between*(exp(load) - 1)

def throughput(load):
    return load*exp(-load)


load_vals = np.linspace(0,5,51)
d_out = np.zeros(len(load_vals))
tp_out = np.zeros(len(load_vals))

for i, load in enumerate(load_vals):
    d_out[i] = delay(4, load)
    tp_out[i] = throughput(load)

plt.figure(1)
plt.plot(tp_out, d_out)
plt.xlabel("Throughput (Frames/slot)")
plt.ylabel("Delay (# Slots)")
plt.title("Delay vs Throughput")
# plt.xlim(-3,3)
plt.show()