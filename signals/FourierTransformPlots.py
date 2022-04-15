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
# plt.axhline(0, color='black')
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

# # Now plot the magnitude of each of these in db.
# x_w_db = 20*np.log10(x_w)
# y_w_db = 20*np.log10(y_w)
# plt.figure(3)
# # plt.plot(w, x_w, label="X(w)")
# # plt.plot(w, y_w_db, label="Y(w)")
# # Plotting the log of the magnitudes, therefore plot against log10 of the x-axis (semilog).
# plt.semilogx(w, x_w_db, label="X(w)")
# plt.semilogx(w, y_w_db, label="Y(w)")
# plt.legend()
# plt.xlabel("radian frequency, w")
# plt.title("|X(w)| and |Y(w)| in db vs w")

# plt.show()

# Now, use python to compute the Fourier Transforms of each of these manually, as opposed to by hand.
# Plot the resulting spectrums. THEN, plot their magnitude in dB to observe which actually has higher frequencies.
t = np.linspace(-50,50,1001)
x_t = np.heaviside(t+0.5, 0.5) - np.heaviside(t-0.5, 0.5)
plt.figure(3)
plt.plot(t, x_t)
plt.xlabel("time t")
plt.ylabel("x(t)")
plt.title("x(t) vs t")
plt.xlim(-3,3)

y_t = (1+np.cos(pi*t))*x_t
plt.figure(4)
plt.plot(t, y_t)
plt.xlabel("time t")
plt.ylabel("y(t)")
plt.title("y(t) vs t")
plt.xlim(-3,3)

# Now, take the fourier transform of each of these signals and plot their spectrums.
x_f = np.fft.fft(x_t)
y_f = np.fft.fft(y_t)

# sampling rate = 10 == 0->50s, 500 samples.


# f = np.linspace(0,50, 501)
f = np.fft.fftfreq(len(x_f), d=0.1)
np.fft.fftshift(f)

for i in range(len(x_f)):
    x_f[i] = abs(x_f[i])

for i in range(len(y_f)):
    y_f[i] = abs(y_f[i])

print(len(x_f))
print(len(f))

# Setup plot for next figure.
plt.figure(5)
plt.scatter(f, x_f)
plt.xlabel("frequency f")
plt.ylabel("|X(f)| == Magnitude of x(t)'s spectrum")
plt.title("|X(f)| vs frequency")

# Setup plot for next figure.
plt.figure(6)
plt.scatter(f, y_f)
plt.xlabel("frequency f")
plt.ylabel("|Y(f)| == Magnitude of y(t)'s spectrum")
plt.title("|Y(f)| vs frequency")

plt.show()
plt.close('all')