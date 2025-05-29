import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

def plot_fft(signal, rate):
    n = len(signal)
    yf = fft(signal)
    xf = fftfreq(n, 1 / rate)

    plt.figure(figsize=(10, 4))
    plt.plot(xf[:n // 2], np.abs(yf[:n // 2]))
    plt.title('Frequency Spectrum (Left Channel)')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.tight_layout()
    plt.show()
