---
title: Algorithms
author: Santiago
date: 2026-09-19
draft: false

tag:
   - Sorting Algorithms
---

Firstly, I've written some notes of the book '
Data Structures and Algorithms with Python

With an Introduction to Multiprocessing' in the following  [[https://github.com/Santiago-l-l-l/systems/tree/main/Data%20Structures%20and%20Algorithms|Github Repository]].

They're more unstructured and don't have a lot of explanation, unlike the rest of this page
which is an attemp to give concise and clear information (stopping all the yap and unnecessary text in cs books).


These are mainly notes of the 'Introduction to Algorithms. Fourth Edition', along with the Python implementation and 
some other things. 

The repository with the .py files can be found [[https://github.com/Santiago-l-l-l/Introduction-to-Algorithms
|here]].

The notes assume some abstract thinking and mathemathical background. 

Before anything, here are some basic **definitions** 

$$
\begin{aligned}
\textbf{Big-O } \mathcal{O}(g(n)) &= \{ f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \text{ for all } n \ge n_0 \} \\
\textbf{Big-Omega } \Omega(g(n)) &= \{ f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le c \cdot g(n) \le f(n) \text{ for all } n \ge n_0 \} \\
\textbf{Theta } \Theta(g(n)) &= \{ f(n) : \exists c_1, c_2 > 0, n_0 > 0 \text{ such that } 0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \text{ for all } n \ge n_0 \} \\[1em]
\textbf{Little-o } o(g(n)) &= \{ f(n) : \forall c > 0, \exists n_0 > 0 \text{ such that } 0 \le f(n) < c \cdot g(n) \text{ for all } n \ge n_0 \} \\
\textbf{Little-omega } \omega(g(n)) &= \{ f(n) : \forall c > 0, \exists n_0 > 0 \text{ such that } 0 \le c \cdot g(n) < f(n) \text{ for all } n \ge n_0 \}
\end{aligned}
$$



There are also other definitions for the big O and little o notation used in numerical analysis (
note that the prior definitions are intendeed for sequences):

It is said that $f$ is $O(g(x))$ when $x \to x_0$ if $\exists \, M, \delta \in \mathbb{R}^+$ such that 
$|f(x) \le M \, |g(x)|$, $\forall x \in V_{ \delta} (x_0)$.

It is said that $f$ is $O(g(x))$ when $x \to \infty$ if $\exists \, M, \delta \in \mathbb{R}^+$ such that
$|f(x) \le M \, |g(x)|$, $\forall x \, : \, |x| > \delta$.

It is said that $f$ is $o(g(x))$ when $x \to x_0$ if $\forall k>0, \, \exists \, \delta \in \mathbb{R}^+$ such that
$|f(x) \le k \, |g(x)|$, $\forall x \in V_{ \delta} (x_0)$.

It is said that $f$ is $o(g(x))$ when $x \to \infty$ if $\forall k>0, \, \exists \, \delta \in \mathbb{R}^+$ >
$|f(x) \le k \, |g(x)|$, $\forall x \, : \, |x| > \delta$.



## Insertion-Sort (A,n)


$$\textbf{Insertion-Sort}(A, n):$$
$$
\begin{array}{ll} \\
1 & \textbf{for } i = 2 \textbf{ to } n \\
2 & \quad \quad \text{key} = A[i] \\
3 & \quad \quad \text{// Insert } A[i] \text{ into the sorted subarray } A[1 \dots i - 1] \\
4 & \quad \quad j = i - 1 \\
5 & \quad \quad\textbf{while } j > 0 \textbf{ and } A[j] > \text{key} \\
6 & \quad \quad \quad A[j + 1] = A[j] \\
7 & \quad \quad \quad j = j - 1 \\
8 & \quad \quad A[j + 1] = \text{key}
\end{array}
$$

The complexity of this algorithms is $O(n)$ for the best case (already sorted) and $O(n^2)$ for the average and worst cases.
 
