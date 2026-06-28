# Sequences
In the discrete time, the signals are represented as sequences of numbers $x[n]$, where $n$ is an integer and it represent the $n^{th}$ number of the sequence.
In general this sequence is obtained from an analog signal with a periodic sampling.

```math
x[n]=x_a(nT_s)
```

$T_s$ is called the sampling period. Some time we use also the sampling frequency that is the reciprocal: $f_s=1/T_s$. For this reason in general we call the $n^{th}$ element of the sequence as a **sample**.

# Basic sequence operations
For discrete time sequence are defined the following operations.
- Sum of sequences (sample-by-sample): $x+y \rightarrow x[n]+y[n]$
- Product of sequences (sample-by-sample): $x\cdot y\rightarrow x[n]\cdot y[n]$
- Multiplication for a constant: $\alpha \cdot x\rightarrow \alpha \cdot x[n]$
- Delay: $y[n]=x[n-n_0]$ (the sequence $y$ will be a shifted version of the $x$ sequence)

# Basic sequences
- **Unit sample sequence (impulse)**:

```math
\delta[n]=
\begin{cases}
1 & \text{if } n = 0 \\
0 & \text{if } n \neq 0
\end{cases}
```

  > **Important!**  
  > Each sequence can be seen as a sum of discrete impulses scaled and delayed:
  ```math
  x[n]=\sum_{k=-\infty}^{\infty} x[k]\delta[n-k]
  ```

- **Unit step sequence**:

```math
u[n]=
\begin{cases}
1 & \text{if } n \geq 0 \\
0 & \text{if } n < 0
\end{cases}
```

  > **Relation with impulse**
  ```math
  u[n]=\sum_{k=-\infty}^{n} \delta[k] \qquad \text{or} \qquad u[n]=\sum_{k=0}^{\infty} \delta[n-k]
  ```

- **Real exponential sequences**:

```math
x[n]=A\alpha^n \qquad A,\alpha \in \mathbb{R}
```

- **Sinusoidal sequences**:

```math
x[n]=A\cos(\omega_0 n+\phi) \qquad A,\omega_0 \in \mathbb{R}
```

  Properties:
  - Frequency periodicity: $A\cos[(\omega_0+2\pi r)n+\phi] = A\cos(\omega_0 n+\phi) \quad r\in\mathbb{N}$
  - Time periodicity: A discrete signal is periodic of $N$ if and only if $N = \dfrac{2\pi k}{\omega_0}$ is an integer.

  > **Important!**  
  > Combining these two properties we can say that in the discrete world, if we set a periodicity $N$, we can have only
  ```math
  \omega_k = \frac{2\pi k}{N} \qquad k=1,\ldots,N-1
  ```
  > distinguishable frequencies.

- **Complex exponential sequences**:

```math
x[n]=A\alpha^n=|A||\alpha_r|^n e^{j(\omega_0 n+\phi)} \qquad A,\alpha \in \mathbb{C},\quad \alpha_r\in\mathbb{R}
```

  > **See the code "Complex exponential sequences"**
