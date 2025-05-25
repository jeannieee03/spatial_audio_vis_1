import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

rate, data = wavfile.read('sample1.wav')  

left = data[:, 0]
right = data[:, 1]

t = np.linspace(0, len(left) / rate, num=len(left))

plt.figure(figsize=(10, 4))
plt.plot(t, left, label='Left Channel')
plt.plot(t, right, label='Right Channel', alpha=0.7)
plt.title('Stereo Audio Waveform')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
