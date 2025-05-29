import numpy as np
from scipy.signal import correlate

def calculate_itd(left, right, rate):
    corr = correlate(left, right, mode='full')
    lags = np.arange(-len(left) + 1, len(right))
    lag = lags[np.argmax(corr)]
    delay_sec = lag / rate
    print(f"[ITD] Estimated delay between channels: {delay_sec:.6f} seconds")
