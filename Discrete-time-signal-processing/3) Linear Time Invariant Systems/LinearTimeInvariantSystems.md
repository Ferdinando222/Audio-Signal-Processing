# Linear Time Invariant Systems

A linear time invariant (LTI) system is a system that satisfies both linearity (the *principle of superposition*) and time-invariance. An LTI system is entirely characterized by a single function: its impulse response.

# Sequence as a Linear Combination of Impulses

Any input sequence can be written as a weighted sum of shifted unit impulses:

```math
x[n]=\sum_{k=-\infty}^{+\infty} x[k]\delta[n-k]
```

Let $h_k[n]$ be the response of the system to an impulse $\delta[n-k]$ applied at $n=k$. Applying the system operator $T$ to the sequence above gives:

```math
y[n]=T\{\sum_{k=-\infty}^{+\infty} x[k]\delta[n-k]\}
```

By linearity, $T$ can be moved inside the summation:

```math
y[n]=\sum_{k=-\infty}^{+\infty} x[k]\,T\{\delta[n-k]\}=\sum_{k=-\infty}^{+\infty} x[k]\,h_k[n]
```

In a purely linear (but not time-invariant) system, $h_k[n]$ depends on both $k$ and $n$, which is impractical: the impulse response changes for every instant $k$ at which the impulse is applied, so infinitely many responses would need to be stored.

# Time-Invariance and the Convolution Sum

Imposing time-invariance forces the system to react identically to a stimulus regardless of when it is applied:

```math
\text{if } h[n]=T\{\delta[n]\} \quad \text{then} \quad T\{\delta[n-k]\}=h[n-k]
```

This states that the response to an impulse delayed by $k$ samples is simply $h[n]$ delayed by $k$ samples. Substituting this into the expression for $y[n]$ gives the **convolution sum**:

```math
y[n]=\sum_{k=-\infty}^{+\infty} x[k]\,h[n-k]
```

**A linear time invariant system is completely characterized by its impulse response $h[n]$.** The convolution sum is denoted by:

```math
y[n]=x[n]*h[n]
```

# Computation of the Convolution Sum

Computing $y[n]$ requires evaluating $h[n-k]$ and multiplying it by $x[k]$ at every $n$. This is easier when $h[n-k]$ is seen as a reflected and shifted version of $h[k]$:

```math
h[n-k]=h[-(k-n)]
```

## Algorithm

1. Consider the impulse response $h[n]=h[k]$.
2. Reflect $h[k]$ about the origin to obtain $h[-k]$.
3. Shift the origin of $h[-k]$ by $n$ samples to obtain $h[n-k]$, then multiply sample by sample with $x[k]$.
4. Sum the products and repeat step 3 for every $n$.

# Properties of Linear Time Invariant Systems

## Commutativity

```math
x[n]*h[n]=h[n]*x[n]
```

## Distributivity over Addition

```math
x[n]*(h_1[n]+h_2[n])=x[n]*h_1[n]+x[n]*h_2[n]
```

## Cascade of LTI Systems

```math
x[n]\rightarrow[h_1[n]]\rightarrow y_1[n]\rightarrow[h_2[n]]\rightarrow y[n]
```

is equivalent to:

```math
x[n]\rightarrow[h_1[n]*h_2[n]]\rightarrow y[n]
```

The overall impulse response of the cascade is therefore $h[n]=h_1[n]*h_2[n]$.

## Stability

An LTI system is stable if and only if its impulse response is absolutely summable:

```math
S=\sum_{k=-\infty}^{+\infty}|h[k]|<\infty
```

## Causality

An LTI system is causal if and only if:

```math
h[n]=0 \quad \text{for } n<0
```