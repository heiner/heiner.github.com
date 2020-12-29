---
layout: post
title:  "Well-definedness of measures and the Lebesgue integral"
---

**Lemma.** Sei $$\H$$ eine Familie von Mengen mit der
Eigenschaft, daß es zu jeder endlichen Familie $$(A_1,
\ldots, A_n)$$ in $$\H$$ eine endliche
disjunkte Familie $$(B_k\st k \in
K_0)$$ in $$\H$$ gibt, so daß gilt

$$\forall j \in\set{1,\ldots,n}\, \exists K_j \subseteq
K_0: A_j=\mathop{\dot{\bigcup}}_{k \in K_j} B_k$$

(Insbesondere immer $$A_j \supseteq B_k$$
oder $$A_j\cap B_k=\varnothing$$, wobei
$$A_j\supseteq B_k \Leftrightarrow k \in K_j.$$)

Sei $$\mu\from \H\to[0, \infty)$$ eine additive Mengenfunktion. Sei $$A_{1}, \ldots, A_n \in
\H$$ und $$a_{1}, \ldots, a_n \in \F.$$ Definiere

$$\qquad b_k:=\sum_{\substack{1\le j\le n\\ A_j\supseteq B_k}} a_j \where{k\in K_0}.$$

Dann $$\sum_{j=1}^n a_j \1_{A_j}=\sum_{k\in K_0} b_k\1_{B_k}$$ und

$$ \sum_{j=1}^n a_j \mu(A_j)=\sum_{k \in K_0} b_k
\mu(B_k)$$

*Beweis.* Die erste Aussage folgt
direkt aus der Definition der $$b_k$$. Die zweite:

$$\begin{aligned} \sum_{j=1}^n a_j \mu(A_j)
&=\sum_{j=1}^n a_j \sum_{k \in K_j}
\mu(B_k) \\ &=\sum_{k \in K_0}
\underbrace{\sum_{j=1}^n \1_{K_j}(k) a_j}_{=b_k}
\mu(B_k)=\sum_{k \in K_0}
b_k \mu(B_k) \end{aligned} $$

**Folgerung.** Seien $$\H, \mu$$ wie im Lemma. Sei
$${X}:=\lin\set{\1_A\st A\in\H}$$. Dann ist $$J\from X\to\F$$, definiert durch

$$ {X} \ni f=\sum_{j=1}^n a_j
\1_{A_j} \mapsto \sum_{j=1}^n a_j
\mu(A_j)$$

wohldefiniert und linear.

*Beweis.* Es reicht, den Fall $$f=0$$ zu behandeln. Sei
$$(B_k\st k \in K_0)$$ die disjunkte
Darstellung sowie $$(b_k\st b \in K_0)$$ wie im
Lemma. Es gilt $$b_k=0$$ für alle $$k \in k_0,$$ denn
$$f=\sum_{j=1}^n a_j \1_{A_j}=\sum_{k \in
K_0} b_k \1_{B_k}$$ und die $$B_k$$
sind paarweise disjunkt. Daher nach Lemma

$$\sum_{j=1}^n a_j \mu(A_j)
% =\sum_{j=1}^n a_j \mu(\mathop{\dot{\bigcup}}_{k \in k_j}B_k)
= \sum_{k\in K_0} b_k \mu(B_k)=0.$$

Das zeigt die
Wohldefiniertheit. Die Linearität ist klar.

Erste Anwendung: Lebesgue-Stieltjes-Inhalt.

**Lemma.** Es sei $$\mathcal{R}$$
der Ring aller Figuren, d.h. endlicher Vereinigungen von halboffenen
Intervallen und $$\H$$ die Menge aller halboffenen
Intervalle.  Dann ist jedes $$F \in \mathcal{R}$$ die
disjunkte Vereinigung von endlich vielen Intervallen.

*Beweis* (Aus [J. Voigt, "Einführung in die Integration", Satz 1.1.1](http://www.math.tu-dresden.de/~voigt/mui/mui.pdf#page=7)).
Es sei $$F=\bigcup_{j=1}^n
I_j$$ mit $$I_j=[a_j, b_j)$$.
Die Menge $$\set{a_j, b_j\st j=1,\ldots,n}$$ läßt
sich schreiben als $$\set{x_k\st k=0,\ldots,m}$$ mit
$$x_0 <x_2 < \cdots < x_m$$. Eine Menge von disjunkten Intervallen,
deren Vereinigung $$F$$ ist, ist

$$\{[x_{k-1}, x_k)\st
1\le k\le m \text{ und } \exists j\in\set{1,\ldots,n} :
[x_{k-1}, x_k) \subseteq[a_j,b_j)\}$$

**Folgerung.** Sei $${G}\from\mathbb{R}\to\mathbb{R}$$
monoton und linksseitig stetig. Die Abbildung $$\mu\from\H\to[0,\infty)$$,
definiert durch $$\mu([a,b)):=G(b)-G(a)$$, läßt sich eindeutig zu einem
Inhalt $$\mu\from\mathcal{R}\to[0, \infty)$$ fortsetzen.

*Beweis.* $$\mu$$ ist additiv, und $$\H$$ hat die
Zerlegungseigenschaft aus Lemma 1 nach Lemma 3. Damit ist
$$J\from X\to\F$$ aus Folgerung 2
wohldefiniert. Sei $$F\in\mathcal{R}$$ eine Figur. Dann ist
$$\1_F \in {X}$$ und somit ist $$\mu(F):=J(\1_F)$$ wohldefiniert und $$\geq 0$$.
Außerdem ist $$\mu$$ additiv, denn für $$\tilde{F}\in\mathcal{R}$$ gilt

$$
\mu(F \mathbin{\dot{\cup}} \tilde{F}) =
J(\1_F+\1_{\tilde{F}}) = J(\1_F) + J(\1_{\tilde{F}}) =
\mu(F)+\mu(\tilde{F}).
$$

Und $$\mu$$ ist monoton: Da $$\mathcal{R}$$ ein Ring ist, folgt aus
$$F, \tilde{F}\in\mathcal{R}$$ auch $$F\setminus\tilde{F}\in\mathcal{R}$$.
Wenn also $$F\supseteq\tilde{F},$$ dann

$$\mu(F)=\mu((F\setminus \tilde{F}) \mathbin{\dot{\cup}} \tilde{F})=\mu(F \setminus
\tilde{F})+\mu(\tilde{F}) \geq
\mu(\tilde{F}) $$

Zur Eindeutigkeit: Sei $$\tilde{\mu}\from\mathcal{R}\to[0,\infty)$$
eine weitere Fortsetzung und ein Inhalt sowie $$F = \mathop{\dot{\bigcup}}_{k=1}^m B_k \in\mathcal{R}$$ mit
$$B_1, \ldots, B_m\in\H$$.
Dann ist

$$\tilde{\mu}(F)=\tilde{\mu}(\mathop{\dot{\bigcup}}
B_k)=\sum \tilde{\mu}(B_k)=\sum \mu(B_k)=\mu(F).$$

Zweite Anwendung, später in der Theorie:

**Lemma.** Sei $$(\Omega, \mathcal{A}, \mu)$$
ein Maßraum und $$f=\sum_{j=1}^n a_j \1_{A_j}$$ eine
einfache Funktion. Dann ist $$\int_\Omega f {~d}\mu:=\sum_{j=1}^n a_j \mu(A_j)$$
wohldefiniert.

*Beweis.* Für $$K\subseteq K_0:=\{1, \ldots, n\}$$
definiere

$$ B_K:=\bigcap_{k\in K}
A_k \cap \bigcap_{k \in K_0 \setminus
K}(\Omega \setminus A_k) $$

Dann ist
$$(B_K\st \varnothing \neq K
\subseteq K_0)$$ eine Zerlegung wie in Folgerung 2, und damit
$$\int f {~d}\mu=J(f)$$ wohldefiniert.
