---
title: Invarianza de la cardinalidad de las bases de espacios vectoriales (caso infinito)
tag:
    - Álgebra
    - Álgebra Lineal
    - Teoría de Conjuntos
---

_*Teorema:*_
Toda base de un $F$-espacio vectorial tiene la misma cardinalidad.

*Demostración:* (Caso infinito) Sean $\mathscr{A}$ y $\mathscr{B}$ bases de un
$F$-espacio vectorial $V$ ordenadas por conjuntos de índices bien
ordenados $I$ y $J$ respectivamente, con
$\mathrm{card}(\mathscr{A}) \geq \aleph_0$ e $i \in I$ y $j \in J$.
Demostrado el caso finito, entonces tenemos que
$\mathrm{card}(\mathscr{B}) \geq \aleph_0$\
Cada vector $\alpha_i \in \mathscr{A}$ es representado de forma única
como una combinación lineal finita de vectores
$\beta_j \in \mathscr{B}$. En efecto, sean $J_{i1} \subseteq J$ y
$J_{i2} \subseteq J$ conjuntos finitos. Suponga que existen
$\{c_k\}_{k \in J_{i1}} \subseteq F$ y
$\{d_k\}_{k \in J_{i2}} \subseteq F$ y se tiene que

$$\alpha_i = \sum\limits_{k \in J_{i1}} c_k \beta_k \text{ y } \alpha_i = \sum\limits_{k \in J_{i2}} d_k \beta_k$$

Entonces

$$\sum\limits_{k \in J_{i1}} c_k \beta_k = \sum\limits_{k \in J_{i2}} d_k \beta_k$$

$$\sum\limits_{k \in J_{i1}} c_k \beta_k - \sum\limits_{k \in J_{i2}} d_k \beta_k = 0$$

Luego, separando las sumas en índices en común e índices no en común, se
tiene

$$\sum\limits_{k \in J_{i1} \cap J_{i2}} (c_k - d_k) \beta_k + \sum\limits_{k \in J_{i1} \setminus J_{i2}} c_k \beta_k - \sum\limits_{k \in J_{i2} \setminus J_{i1}} d_k \beta_k = 0$$

$\mathscr{B}$ es base, entonces
$\forall c_k, k \in J_{i1} \setminus J_{i2}$ se tiene que $c_k = 0$ y
del mismo modo $\forall d_k, k \in J_{i2} \setminus J_{i1}$ se tiene que
$d_k = 0$. Luego, $\forall k \in J_{i1} \cap J_{i2}$, $c_k - d_k = 0$.
Luego entonces $c_k = d_k$. Así, tenemos que la representación es
única.\
Ahora, cada $\beta_j \in \mathscr{B}$ aparece en una combinación lineal
finita de un $\alpha_i \in \mathscr{A}$. Si no fuera así, entonces
suponga que $\beta_{j_0}$ no aparece en ninguna combinación lineal
finita para todo $\alpha_i \in \mathscr{A}$. Luego, sea
$I_{j_0} \subseteq I$ conjunto finito y sea
$\{e_l\}_{l \in I_{j_0}} \subseteq F$, como $\mathscr{A}$ es base,
entonces

$$\beta_{j_0} = \sum\limits_{l \in I_{j_0}} e_l \alpha_l$$

Cada $\alpha_l, l \in I_{j_0}$ se representa como una combinación lineal
finita de vectores en $\mathscr{B}$, sea $J_\alpha \subseteq J$ conjunto
finito y $\{c_k\}_{k \in J_{\alpha}}$, supongamos entonces

$$\beta_{j_0} = \sum\limits_{k \in J_{\alpha}} c_k \beta_k$$

luego entonces, $\mathscr{B}$ es linealmente dependiente, lo que
contradice que $\mathscr{B}$ sea una base de $V$. Por lo tanto, todo
vector $\beta_j \in \mathscr{B}$ aparece en alguna combinación lineal
que representa a los $\alpha_i \in \mathscr{A}$.\
Entonces se define $\underset{\beta_j \mapsto \alpha_i}{f: \mathscr{B} \longrightarrow \mathscr{A}}$ que a un $\beta_j \in \mathscr{B}$ le asigna sólo un
$\alpha_i \in \mathscr{A}$ donde $\beta_j$ forma parte de la combinación
lineal finita única que representa a $\alpha_i$. Entonces $\underset{\beta_j \mapsto \alpha_i}{f: \mathscr{B} \longrightarrow \mathscr{A}}$ es una función.\
Luego, sea $J_i \subseteq J$ conjunto finito y
$\alpha_i' \in f(\mathscr{B})$, entonces
$f^{-1}(\{\alpha_i'\}) = \{\beta_j\}_{j \in J_i}$, $J_i \subset J$ es un
conjunto tal que $\beta_j$ forma parte de la combinación lineal finita
única que representa a $\alpha_i$, entonces $f^{-1}(\{\alpha_i'\})$ es
un conjunto finito.\
Sea
$\Gamma := \{f^{-1}(\{\alpha_i'\}) \in \mathcal{P}(\mathscr{B}) \mid \alpha_i' \in f(\mathscr{B})\}$.
Luego $\mathscr{B} = \bigcup\limits_{\gamma \in \Gamma} \gamma$, la
cual, como $f$ es función, es una unión disjunta. Así
$\mathrm{card}(\mathscr{B}) = \sum\limits_{\gamma \in \Gamma} \mathrm{card}(\gamma) \leq \mathrm{card}(f(\mathscr{B}))$
y como $f(\mathscr{B}) \subseteq \mathscr{A}$,
$\mathrm{card}(f(\mathscr{B})) \leq \mathrm{card}(\mathscr{A})$. Luego
entonces $\mathrm{card}(\mathscr{B}) \leq \mathrm{card}(\mathscr{A})$ y
se tiene que existe $\phi : \mathscr{B} \longrightarrow \mathscr{A}$
función inyectiva.\
De manera análoga, intercambiando los papeles de $\mathscr{B}$ y
$\mathscr{A}$, se llega a que
$\mathrm{card}(\mathscr{A}) \leq \mathrm{card}(\mathscr{B})$ y entonces
existe una función inyectiva
$\psi : \mathscr{A} \longrightarrow \mathscr{B}$. Luego, por el Teorema
de Cantor-Bernstein se tiene que
$\mathrm{card}(\mathscr{A}) = \mathrm{card}(\mathscr{B})$. ◻
