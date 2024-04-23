import numpy as np
import matplotlib.pyplot as plt


# Define the wave function
def psi(x):
    return np.exp(-(x**2)/2)


# Define the potential
def V(x):
    return x**2/2


# Define the time evolution operator
def U(x, t):
    return np.exp(-1j*V(x)*t)


# Define the ASCII art generator
def ascii_art(p):
    # Assert that p is a 1D numpy array
    assert isinstance(p, np.ndarray) and p.ndim == 1, "p must be a 1D numpy array"

    # Convert p to ASCII art
    ascii_art = ""
    for i in range(len(p)):
        ascii_art += "X" * int(p[i] * 100)
        ascii_art += "\n"


    # Assert that ascii_art is a string
    assert isinstance(ascii_art, str), "ascii_art must be a string"


    return ascii_art


# Set the parameters
N = 1000  # Number of points
L = 10    # Length of the system
dx = L/N  # Spatial step
dt = 0.01 # Time step
T = 10    # Total time


# Initialize the wave function
x = np.linspace(-L/2, L/2, N)
psi_x = psi(x)


# Evolve the wave function in time
for t in np.arange(0, T, dt):
    psi_x = psi_x.astype(complex) * U(x, t)


# Calculate the probability density
p = np.abs(psi_x)**2


# Generate the ASCII art
ascii_art_str = ascii_art(p)


# Print the ASCII art
print(ascii_art_str)