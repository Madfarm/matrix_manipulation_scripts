import numpy as np


def generate_signal(frequency, sampling_rate, duration):
    time = np.arange(0, duration, 1/sampling_rate)
    signal = np.sin(2 * np.pi * frequency * time)
    return signal


def dft(signal):
    n = len(signal)
    frequencies = np.arange(n)
    fourier_transform = np.zeros(n, dtype=complex)
    for frequency in frequencies:
        fourier_transform[frequency] = np.sum(signal * np.exp(-2j * np.pi * frequency * np.arange(n) / n))
    return fourier_transform


def visualize_fourier_transform(fourier_transform):
    magnitude = np.abs(fourier_transform)
    max_magnitude = np.max(magnitude)
    ascii_art = ''
    for value in magnitude:
        ascii_art += '*' * int(value / max_magnitude * 50) + '\n'
    assert isinstance(ascii_art, str), "ASCII art must be a string."
    return ascii_art


# Generate a complex sinusoidal signal
sampling_rate = 1000
duration = 1
signal1 = generate_signal(5, sampling_rate, duration)
signal2 = generate_signal(10, sampling_rate, duration)
signal = signal1 + signal2


# Perform DFT
fourier_transform = dft(signal)


# Visualize the Fourier Transform
ascii_art = visualize_fourier_transform(fourier_transform)
print(ascii_art)