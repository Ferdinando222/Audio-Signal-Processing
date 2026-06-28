# This is an algorithm that calculates the moving average of 
# a discrete-time signal.

# The moving average filter can be seen as a low-pass filter
# that smooths out short-term fluctuations and highlights longer-term
#  trends in the data. On the other hand, if you increase too much the window
# you will lose the high frequency components of the signal, and the 
# output will be a very smooth signal.

import numpy as np

def moving_average(signal, left_bound, right_bound):
    """
    Calculate the moving average of a discrete-time signal.

    Parameters:
    signal (array-like): The input signal.
    window_size (int): The size of the moving average window.

    Returns:
    numpy.ndarray: The signal with the moving average applied.
    """
    output = np.zeros(len(signal))


    for i in range(len(signal)):
        if i < left_bound:
            output[i] = np.mean(signal[:i + right_bound + 1])
        elif i >= len(signal) - right_bound:
            output[i] = np.mean(signal[i - left_bound:])
        else:
            output[i] = np.mean(signal[i - left_bound:i + right_bound + 1])

    return output

def main():
    # Example usage
    import matplotlib.pyplot as plt
    
    # Define a sinusoidale signal with high noise
    t = np.linspace(0, 1, 100)
    sinusoid = np.sin(2 * np.pi * 5 * t) 
    noise = 0.5 * np.random.randn(len(t))
    signal = sinusoid + noise
    left_bound = 10
    right_bound = 10
    averaged_signal = moving_average(signal, left_bound, right_bound)

    # plot the original and averaged signals

    plt.figure(figsize=(10, 5))
    plt.plot(t, signal, label='Original Signal', alpha=0.5)
    plt.plot(t, averaged_signal, label='Moving Average', color='red')
    plt.plot(t, sinusoid, label='Original Sinusoid', color='green', linestyle='--')
    plt.title('Moving Average of a Noisy Signal')   
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
