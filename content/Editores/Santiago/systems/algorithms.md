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


These are mainly notes of the book *Introduction to algorithms* by Cormen, T. H., Leiserson, C. E., Rivest, R. L., \& Stein, C. (2022).  (4th ed.). MIT Press.
, along with the Python implementation and 
some other things. 

The repository with the .py files can be found [[https://github.com/Santiago-l-l-l/Introduction-to-Algorithms
|here]].

The notes assume some abstract thinking and mathemathical background. 

Before anything, here are some basic definitions

# Basic Definitions 

## Big O Notation

$$
\begin{aligned}
\textbf{Big-O } \mathcal{O}(g(n)) &= \{ f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le f(n) \le c \cdot g(n) \text{ for all } n \ge n_0 \} \\
\textbf{Big-Omega } \Omega(g(n)) &= \{ f(n) : \exists c > 0, n_0 > 0 \text{ such that } 0 \le c \cdot g(n) \le f(n) \text{ for all } n \ge n_0 \} \\
\textbf{Theta } \Theta(g(n)) &= \{ f(n) : \exists c_1, c_2 > 0, n_0 > 0 \text{ such that } 0 \le c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \text{ for all } n \ge n_0 \} \\[1em]
\textbf{Little-o } o(g(n)) &= \{ f(n) : \forall c > 0, \exists n_0 > 0 \text{ such that } 0 \le f(n) < c \cdot g(n) \text{ for all } n \ge n_0 \} \\
\textbf{Little-omega } \omega(g(n)) &= \{ f(n) : \forall c > 0, \exists n_0 > 0 \text{ such that } 0 \le c \cdot g(n) < f(n) \text{ for all } n \ge n_0 \}
\end{aligned}
$$

$O$-notation provides an asymptotic upper bound on a function, $\Omega$-notation an asymptotic lower bound
and $\Theta$-notation an asymptotic tight bound.

Moreover, we have the following, clear

## Theorem 1.1

For any two functions $f(n), \, g(n)$. $f(n)= \, \Theta(g(n)) \, \iff \, f(n)=O(g(n))$ and $f(n)= \Omega(g(n))$



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

$$\\$$

## Recurrence

A **recurrence** is an equation (or inequality) that describes a function in terms of its value on other, typically smaller, 
arguments. It contains two or more cases. If a case involves the recursive invocation of the function on different inputs, 
it's a **recursive case**, if not, it's a **base case**. 

It is **well defined** if exists at least one function that satisfies it, and **ill defined** otherwise.

A recurrence $T(n)$ is **algorithmic** if, for every sufficiently large *threshold* constant $n_0>0$, 
$\forall \, \, n<n_0$, $T(n)=\Theta(1)$ and $\forall \, \, n \ge n_0 $, every path of recursion 
terminates in a defined base case within a finite number of recursive invocations.

Some methodsfor solving recurrences are:

## Substitution Method

Consists of 2 steps: guess the form of the solution using constants and use induction to prove
the solution works and find the constants.

*Example:* given $T(n)=2T(\lfloor x \rfloor) + \Theta(n)$, we suppose $T(n) \le c \, n \text{lg} \, n$, $
\forall \, n \ge n_0$ and later we'll find $c$ and $n_0$.

$\begin{aligned}
T(n) &\le 2c\lfloor n/2 \rfloor \lg(\lfloor n/2 \rfloor) + \Theta(n) \\
&\le 2c(n/2) \lg(n/2) + \Theta(n) \\
&= cn \lg(n/2) + \Theta(n) \\
&= cn \lg n - cn \lg 2 + \Theta(n) \\
&= cn \lg n - cn + \Theta(n) \\
&\le cn \lg n,
\end{aligned}$

where the last step holds if we constrain the constants $n_0$ and $c$ to be sufficiently large that for $n \ge 2n_0$.
$T(n) \le cn \lg n$ when $n_0 \le n < 2n_0$. Assuming that $T(n)$ is algorithmic, it suffices to take  $n_0=2$, 
$c=\text{max} \{ T(2), T(3) \}$.




## Recursion-tree Method

In a recursion tree, each node represents the cost of a single subproblem somewhere in the set of
recursive function invocations and it's best used to generate intuition. 

One self-explanatory example is 

![[recur_tree1.png | 1000]]

Adding the costs we get the recurrence

$\begin{aligned}
T(n) &= cn^2 + \frac{3}{16}cn^2 + \left(\frac{3}{16}\right)^2 cn^2 + \dots + \left(\frac{3}{16}\right)^{\log_4 n} cn^2 + \Theta(n^{\log_4 3}) \\
&= \sum_{i=0}^{\log_4 n} \left(\frac{3}{16}\right)^i cn^2 + \Theta(n^{\log_4 3}) \\
&< \sum_{i=0}^{\infty} \left(\frac{3}{16}\right)^i cn^2 + \Theta(n^{\log_4 3}) \\
&= \frac{1}{1 - 3/16} cn^2 + \Theta(n^{\log_4 3}) \quad \text{(by infinite geometric series summation)} \\
&= \frac{16}{13} cn^2 + \Theta(n^{\log_4 3}) \\
&= O(n^2) \quad (\text{since } \Theta(n^{\log_4 3}) \approx \Theta(n^{0.793}) = O(n^2)).
\end{aligned}$

The last assertion can be proved using the substitution method.



## Master Method

This method is used for the so called *master recurrences* $T(n)=aT(\frac{n}{b})+f(n)$. Where $f(n)$ is called
a driving function that encompasses the cost of dividing the problem before the recursion and 
 the cost of combining the results of the recursive solutions to subproblems.

(The floor and ceiling functions are left implicit)

## Theorem 4.1 (Master Theorem)

Let $a>0,  b>1$, $f(n)$ an eventually nonnegative driving function. Given the recurrence

$T(n)=aT(\frac{n}{b})+f(n)$, where $aT(n/b)=a' T(\lfloor n/b \rfloor) + a'' T(\lceil n/b \rceil)$ 
for some $a' , a'' \ge 0$, $a = a' + a''$. Then, if

- $\exists \, \epsilon > 0$ such that $f(n) = O(n^{\log_b a - \epsilon})$, then $T(n) = \Theta(n^{\log_b a})$.
- $\exists \, k \ge 0$ such that $f(n) = \Theta(n^{\log_b a} \lg^k n)$, then $T(n) = \Theta(n^{\log_b a} \lg^{k+1} n)$.
- $\exists \,  \epsilon > 0$ such that $f(n) = \Omega(n^{\log_b a + \epsilon})$, and if $f(n)$ additionally satisfies the regularity condition $af(n/b) \le cf(n)$ for some $c < 1$ and all sufficiently large $n$, then $T(n) = \Theta(f(n))$.

The function $n^{\log_b a}$ is called the *watershed function*.

Intuitively, if the watershed function grows asymptotically (polynomially $n^{\epsilon}$) faster than the driving function, then case 1 applies. Case 2 applies if the
two functions grow at nearly the same asymptotic rate. In case 3 
 the driving function grows asymptotically faster than the watershed
function.

**Examples:**

- **$T(n) = 9T(n/3) + n$**
  - $a = 9$, $b = 3$, $f(n) = n$, and $n^{\log_3 9} = \Theta(n^2)$.
  <br>
  - **Case 1** because $f(n) = n = O(n^{2-\epsilon})$ for $\epsilon \le 1$.
  <br>
  - $T(n) = \Theta(n^2)$

<br>

- **$T(n) = T(2n/3) + 1$**
  - $a = 1$, $b = 3/2$, $f(n) = 1$, and $n^{\log_{3/2} 1} = 1$.
  <br>
  - **Case 2** because $f(n) = 1 = \Theta(n^{\log_b a} \lg^0 n) = \Theta(1)$.
  <br>
  - $T(n) = \Theta(\lg n)$

<br>

- **$T(n) = 3T(n/4) + n \lg n$**
  - $a = 3$, $b = 4$, $f(n) = n \lg n$, and $n^{\log_4 3} \approx O(n^{0.793})$.
  <br>
  - **Case 3** because $f(n) = \Omega(n^{\log_4 3 + \epsilon})$ for $\epsilon \approx 0.2$, and $3(n/4) \lg(n/4) \le (3/4)n \lg n$ for $c = 3/4 < 1$.
  <br>
  - $T(n) = \Theta(n \lg n)$

<br>

- **$T(n) = 2T(n/2) + n \lg n$**
  - $a = 2$, $b = 2$, $f(n) = n \lg n$, and $n^{\log_2 2} = n$.
  <br>
  - **Case 2** because $f(n) = n \lg n = \Theta(n^{\log_b a} \lg^1 n)$.
  <br>
  - $T(n) = \Theta(n \lg^2 n)$


There are cases where this method doesn't apply: We might have that $f(n) > n^{\log_b a}$ for an infinite number of values of $n$ but also that $f(n) < n^{\log_b a}$ for an infinite number of different values of $n$.
$f(n) = o(n^{\log_b a})$, yet the watershed function does not grow polynomially faster than the driving function. Similarly, for cases 2 and 3 when $f(n) = \omega(n^{\log_b a})$ and the driving function grows more than polylogarithmically faster than the watershed function, but it does not grow polynomially faster.


## Akra-Bazzi Method

This method is used to solve **Akra-Bazzi recurrences** $\, \, \displaystyle T(n) = f(n) + \sum_{i=1}^{k} a_i T(n/b_i)$.

First, determine the unique real number $p$ such that $\displaystyle \sum_{i=1}^{k} \frac{a_i}{b_i^p} = 1$. Such a value $p$ always exists
because the summation approaches $\infty$ as $p \to -\infty$, decreases monotonically as $p$ increases, and approaches $0$ as $p \to \infty$ (so the Intermediate Value Theorem applies). 
The Akra-Bazzi method then evaluates the tight asymptotic solution to the recurrence as $\displaystyle T(n) = \Theta\left(n^p \left(1 + \int_{1}^{n} \frac{f(x)}{x^{p+1}} \, dx\right)\right)$.

(The original paper is more detailed and very interesting, I recommend at least flipping through it.

Akra, M., Bazzi, L. On the Solution of Linear Recurrence Equations. 
*Computational Optimization and Applications* 10, 195–210 (1998).
[https://doi.org/10.1023/A:1018373005182](https://doi.org/10.1023/A:1018373005182) ).

This method handles more cases than the Master method.

# Basic Algorithms

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

In the **RAM** (Random-Access Machine)  model each instruction or data access takes a constant amount
of time. 

## Merge(A, p, q, r)

$$ \textbf{MERGE}(A, p, q, r): \\$$
$$
\begin{array}{ll}
1 & n_L = q - p + 1 \quad \text{// length of } A[p \dots q] \\
2 & n_R = r - q \quad \text{// length of } A[q + 1 \dots r] \\
3 & \text{let } L[0 \dots n_L - 1] \text{ and } R[0 \dots n_R - 1] \text{ be new arrays} \\
4 & \textbf{for } i = 0 \textbf{ to } n_L - 1 \quad \text{// copy } A[p \dots q] \text{ into } L[0 \dots n_L - 1] \\
5 & \quad L[i] = A[p + i] \\
6 & \textbf{for } j = 0 \textbf{ to } n_R - 1 \quad \text{// copy } A[q + 1 \dots r] \text{ into } R[0 \dots n_R - 1] \\
7 & \quad R[j] = A[q + j + 1] \\
8 & i = 0 \quad \text{// } i \text{ indexes the smallest remaining element in } L \\
9 & j = 0 \quad \text{// } j \text{ indexes the smallest remaining element in } R \\
10 & k = p \quad \text{// } k \text{ indexes the location in } A \text{ to fill} \\
11 & \text{// As long as each array contains an unmerged element, copy the smallest back.} \\
12 & \textbf{while } i < n_L \textbf{ and } j < n_R \\
13 & \quad \textbf{if } L[i] \le R[j] \\
14 & \quad \quad A[k] = L[i] \\
15 & \quad \quad i = i + 1 \\
16 & \quad \textbf{else } A[k] = R[j] \\
17 & \quad \quad j = j + 1 \\
18 & \quad k = k + 1 \\
19 & \text{// Copy the remaining elements of the other array to the end of } A[p \dots r]. \\
20 & \textbf{while } i < n_L \\
21 & \quad A[k] = L[i] \\
22 & \quad i = i + 1 \\
23 & \quad k = k + 1 \\
24 & \textbf{while } j < n_R \\
25 & \quad A[k] = R[j] \\
26 & \quad j = j + 1 \\
27 & \quad k = k + 1
\end{array}
$$

## Merge-sort(A, p, r)
$$\textbf{MERGE-SORT}(A, p, r): \\$$
$$
\begin{array}{ll}
1 & \textbf{if } p \ge r \quad \text{// zero or one element?} \\
2 & \quad \textbf{return} \\
3 & q = \lfloor (p + r) / 2 \rfloor \quad \text{// midpoint of } A[p \dots r] \\
4 & \textbf{MERGE-SORT}(A, p, q) \quad \text{// recursively sort } A[p \dots q] \\
5 & \textbf{MERGE-SORT}(A, q + 1, r) \quad \text{// recursively sort } A[q + 1 \dots r] \\
6 & \text{// Merge } A[p \dots q] \text{ and } A[q + 1 \dots r] \text{ into } A[p \dots r]. \\
7 & \textbf{MERGE}(A, p, q, r)
\end{array}
$$


The complexity of this algorithm for every case is $O(n \, \text{log} \, n)$, i.e., the time complexity is $\Theta(n \, \text{log} \, n)$ for every case.

## Bubblesort (A, n)

$$\textbf{BUBBLESORT}(A, n): \\ $$
$$
\begin{array}{ll}
1 & \textbf{for } i = 1 \textbf{ to } n - 1 \\
2 & \quad \textbf{for } j = n \textbf{ downto } i + 1 \\
3 & \quad \quad \textbf{if } A[j] < A[j - 1] \\
4 & \quad \quad \quad \text{exchange } A[j] \text{ with } A[j - 1]
\end{array}
$$

The worst-case time complexity is $O(n^2)$, and the best-case is $\Omega(n^2)$, so $\Theta(n^2)$.

## Matrix-Multiply-Recursive

$$\textbf{MATRIX-MULTIPLY-RECURSIVE}(A, B, C, n): \\$$
$$
\begin{array}{ll}
1 & \textbf{if } n == 1 \\
2 & \quad \text{// Base case.} \\
3 & \quad c_{11} = c_{11} + a_{11} \cdot b_{11} \\
4 & \quad \textbf{return} \\
5 & \text{// Divide.} \\
6 & \text{partition } A, B, \text{ and } C \text{ into } n/2 \times n/2 \text{ submatrices} \\
  & A_{11}, A_{12}, A_{21}, A_{22}; \; B_{11}, B_{12}, B_{21}, B_{22}; \\
  & \text{and } C_{11}, C_{12}, C_{21}, C_{22}, \text{ respectively} \\
7 & \text{// Conquer.} \\
8 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{11}, B_{11}, C_{11}, n/2) \\
9 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{11}, B_{12}, C_{12}, n/2) \\
10 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{21}, B_{11}, C_{21}, n/2) \\
11 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{21}, B_{12}, C_{22}, n/2) \\
12 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{12}, B_{21}, C_{11}, n/2) \\
13 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{12}, B_{22}, C_{12}, n/2) \\
14 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{22}, B_{21}, C_{21}, n/2) \\
15 & \textbf{MATRIX-MULTIPLY-RECURSIVE}(A_{22}, B_{22}, C_{22}, n/2)
\end{array}
$$

Since there are 8 recursive calls, we have a recurrence of the form $T(n)= 8T(\frac{n}{2}) + \Theta(1)$ 
for the running time of Matrix-Multiply-Recursive. Whose solution is $T(n)=\Theta(n^3)$.


## Strassen's Algorithm

THe recurrence for the running time of this algorithm is $T(n)=7T(\frac{n}{2})+\Theta(n^2)$ whose 
solution is $T(n)=\Theta(n^{\text{log}7})=\Theta(n^{2.81})$

$$\textbf{STRASSEN}(A, B, C, n): \\$$
$$
\begin{array}{ll}
1 & \textbf{if } n == 1 \\
2 & \quad \text{// Base case.} \\
3 & \quad c_{11} = c_{11} + a_{11} \cdot b_{11} \\
4 & \quad \textbf{return} \\
5 & \text{// Divide.} \\
6 & \text{partition } A, B, \text{ and } C \text{ into } n/2 \times n/2 \text{ submatrices} \\
  & A_{11}, A_{12}, A_{21}, A_{22}; \; B_{11}, B_{12}, B_{21}, B_{22}; \\
  & \text{and } C_{11}, C_{12}, C_{21}, C_{22}, \text{ respectively} \\
7 & \text{// Create temporary matrices for Strassen's combinations.} \\
8 & S_1 = B_{12} - B_{22} \\
9 & S_2 = A_{11} + A_{12} \\
10 & S_3 = A_{21} + A_{22} \\
11 & S_4 = B_{21} - B_{11} \\
12 & S_5 = A_{11} + A_{22} \\
13 & S_6 = B_{11} + B_{22} \\
14 & S_7 = A_{12} - A_{22} \\
15 & S_8 = B_{21} + B_{22} \\
16 & S_9 = A_{11} - A_{21} \\
17 & S_{10} = B_{11} + B_{12} \\
18 & \text{// Conquer - Create 7 matrices for recursive calls.} \\
19 & \text{allocate } P_1, P_2, P_3, P_4, P_5, P_6, P_7 \text{ as new } n/2 \times n/2 \text{ matrices initialized to zero} \\
20 & \textbf{STRASSEN}(A_{11}, S_1, P_1, n/2) \\
21 & \textbf{STRASSEN}(S_2, B_{22}, P_2, n/2) \\
22 & \textbf{STRASSEN}(S_3, B_{11}, P_3, n/2) \\
23 & \textbf{STRASSEN}(A_{22}, S_4, P_4, n/2) \\
24 & \textbf{STRASSEN}(S_5, S_6, P_5, n/2) \\
25 & \textbf{STRASSEN}(S_7, S_8, P_6, n/2) \\
26 & \textbf{STRASSEN}(S_9, S_{10}, P_7, n/2) \\
27 & \text{// Combine - update C quadrants using linear combinations of P.} \\
28 & C_{11} = C_{11} + P_5 + P_4 - P_2 + P_6 \\
29 & C_{12} = C_{12} + P_1 + P_2 \\
30 & C_{21} = C_{21} + P_3 + P_4 \\
31 & C_{22} = C_{22} + P_5 + P_1 - P_3 - P_7
\end{array}
$$



# Probabilistic Analysis and Randomized Algorithms

If you need a review on probability theory you may want to view [this](https://3inaba.github.io/Notas-LFMMyOC/Editores/Santiago/prob) 

To perform a probabilistic analysis, we
use knowledge of, or make assumptions about, the distribution of the inputs. Then
we analyze our algorithm, computing an average-case running time, where we take
the average, or expected value, over the distribution of the possible inputs. When
reporting such a running time, we refer to it as the **average-case running time**.

In the book there are examples and not a structured approach. I'll leave this space in blank for now and 
fill in the page later using other bibliography.


# Sorting and Order Statistics

'Many computer scientists consider sorting to be the most fundamental problem in
the study of algorithms'. Here's a summary table:


| Algorithm | Worst-case running time | Average-case/expected running time |
| :--- | :--- | :--- |
| **Insertion sort** | $\Theta(n^2)$ | $\Theta(n^2)$ |
| **Merge sort** | $\Theta(n \lg n)$ | $\Theta(n \lg n)$ |
| **Heapsort** | $O(n \lg n)$ | — |
| **Quicksort** | $\Theta(n^2)$ | $\Theta(n \lg n)$ (expected) |
| **Counting sort** | $\Theta(k + n)$ | $\Theta(k + n)$ |
| **Radix sort** | $\Theta(d(n + k))$ | $\Theta(d(n + k))$ |
| **Bucket sort** | $\Theta(n^2)$ | $\Theta(n)$ (average-case) |


The $i$-th order statistic of a set of $n$ numbers is the $i$ th smallest number in the set.  

In general, the $i$-th order statistics is $X_{(i)}= \text{min} \{ X_1, ..., X_n \} \setminus \{ X_{(1)}, ..., X_{(i-1)} \} $, 
with $X_{(1)}= \text{min} \{ X_1, ..., X_n \}$. Where $X_1, ..., X_n$ is a random sample (a collection of 
$X_1, ..., X_n$ independent and identically distributed random variables ).


## Heapsort

Heapsort sorts in place: only a constant number of array elements
are stored outside the input array at any time






