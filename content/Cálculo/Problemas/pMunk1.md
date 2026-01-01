---
title: Problema del libro de Munkres §12, 2
tag:
    - Cálculo
    - Integración en varias variables
---

**Lema 1**. *$A:= \mathbb{Q}^{+}\cup\{0\}$ es numerable.*

_Demostración:_ Considere la función $f : A \longrightarrow \mathbb{N}$
definida por $f(0)=0$ y $f(p/q) = 2^{p}3^q$ si $p/q \not= 0$. Por el
teorema fundamental de la aritmética $f$ es inyectiva.

Ahora, la función $g : \mathbb{N} \longrightarrow A$ con $g(n)=n$ es
claramente inyectiva. Así, por el teorema de Cantor-Bernstein,
$|A| = |\mathbb{N}|$. ◻

**Lema 2**. *Si $A$ y $B$ son numerables, entonces $A \times B$ es
numerable.*

_Demostración:_ Como $A$ y $B$ son numerables, existen
$\alpha : A \longrightarrow \mathbb{N}$ y
$\beta : B \longrightarrow \mathbb{N}$ biyectivas. Entonces la función
$\gamma_1 : A\times B \longrightarrow \mathbb{N}\times \mathbb{N}$ con
$\gamma_1(a,b) = (\alpha(a), \beta(b))$ es inyectiva. Similarmente, la
función
$\gamma_2 : \mathbb{N}\times \mathbb{N} \longrightarrow A\times B$ con
$\gamma_2(m,n) = (\alpha^{-1}(m), \beta^{-1}(n))$ es inyectiva. Luego,
$|A \times B| = |\mathbb{N}\times \mathbb{N}|$.\
Sea $f : \mathbb{N}\times \mathbb{N} \longrightarrow \mathbb{N}$ con
$f(m,n) = 2^m3^n$. Entonces $f$ es inyectiva. Ahora sea
$g : \mathbb{N} \longrightarrow \mathbb{N}\times \mathbb{N}$ con
$f(n) = (n,0)$. Claramente $g$ es inyectiva. Luego
$|\mathbb{N}\times \mathbb{N}| = |\mathbb{N}|$.\
Así, $|A \times B| = |\mathbb{N}|$. ◻

**Problema 1**. *Sean
$A = \{x \in [0,1] \mid x = p/q \land p,q \in \mathbb{Q}^{+} \cup \{0\} \land q\not=0 \land \mathrm{mcd}(p,q) = 1\}$
y $Q = [0,1] \times [0,1]$. Sea $f : Q \longrightarrow \mathbb{R}$ con
$$f(x,y) = \frac{1}{q} \text{, si } (x,y) \in A \times \mathbb{Q}$$ y $$f(x,y) = 0 \text{, si } (x,y) \in (\mathbb{I}\times [0,1]) \cup(A \times \mathbb{I}) $$*

a)  *Muestre que $\displaystyle{\int_Qf}$ existe.*

b)  *Calcule $\displaystyle{\overline{\int_{y \in [0,1]}}f(x,y)}$ y
    $\displaystyle{\underline{\int_{y \in [0,1]}}f(x,y)}$.*

c)  *Verificar el teorema de Fubini.*

_Demostración (a):_ Sea $\epsilon > 0$ y $k \in \mathbb{N}$ con
$1/k < \epsilon$. Existen $\displaystyle{\sum_{q=1}^{k}\phi(q) + 1}$
números racionales $x \in A$, $x = p/q$ tales que $q < k$, esto es,
tales que $1/k < 1/q$.\
Sea $(x_0, y_0) \in Q$, con
$(x_0, y_0) \in (\mathbb{I}\times [0,1]) \cup(A \times \mathbb{I})$ y
$(x,y) \in Q$. Sea
$$\delta := \frac{\min\{|x - x_0| \mid x \in A \land x = p/q \land 1/k<1/q\}}{2}.$$
Si $\| (x,y) - (x_0,y_0) \| < \delta$, entonces:

I)  Si $(x,y) \in (\mathbb{I}\times [0,1]) \cup(A \times \mathbb{I})$,
    $|f(x,y) - f(x_0, y_0)| = 0 < \epsilon.$

II) Si $(x,y) \in A\times\mathbb{Q}$, con $x = p/q$, entonces
    $|f(x,y) - f(x_0,y_0)| = \frac{1}{q} \leq \frac{1}{k} <\epsilon$.

Así $f$ es continua en
$[(\mathbb{I}\times [0,1]) \cup(A \times \mathbb{I})] \cap Q$. Entonces
$f$ es discontinua en, a lo más,
$$D := [(\mathbb{Q}^{+}\cup\{0\})\times(\mathbb{Q}^{+}\cup\{0\})] \cap Q.$$

Por el Lema 1
$(\mathbb{Q}^{+}\cup\{0\}) \cap[0,1] \subseteq \mathbb{Q}^{+}\cup\{0\}$
es numerable y por el Lema 2, $D$ es numerable. Luego, existe una
biyección $\alpha : \mathbb{N} \longrightarrow D$ con
$\alpha(i) = (r,s)$. Así, la familia
$\{O_{\alpha(i)}\}_{i \in \mathbb{N}}$ con $$O_{\alpha(i)} = 
\left[r - \frac{\sqrt{\epsilon}}{\sqrt{2^{i+3}}}, r+\frac{\sqrt{\epsilon}}{\sqrt{2^{i+3}}}\right]
\times
\left[s - \frac{\sqrt{\epsilon}}{\sqrt{2^{i+3}}}, s + \frac{\sqrt{\epsilon}}{\sqrt{2^{i+3}}}\right],$$
es numerable y
$\displaystyle{v(O_{\alpha(i)}) = \frac{\epsilon}{2^{i+1}}}$.

Luego entonces, $$\sum_{i\in\mathbb{N}} v(O_{\alpha(i)}) = \sum_{k \in \mathbb{N}} \frac{\epsilon}{2^{i+1}} = \frac{\epsilon}{2} < \epsilon.$$ 

Y claramente, como $\alpha$ es biyectiva,
$\displaystyle{D \subseteq \bigcup_{j \in \mathbb{N}} O_{\alpha(i)}}$.\
Así, $f$ es discontinua en, a lo más, un conjunto de medida cero.
Aplicando la condición de Lebesgue, se tiene lo deseado. ◻

_Solución (b)_:\
Si $x \in \mathbb{I}$, entonces para cualquier partición $P$ de $[0,1]$,
$R \in P$: $$m(f, R) = 0 \text{ y } M(f,R) = 0.$$ Luego
$$\overline{\int_{y \in [0,1]}}f(x,y) = \underline{\int_{y \in [0,1]}}f(x,y) = 0$$

Si $x \in A$, entonces $f(x,y) = 1/q$ si $y \in \mathbb{Q}$ y
$f(x,y) = 0$ si $y \in \mathbb{I}$. Así $m(f,R) = 0$ y $M(f,R) = 1/q$
para cualquier $R$ rectángulo inducido por una partición $P$ de $[0,1]$.
Luego
$$\overline{\int_{y \in [0,1]}}f(x,y) = 1/q \text{ y } \underline{\int_{y \in [0,1]}}f(x,y) = 0,$$
esto es,
$$\overline{\int_{y \in [0,1]}}f(x,y) = 1/q  \text{, si } x \in A$$ y $$f(x,y) = 0 \text{, si } x \in \mathbb{I} \text{ y }\underline{\int_{y \in [0,1]}}f(x,y) = 0$$

_Solución (c):_\
Ahora, como $f$ es integrable, $\int_Qf=\underline{\int_Q}f$. Para
cualquier partición $P$ de $Q$ existe
$(\iota, \kappa) \in \mathbb{I}\times [0,1]$ tal que, para $R \in P$,
$(\iota, \kappa) \in R$. Así, $m(f,R) = 0$ y entonces $I(f,P) = 0$, para
cualquier $P$. Entonces $$\int_Q f = 0.$$

Por otro lado,
$$\int_{x \in [0,1]} \underline{\int_{y \in [0,1]}}f(x,y) = \int_{x\in[0,1]}0 = 0,$$
y, si $h : [0,1] \longrightarrow \mathbb{R}$,
$h(x):=\overline{\int_{y\in[0,1]}}f(x,y)$, entonces
$$\int_{x \in [0,1]} \overline{\int_{y \in [0,1]}}f(x,y) = \int_{x\in[0,1]}h(x) = 0 \text{ (es la función de Thomaé)}.$$

Así, se verifica el Teorema de Fubini:
$$\int_{Q}f = \int_{x \in [0,1]} \overline{\int_{y \in [0,1]}}f(x,y) = \int_{x \in [0,1]} \underline{\int_{y \in [0,1]}}f(x,y).$$
