# Frequency Representation

If we consider an input signal $x[n]=e^{j\omega n}$, we can show that if we put this into an LTI system with impulse response $h[n]$, the output signal $y[n]$ will be a scaled version of the same signal.

```math
y[n]=\sum_{k=-\infty}^{\infty}h[k]e^{j\omega (n-k)}
```
```math
y[n]=e^{j\omega n}\sum_{k=-\infty}^{\infty}h[k]e^{-j \omega k}
```

If we set

```math
H(e^{j \omega})=\sum_{k=-\infty}^{\infty}h[k]e^{-j\omega k}
```

then

```math
y[n]=H(e^{j \omega})e^{j\omega n}
```

$H(e^{j\omega})$ represents the **frequency response** and it is the eigenvalue associated with the eigenfunction $e^{j\omega n}$. The frequency response describes how the complex amplitude of the input signal changes as a function of the frequency $\omega$.

## Example 1: Frequency response of the delay system

Consider the delay system, whose impulse response is $h[n]=\delta[n-n_d]$. The frequency response is:

```math
H(e^{j\omega}) = \sum_{n=-\infty}^{\infty} \delta[n-n_d]e^{-j\omega n}=e^{-j\omega n_d}
```

Using the Euler relation:

```math
H_R(e^{j\omega})=\cos(\omega n_d)
```
```math
H_I(e^{j\omega})=-\sin(\omega n_d)
```

> **Important!**  
> The magnitude is $1$ and the phase is linear, $\omega n_d$.

## Example 2: Frequency response of a sinusoidal signal through an LTI system

Consider a sinusoidal signal:

```math
x[n]=A\cos(\omega_0 n + \phi)= \frac{A}{2} e^{j\omega_0 n}e^{j\phi}+\frac{A}{2} e^{-j\omega_0 n}e^{-j\phi}
```

The total response will be:

```math
y[n]=\frac{A}{2}\Big[H(e^{j\omega_0})e^{j\omega_0 n}e^{j\phi}+H(e^{-j\omega_0})e^{-j\omega_0 n}e^{-j\phi}\Big]
```
```math
y[n]=A|H(e^{j\omega_0})| \cos(\omega_0 n+\phi+\theta)
```

  > **Note**  
  > If $h[n]$ is real, then $H(e^{-j\omega_0})=H^*(e^{j\omega_0})$ and $\theta = \angle H(e^{j\omega_0})$.

## Important property in discrete time

In discrete time the frequency response is always a periodic function of the frequency, with period $2\pi$:

```math
H(e^{j(\omega+2\pi r)})= H(e^{j\omega}), \qquad r\in \mathbb{N}
```

# Fourier Transform

Considering the following notation:

```math
X(e^{j\omega}) = \mathcal{F}\{x[n]\}
```
```math
x[n] = \mathcal{F}^{-1}\{X(e^{j\omega})\}
```

where $\mathcal{F}$ is the Fourier Transform operator and $\mathcal{F}^{-1}$ is the Inverse Fourier Transform operator.

# Properties of the Fourier Transform

- **Linearity**:

```math
\mathcal{F}\{ax_1[n]+bx_2[n]\}=aX_1(e^{j\omega})+bX_2(e^{j\omega})
```

- **Time shifting**:

```math
\mathcal{F}\{x[n-n_d]\}=X(e^{j\omega})e^{-j\omega n_d}
```

- **Time reversal**:

```math
\mathcal{F}\{x[-n]\} = X(e^{-j\omega})
```

- **Differentiation in frequency**:

```math
\mathcal{F}\{nx[n]\} = j\frac{dX(e^{j\omega})}{d\omega}
```

- **Parseval's theorem**:

```math
E = \sum_{n=-\infty}^{\infty} |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 \, d\omega
```

- **Convolution theorem**:

```math
y[n] = \sum_{k=-\infty}^{\infty} x[k]h[n-k] = x[n] * h[n]
```
```math
Y(e^{j\omega}) = X(e^{j\omega})H(e^{j\omega})
```

- **Modulation theorem** (the opposite of convolution):

```math
y[n] = x[n]w[n]
```
```math
Y(e^{j\omega}) = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\theta})W(e^{j(\omega-\theta)}) \, d\theta
```

  > **Important!**  
  > In the discrete world the DTFT is periodic with period $2\pi$, so there is no perfect duality between convolution and multiplication as in continuous time. The rule is: a convolution in time corresponds to a multiplication of the spectra in frequency, but a multiplication in time does **not** correspond to an infinite convolution in frequency, due to the periodicity of the spectrum — instead a **periodic convolution** must be performed, computing the integral over a single period.