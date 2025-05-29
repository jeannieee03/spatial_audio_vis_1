import numpy as np
from scipy.io import wavfile

from analysis import waveform, fft_analysis, itd_analysis, rms_analysis, moving_avg

rate, data = wavfile.read('sample1.wav')
left = data[:, 0]
right = data[:, 1]
t = np.linspace(0, len(left) / rate, num=len(left))

waveform.plot_waveform(t, left, right)
fft_analysis.plot_fft(left, rate)
itd_analysis.calculate_itd(left, right, rate)
rms_analysis.plot_rms(t, left, right)
moving_avg.plot_moving_average(t, left, right)
