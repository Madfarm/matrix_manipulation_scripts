import numpy as np


def generate_signal(frequency, amplitude, phase, sample_rate, duration):
    """
    Generate a sinusoidal signal with the given frequency, amplitude, phase, sample rate, and duration.


    Parameters:
    frequency (float): The frequency of the signal in Hz.
    amplitude (float): The amplitude of the signal.
    phase (float): The phase of the signal in radians.
    sample_rate (int): The sample rate of the signal in Hz.
    duration (float): The duration of the signal in seconds.


    Returns:
    numpy.ndarray: The generated signal.
    """
    time = np.arange(0, duration, 1/sample_rate)
    signal = amplitude * np.sin(2 * np.pi * frequency * time + phase)
    return signal


def dft(signal):
    """
    Compute the Discrete Fourier Transform (DFT) of the given signal.


    Parameters:
    signal (numpy.ndarray): The input signal.


    Returns:
    numpy.ndarray: The DFT of the signal.
    """
    n = len(signal)
    dft = np.zeros(n, dtype=complex)
    for k in range(n):
        for t in range(n):
            dft[k] += signal[t] * np.exp(-2j * np.pi * k * t / n)
    return dft


def visualize_ascii(signal):
    """
    Visualize the given signal using ASCII art.


    Parameters:
    signal (numpy.ndarray): The input signal.


    Returns:
    str: The ASCII art representation of the signal.
    """
    ascii_art = ""
    for value in signal:
        if value > 0:
            ascii_art += "*"
        else:
            ascii_art += " "
    return ascii_art


# Generate a signal
frequency = 10  # Hz
amplitude = 1
phase = 0  # radians
sample_rate = 100  # Hz
duration = 1  # second
signal = generate_signal(frequency, amplitude, phase, sample_rate, duration)


# Compute the DFT of the signal
dft_signal = dft(signal)


# Visualize the signal using ASCII art
ascii_art = visualize_ascii(dft_signal)


# Validate that the ASCII art is a string
assert isinstance(ascii_art, str), "ASCII art must be a string"


# Print the ASCII art
print(ascii_art)