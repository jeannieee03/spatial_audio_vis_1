import matplotlib.pyplot as plt

def plot_waveform(t, left, right):
    plt.figure(figsize=(10, 4))
    plt.plot(t, left, label='Left Channel')
    plt.plot(t, right, label='Right Channel', alpha=0.7)
    plt.title('Stereo Audio Waveform')
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.tight_layout()
    plt.show()
