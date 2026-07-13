| No. | Sequence | Fourier Transform |
| :--- | :--- | :--- |
| **1.** | $\delta[n]$ | $1$ |
| **2.** | $\delta[n - n_0]$ | $e^{-j\omega n_0}$ |
| **3.** | $1 \quad (-\infty < n < \infty)$ | $\displaystyle\sum_{k=-\infty}^{\infty} 2\pi\delta(\omega + 2\pi k)$ |
| **4.** | $a^n u[n] \quad (\lvert a \rvert < 1)$ | $\displaystyle\frac{1}{1 - ae^{-j\omega}}$ |
| **5.** | $u[n]$ | $\displaystyle\frac{1}{1 - e^{-j\omega}} + \sum_{k=-\infty}^{\infty} \pi\delta(\omega + 2\pi k)$ |
| **6.** | $(n + 1)a^n u[n] \quad (\lvert a \rvert < 1)$ | $\displaystyle\frac{1}{(1 - ae^{-j\omega})^2}$ |
| **7.** | $\displaystyle\frac{r^n \sin\omega_p(n+1)}{\sin\omega_p}u[n] \quad (\lvert r \rvert < 1)$ | $\displaystyle\frac{1}{1 - 2r\cos\omega_p e^{-j\omega} + r^2 e^{-j2\omega}}$ |
| **8.** | $\displaystyle\frac{\sin\omega_c n}{\pi n}$ | $X(e^{j\omega}) = \begin{cases} 1, & \lvert\omega\rvert < \omega_c \\ 0, & \omega_c < \lvert\omega\rvert \le \pi \end{cases}$ |
| **9.** | $x[n] = \begin{cases} 1, & 0 \le n \le M \\ 0, & \text{otherwise} \end{cases}$ | $\displaystyle\frac{\sin[\omega(M+1)/2]}{\sin(\omega/2)} e^{-j\omega M/2}$ |
| **10.** | $e^{j\omega_0 n}$ | $\displaystyle\sum_{k=-\infty}^{\infty} 2\pi\delta(\omega - \omega_0 + 2\pi k)$ |
| **11.** | $\cos(\omega_0 n + \phi)$ | $\displaystyle\sum_{k=-\infty}^{\infty} \left[\pi e^{j\phi}\delta(\omega - \omega_0 + 2\pi k) + \pi e^{-j\phi}\delta(\omega + \omega_0 + 2\pi k)\right]$ |