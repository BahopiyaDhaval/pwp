import numpy as np

def analyze_system():
    # H(z) = 0.5 (z - 0.7)(z - 0.9) / ((z - 0.6)(z - 0.4))

    # Zeros from numerator factors
    zeros = np.array([0.7, 0.9], dtype=complex)

    # Poles from denominator factors
    poles = np.array([0.6, 0.4], dtype=complex)

    print("Zeros:", zeros)
    print("Poles:", poles)

    # Stability: all poles must satisfy |p| < 1
    if np.all(np.abs(poles) < 1):
        print("System is Stable")
    else:
        print("System is Unstable")

analyze_system()
