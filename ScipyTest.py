import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

sig = np.repeat(1, 100)
win = np.arange(100)
filtered = signal.convolve(sig, win, mode='same') / sum(win)

fig, (ax_orig, ax_win, ax_filt) = plt.subplots(3, 1, sharex=True)
ax_orig.plot(sig)
ax_orig.set_title('Original pulse, unitary step')
ax_orig.margins(0, 0.1)
ax_win.plot(win)
ax_win.set_title('Filter impulse response, ramp')
ax_win.margins(0, 0.1)
ax_filt.plot(filtered)
ax_filt.set_title('Filtered signal, result of the convolution')
ax_filt.margins(0, 0.1)
fig.tight_layout()
fig.show()
plt.show()