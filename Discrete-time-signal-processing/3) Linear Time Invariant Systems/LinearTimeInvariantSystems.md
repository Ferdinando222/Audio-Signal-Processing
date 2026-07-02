# Linear Time Invariant Systems

A linear time invariant system is a specific class of systems that combines the property of linearity (*Principle of superposition*) and time-invariant. In particular, a linear time invariant system can be entirely charcterized by its impulse response.

Infact if we consider an input impulse $\delta[n-k]$ occuring at $n=k$ and $h_k[n]$ the response of the system, we can write

*Sequence as a linear combination of impulses responses*
$$
y[n]=T\{\sum_{k=-\infty}^{+\infty} x[k]\delta[n-k]\} 
$$

*Linearity*
$$
y[n]=\sum_{k=-\infty}^{+\infty} x[k]T\{\delta[n-k]\}=\sum_{k=-\infty}^{+\infty} x[k]h_k[n]
$$

In a purely linear system, the response of the system $h_k[n]$ depends both from $k$ and $n$ and this is not very practical. **The impulse response in this case change for every step k**. This requires to memorize infinite impulse response for each instant of time when the impulse is applied.
Applying the constraint of time-invariance, we force the system to act in the same way independently when it's stimolated.

*Time-invariance*

$$
    if \quad h[n]=T\{\delta[n]\}\quad then \quad \delta[n-k]=h[n-k]
$$

So with this constraint we are saying that that system response to an impulse delayed of $k$ is equal to a delayed $h$ of $k$ samples. So we can write

$$
y[n]=\sum_{k=-\infty}^{+\infty} x[k]h[n-k]
$$

In conlusion: **A linear time invariant system (LTI) is completly characterized by its impulse response $h[n]$**. This expression is also known as the convolution sum, and it can be represented with this notation:

$$
y[n]=x[n]*h[n]
$$

## Computation of convolution sum

In order to compute the convolution for each sample $n$ we need to compute $h[n-k]$ and then multiply it with $x[k]$.
For this reasn is useful to see the following relationshio:
$$
h[n-k]=h[-(k-n)]
$$

This expression tell us thath $h[n-k]$ can be seen as reflected and traslated version of $h[k]$. The algorithm to correctly compute this convolution is:

1) Consider the impulse response $h[n]=h[k]$
2) Reflecting $h[k]$ about origin in order to obtain $h[-k]$
3) Now to compute the output of the sample $n$, you have to shift the origin of $h[-k]$ of $n$ samples $h[-(k-n)]$, and then you can multiply sample by sample $x[k]h[n-k]$
4) Repeat 3 for each $n$ samples

## Properties of linear time invariant systems

1) The convolution operation is commutative:
   $$
   x[n]*h[n]=h[n]*x[n]
   $$

2) Distribution over addition:
   $$
   x[n]*(h_1[n]+h_2[n])=x[n]*h_1[n]+x[n]*h_2[n]
   $$

3) Property of a cascade of LTI:
   
   $$
   x[n]\rightarrow[h_1[n]]\rightarrow y_1[n]\rightarrow[h_2[n]]\rightarrow y[n]  
   $$

   This is equal to consider

   $$
   x[n]\rightarrow[h_1[n]*h_2[n]]\rightarrow y[n]
   $$

   So the overall system is $h[n] = h_1[n]*h_2[n]$

4) Stability:    
   LTI systems are stable if and only if the impulse response is absolutly summable:

   $$
    S=\sum_{k=-\infty}^{+\infty}|h[k]|<\infty
   $$

5) Causality for LTI: 
   A LTI is causal if and only if $h[n]=0$ for $n<0$