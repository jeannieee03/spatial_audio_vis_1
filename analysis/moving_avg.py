import numpy as np
import matplotlib.pyplot as plt

def plot_moving_average(t, left, right, window_size=1000):
    left_avg = np.convolve(left, np.ones(window_size)/window_size, mode='valid')
    right_avg = np.convolve(right, np.ones(window_size)/window_size, mode='valid')
    t_avg = t[:len(left_avg)]

    plt.figure(figsize=(10, 4))
    plt.plot(t_avg, left_avg, label='Left Moving Avg')
    plt.plot(t_avg, right_avg, label='Right Moving Avg')
    plt.title('Moving Average of Amplitude')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.show()
