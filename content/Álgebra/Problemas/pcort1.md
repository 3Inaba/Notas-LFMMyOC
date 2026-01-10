---
title: Raíz de un polinomio de grado 3 es una cortadura 
tags:
    - Teoría de Conjuntos
    - Cortaduras de Dedekind
---

_Problema:_ Demostrar que el conjunto $\gamma := \{x \in \mathbb{Q} \mid x \leq 0 \lor x^3 - 5x < 1\}$ es una cortadura.

_Demostración:_ (i) Considere $\frac{4}{3}^3 - 5\frac{4}{3} = - \frac{116}{27} < 1$. Entonces $\gamma \not= \varnothing$. Ahora, $10^3 - 5(10) > 1$, por lo que $\mathbb{Q} \setminus \gamma \not= \varnothing$. Así $\{\gamma, \mathbb{Q} \setminus \gamma\}$ es una partición de $\mathbb{Q}$.

(ii) Sea $x \in \gamma$ y $y < x$. Si $y \leq 0$ entonces $y \in \gamma$. Si $0 < y < \frac{4}{3}$ entonces, si suponemos que $y^3 - 5y \geq 1$

$$\left(\frac{4}{3}^3 - 5\frac{4}{3}\right) - (y^3 - 5y) = \left(\frac{4}{3} - y\right)\left(\frac{4}{3}^2 + \frac{4}{3}y + y^2 - 5)\right)$$
$$=  \left(\frac{4}{3} - y\right)\left(\frac{4}{3}^2 + \frac{4}{3}y + (y^2 - 5))\right) > 0$$

Así

$$\left(\frac{4}{3}^3 - 5\frac{4}{3}\right) > (y^3 - 5y)$$

y entonces $1 > y^3 - 5y \geq 1$ $\bot$. Luego $y \in \gamma$.

Si $\frac{3}{4} < y$ entonces

$$(x^3 - 5x) - (y^3 - 5y) = (x - y)(x^2 + xy + y^2 - 5)$$
$$ > (x - y)(\frac{16}{9} + \frac{16}{9} + \frac{16}{9} - 5) > 0$$

Así $1 > x^3 - 5x > y^3 - 5y$. Luego $y \in \gamma$.

(iii) Sean $x \in \gamma$ y $\epsilon := \min\{1, \frac{1 - (x^3 - 5x)}{3x^2 + 3x + 1}\} > 0$. Entonces

$$(x + \epsilon)^3 - 5(x+\epsilon) - (x^3 - 5x) = 3x^2\epsilon + 3x\epsilon^2 + \epsilon^3 - 5\epsilon$$
$$= \epsilon(3x^2 + 3x\epsilon + \epsilon^2 - 5)$$
$$< \epsilon(3x^2 + 3x + 1)$$
$$< 1 - (x^3 - 5x)$$

y entonces $(x + \epsilon)^3 - 5(x + \epsilon) < 1$.

Luego $\gamma$ es una cortadura.
