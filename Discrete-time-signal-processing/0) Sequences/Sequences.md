# Sequences
In the discrete time, the signals are represented as sequences of numbers $x[n]$, where $n$ is an integer and it represent the $n^{th}$ number of the sequence.
In general this sequence is obtained from an analog signal with a periodic sampling.
$$
    x[n]=x_a(nT_s)
$$

$T_s$ is called the sampling period. Some time we use also the sampling frequency that is the reciprocal: $f_s=1/T_s$. For this reason in general we call the $n^{th}$ elemnt of the sequence as a **sample**.

# Basic sequence operations
For discrete time sequence are defined the following operations.
- Sum of sequences (sample-by-sample): $x+y \rightarrow x[n]+y[n]$
- Product of sequences (sample-by-sample): $x\cdot y\rightarrow x[n]\cdot y[n]$ 
- Multiplication for a constant: $\alpha \cot x\rightarrow \alpha \cdot x[n]$
- Delay: $y[n]=x[n-n_0]$ (the sequence $y$ will be a shifted version of the $x$ sequence)

# Basic sequence

- Unit sample sequece (impulse):
  $$
  \delta[n]= \begin{cases} 1 & \text{if } n \neq 0 \\ 0 & \text{if } n = 0 \end{cases}
  $$

  **Important!**
  Each sequence can be seen as a sum of discrete impulses scaled and delayed: $x[n]=\sum_{k=-\infty}^{\infty} x[k]\delta[n-k]$
- Unit step sequence:
  $$
  u[n]= \begin{cases} 1 & \text{if } n \geq 0 \\ 0 & \text{if } n < 0 \end{cases}
  $$
  **Relation with impulse**
  $u[n]=\sum_{k=-\infty}^{n} \delta[k]$  or  $u[n]=\sum_{k=0}^{\infty} \delta[n-k]$
- Real exponential sequences:
  $$
  x[n]=A\alpha^n \qquad     A,\alpha \in  \mathbb{R}
  $$
- Sinusoidal sequences:
  $$
  x[n]=A cos(\omega_0n+\phi) \qquad  A,\omega_0 \in \mathbb{R}
  $$
  Properties:
  - Frequency periodicity: $A cos[(\omega_0+2\pi r) n+\phi] = Acos(\omega_0n+\phi) \quad r\in\mathbb{N}$ 
  - Time periodicity: A discrete signal is periodic of N if and only if $N = \frac{2\pi k}{\omega_0}$ is an integer
  
  **Important!**
  Combining these two properties we can say that in the discrete world if we set a periodicity N, we can have only $w_k =\frac{2\pi k}{N}$ with $k=1,...,N-1$ distinguinshable frequencies
- Complex exponential sequences
  $$
  x[n]=A\alpha^n=|A||\alpha_r|^ne^{j\omega_0n+\phi} \qquad     A,\alpha \in  \mathbb{C} \quad \alpha_r\in\mathbb{R}
  $$
  **See the code "Complex exponential sequences"**