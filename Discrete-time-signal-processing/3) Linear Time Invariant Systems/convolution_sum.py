# This is a script that calculates the convolution sum of two discrete-time signals.
import numpy as np
import matplotlib.pyplot as plt
def convolution_sum(input_signal, impulse_response):
    """
    Calculate the convolution sum of two discrete-time signals.

    Parameters:
    input_signal (array-like): The input signal.
    impulse_response (array-like): The impulse response of the system.

    Returns:
    numpy.ndarray: The output signal after convolution.
    """

    # Calculate the length of the output signal
    output_length = len(input_signal) + len(impulse_response) - 1  
    output_signal = np.zeros(output_length)

    # Perform the convolution sum
    for n in range(output_length):
        for k in range(len(impulse_response)):
            if 0 <= n - k < len(impulse_response):
                output_signal[n] +=input_signal[k] * impulse_response[n - k]
    return output_signal


# Create test function to verify the convolution sum implementation

def test_convolution_sum():
    # Define a simple input signal and impulse response
    input_signal = np.array([1, 2, 3])
    impulse_response = np.array([0, 1, 0.5])

    # Calculate the expected output using numpy's built-in convolution function
    expected_output = np.convolve(input_signal, impulse_response)

    # Calculate the output using the custom convolution_sum function
    output_signal = convolution_sum(input_signal, impulse_response)

    # Check if the output matches the expected output
    assert np.allclose(output_signal, expected_output), "Test failed: Output does not match expected result."
    print("Test passed: Output matches expected result.")

def main():
    # Example usage
    input_signal = np.array([1, 2, 3])
    impulse_response = np.array([0, 1, 0.5])
    output_signal = convolution_sum(input_signal, impulse_response)
    print("Input Signal:", input_signal)
    print("Impulse Response:", impulse_response)
    print("Output Signal (Convolution Sum):", output_signal)

    # plot the input signal, impulse response, and output signal
    n = np.arange(len(input_signal))
    m = np.arange(len(impulse_response))
    p = np.arange(len(output_signal))

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.stem(n, input_signal)
    plt.xlabel('n')
    plt.ylabel('x(n)')
    plt.title('Input Signal')

    plt.subplot(1, 3, 2)
    plt.stem(m, impulse_response)
    plt.xlabel('n')
    plt.ylabel('h(n)')
    plt.title('Impulse Response')

    plt.subplot(1, 3, 3)
    plt.stem(p, output_signal)
    plt.xlabel('n')
    plt.ylabel('y(n)')
    plt.title('Output Signal')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    test_convolution_sum()
    main()