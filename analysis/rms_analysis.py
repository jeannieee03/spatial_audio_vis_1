import numpy as np
import matplotlib.pyplot as plt

def plot_rms(t, left, right, window_size=1000):
    left_rms = np.sqrt(np.convolve(left**2, np.ones(window_size)/window_size, mode='valid'))
    right_rms = np.sqrt(np.convolve(right**2, np.ones(window_size)/window_size, mode='valid'))
    t_rms = t[:len(left_rms)]

    plt.figure(figsize=(10, 4))
    plt.plot(t_rms, left_rms, label='Left RMS')
    plt.plot(t_rms, right_rms, label='Right RMS')
    plt.title('RMS Amplitude over Time')
    plt.xlabel('Time [s]')
    plt.ylabel('RMS Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.show()
