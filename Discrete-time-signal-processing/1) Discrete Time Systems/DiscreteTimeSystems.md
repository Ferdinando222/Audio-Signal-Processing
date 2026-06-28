# Discrete Time Systems

A discrete time system is defined as:

```math
y[n]=T\{x[n]\}
```

where $T$ is a mathematical function that maps an input sequence $x[n]$ to the output sequence $y[n]$.

## Examples

- **Ideal delay system**:

```math
y[n]=x[n-n_d], \qquad -\infty<n<\infty, \quad n_d\in\mathbb{N}
```

  This system simply shifts to the right (if $n_d$ is positive, otherwise to the left) the input signal by a factor of $n_d$.

- **Moving average**:

```math
y[n]=\frac{1}{M_1+M_2+1}\sum_{k=-M_1}^{M_2}x[n-k]
```

# Memoryless Systems

A system is memoryless if the output $y[n]$ depends only on the input $x[n]$ at the same value of $n$.

## Example

```math
y[n]=(x[n])^2
```

# Linear Systems

Consider $y_1[n]$ and $y_2[n]$ the outputs of the system, $x_1[n]$ and $x_2[n]$ the inputs of the system. The system is linear if and only if the following two properties are satisfied:

- **Additivity property**:

```math
T\{x_1[n]+x_2[n]\}=T\{x_1[n]\}+T\{x_2[n]\}=y_1[n]+y_2[n]
```

- **Homogeneity**:

```math
T\{ax[n]\}=aT\{x[n]\}=ay[n]
```

# Non-Linear Systems

If the properties above are not satisfied, the system is non-linear.

## Example

```math
w[n]=\log_{10}(|x[n]|)
```

Consider two distinct inputs $x_1[n]$ and $x_2[n]$, we can write:

```math
\log_{10}(|x_1[n]+x_2[n]|)\neq \log_{10}(|x_1[n]|)+\log_{10}(|x_2[n]|)
```

```math
\log_{10}(|ax[n]|)\neq a\log_{10}(|x[n]|)
```

# Time-Invariant Systems

A time-invariant system is a system for which a time shift in the input sequence causes a corresponding time shift in the output sequence.

Given:

```math
x_1[n]=x[n-n_0]
```

this produces an output equal to:

```math
y_1[n]=y[n-n_0]
```

# Causality

A system is causal if, for every choice of $n_0$, the output sequence value at $n=n_0$ depends only on the input samples for $n \leq n_0$.

# Stability

A system is stable in the bounded input, bounded output (*BIBO*) sense if and only if every bounded input sequence produces a bounded output sequence.