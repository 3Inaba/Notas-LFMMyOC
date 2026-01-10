---
title: La suma de la raíz de dos y su inverso multilplicativo es mayor a 2 
tags:
    - Teoría de Conjuntos
    - Cortaduras de Dedekind
---

_Problema:_ Si $\sqrt{2} := \{x \in \mathbb{Q} \mid x \leq 0 \lor x^2 < 2\}$, demostrar que  $\sqrt{2} +_{\mathscr{C}} \sqrt{2}^{-1} \geq_{\mathscr{C}} 2_{\mathscr{C}}$.

_Demostración:_ Demuestre en general que si $a \in \mathbb{Z}^+$ entonces para todo $n \in \mathbb{N} \setminus \{0,1\}$ el conjunto $\sqrt[n]{a} := \{x \in \mathbb{Q} \mid x \leq 0 \lor x^n < a\}$ es una cortadura.

Ahora, recordando $\sqrt{2}^{-1} = \{x \in \mathbb{Q} \mid \frac{1}{x} \not\in \sqrt{2} \land$ $x$ no es elemento mínimo de $\mathbb{Q} \setminus \sqrt{2}$ $\}$.

Así, considere $\sqrt{2} +_{\mathscr{C}} \sqrt{2}^{-1} := \{z \in \mathbb{Q} \mid \exists x \in \sqrt{2} \land \exists y \in \sqrt{2}^{-1} $ tal que $ z = x+y\}$

Entonces, tómese $\frac{7}{10} \in \sqrt{2}^{-1}$ $($pues $\frac{100}{49} > 2)$ y $\frac{7}{5} \in \sqrt{2}$ $(\frac{49}{25} < 2)$. Luego $\frac{7}{10} + \frac{7}{5} = \frac{7 + 14}{10} = \frac{21}{10} > 2$. Así $\frac{21}{10} \in \sqrt{2} +_{\mathscr{C}} \sqrt{2}^{-1}$ es tal que $\frac{21}{10} \not\in 2$, luego $\sqrt{2} +_{\mathscr{C}} \sqrt{2}^{-1} \geq_{\mathscr{C}} 2_{\mathscr{C}} $
