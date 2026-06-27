# Sequences
In discrete time, signals are represented as sequences of numbers $x[n]$, where $n$ is an integer representing the $n^{\text{th}}$ element of the sequence.
In general, this sequence is obtained from an analog signal through periodic sampling:

$$
x[n]=x_a(nT_s)
$$

$T_s$ is called the sampling period. Sometimes we also use the sampling frequency, which is its reciprocal: $f_s=1/T_s$. For this reason, the $n^{\text{th}}$ element of the sequence is generally called a **sample**.

# Basic sequence operations
The following operations are defined for discrete-time sequences:
- **Sum of sequences** (sample-by-sample): $x+y \rightarrow x[n]+y[n]$
- **Product of sequences** (sample-by-sample): $x\cdot y\rightarrow x[n]\cdot y[n]$ 
- **Multiplication by a constant**: $\alpha \cdot x \rightarrow \alpha \cdot x[n]$
- **Delay**: $y[n]=x[n-n_0]$ (the sequence $y$ is a shifted version of the sequence $x$)

# Basic sequences

- **Unit sample sequence (impulse)**:
  
  $$
  \delta[n]= \begin{cases} 1 & \\text{if } n = 0 \\\\ 0 & \\text{if } n \\neq 0 \end{cases}
  $$
  
  **Important!** Each sequence can be seen as a sum of discrete impulses scaled and delayed: $x[n]=\sum_{k=-\infty}^{\infty} x[k]\delta[n-k]$

- **Unit step sequence**:
  
  $$
  u[n]= \begin{cases} 1 & \\text{if } n \\geq 0 \\\\ 0 & \\text{if } n < 0 \end{cases}
  $$

  **Relation with impulse**: $u[n]=\sum_{k=-\infty}^{n} \delta[k]$ or $u[n]=\sum_{k=0}^{\infty} \delta[n-k]$

- **Real exponential sequences**:
  
  $$
  x[n]=A\alpha^n \qquad A,\alpha \in \mathbb{R}
  $$
  
- **Sinusoidal sequences**:

  $$
  x[n]=A \cos(\omega_0n+\phi) \qquad A,\omega_0 \in \mathbb{R}
  $$

  **Properties**:
  - **Frequency periodicity**: $A \cos[(\omega_0+2\pi r) n+\phi] = A \cos(\omega_0n+\phi) \quad r\in\mathbb{Z}$ 
  - **Time periodicity**: A discrete signal is periodic with period $N$ if and only if $N = \frac{2\pi k}{\omega_0}$ is an integer ($k \in \mathbb{Z}$).
  
  **Important!** Combining these two properties, we can state that in the discrete world, if we set a periodicity $N$, we can have only $w_k =\frac{2\pi k}{N}$ with $k=0, 1, \dots, N-1$ distinguishable frequencies.

- **Complex exponential sequences**:

  $$
  x[n]=A\alpha^n=|A||\alpha|^ne^{j(\omega_0n+\phi)} \qquad A,\alpha \in \mathbb{C}, \quad \omega_0,\phi \in \mathbb{R}
  $$

  *See the code "Complex exponential sequences"*
