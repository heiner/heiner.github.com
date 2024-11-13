---
layout: post
title:  "Well-definedness in measure theory"
---

This blog covers very niche topics. Today: How to easily show that the
Lebesgue measure and the Lebesgue integral is well-defined.

I recently started reading the ["Bandit Algorithms" book
by Tor Lattimore and Csaba
Szepesvari](https://banditalgs.com). [I like it a
lot.](https://twitter.com/HeinrichKuttler/status/1343551842580639750)
Chapter 2 there got me back to
one of my favorite topics in math: Measure Theory. While measure
theory is often held as being boring or dry, I disagree. It's just
often presented in a suboptimal way. In particular, many authors get
so carried away by a progression of simple functions -- positive
functions -- real-valued functions that they forget that linearity is a
great thing (one symptom of this: Trying to find a "common partition"
for two simple functions).

Here we present a simple lemma and its corollary that takes care of
most well-definedness questions in measure theory, in particular: Why
the extension of a pre-measure from a semiring to a ring is
well-defined (and therefore unique), and why the Lebesgue integral of
simple functions is well-defined.

**Lemma 1.** Let $$\H$$ be a family of sets with the following partition
property: For each finite family $$(A_1, \ldots, A_n)$$ in $$\H$$
there is a finite disjoint family $$(B_k\st k \in
K_0)$$ in $$\H$$ such that

$$\forall j \in\set{1,\ldots,n}\, \exists K_j \subseteq
K_0: A_j=\mathop{\dot{\bigcup}}_{k \in K_j} B_k.$$

(In particular, either $$A_j \supseteq B_k$$ or $$A_j\cap
B_k=\emptyset$$ is true at all times, with
$$A_j\supseteq B_k \Leftrightarrow k \in K_j.$$)

Let $$\mu\from \H\to[0, \infty)$$ be an additive set function (i.e.,
if $$A, B\in\H$$ are disjoint with $$A\mathbin{\dot{\cup}} B\in\H$$,
then $$\mu(A\mathbin{\dot{\cup}} B) = \mu(A) + \mu(B)$$). Let $$A_1, \ldots, A_n \in
\H$$ and $$a_1, \ldots, a_n \in \F \in\set{\R, \mathbb{C}}$$. Define

$$\qquad b_k:=\sum_{\substack{1\le j\le n\\ A_j\supseteq B_k}} a_j \where{k\in K_0}.$$

Then $$\sum_{j=1}^n a_j \1_{A_j}=\sum_{k\in K_0} b_k\1_{B_k}$$ and

$$ \sum_{j=1}^n a_j \mu(A_j)=\sum_{k \in K_0} b_k
\mu(B_k)$$

*Proof.* The first statement follows directly from the definition of
$$b_k$$. The second:

$$\begin{aligned} \sum_{j=1}^n a_j \mu(A_j)
&=\sum_{j=1}^n a_j \sum_{k \in K_j}
\mu(B_k) \\ &=\sum_{k \in K_0}
\underbrace{\sum_{j=1}^n \1_{K_j}(k) a_j}_{=b_k}
\mu(B_k)=\sum_{k \in K_0}
b_k \mu(B_k).  \qquad\text{//}\end{aligned}$$

**Corollary 2.** Let $$\H, \mu$$ as in Lemma 1. Let
$$X:=\lin\set{\1_A\st A\in\H}$$. Then $$J\from X\to\F$$, defined via

$$X\ni f=\sum_{j=1}^n a_j \1_{A_j} \mapsto \sum_{j=1}^n a_j \mu(A_j),$$

is well-defined and linear.

*Proof.* It suffices to treat the case $$f=0$$. Let
$$(B_k\st k \in K_0)$$ be the disjoint representation and $$(b_k\st b
\in K_0)$$ as in Lemma 1. Then $$b_k=0$$ for all $$k \in k_0,$$ as
$$f=\sum_{j=1}^n a_j \1_{A_j}=\sum_{k \in
K_0} b_k \1_{B_k}$$ and the $$B_k$$ are pairwise disjoint. By Lemma 1,

$$\sum_{j=1}^n a_j \mu(A_j)
% =\sum_{j=1}^n a_j \mu(\mathop{\dot{\bigcup}}_{k \in k_j}B_k)
= \sum_{k\in K_0} b_k \mu(B_k)=0.$$

This shows $$J$$ is well-defined; it's also clearly linear. //


With this simple tool, we can look at our first application: The
Lebesgue-Stieltjes pre-measure.

**Lemma 3.** Let $$\H$$ be the set of half-open intervals and let
$$\mathcal{R}$$ be the ring of finite unions of
half-open intervals. Then each $$F \in \mathcal{R}$$ is the disjoint
union of finitely many intervals.

*Proof* (Adapted from [J. Voigt, "Einführung in die Integration", Satz 1.1.1](http://www.math.tu-dresden.de/~voigt/mui/mui.pdf#page=7)).
Let $$F=\bigcup_{j=1}^n
I_j$$ with $$I_j=[a_j, b_j)$$.
The set $$\set{a_j, b_j\st j=1,\ldots,n}$$ can be written as
$$\set{x_k\st k=0,\ldots,m}$$ with $$x_0 <x_2 < \cdots < x_m$$. A set
of disjoint intervals with union $$F$$ is

$$\{[x_{k-1}, x_k)\st
1\le k\le m \text{ and } \exists j\in\set{1,\ldots,n} :
[x_{k-1}, x_k) \subseteq[a_j,b_j)\}.  \qquad\text{//}$$

**Corollary 4.** Let $$G\from\R\to\R$$ be
monotone. The mapping $$\mu\from\H\to[0,\infty)$$,
defined via $$\mu([a,b)) := G(b)-G(a)$$, can be uniquely extended to
an additive set function $$\mu\from\mathcal{R}\to[0, \infty)$$.

*Proof.* $$\mu$$ is additive and $$\H$$ has the partition property
from Lemma 1 by Lemma 3. Hence $$J\from X\to\F$$ from Corollary 2 is
well-defined. Let $$F\in\mathcal{R}$$. Then
$$\1_F\in X$$ and thus $$\mu(F):=J(\1_F)$$ is well-defined and $$\geq 0$$.
This extension $$\mu$$ is additive, since for $$\tilde{F}\in\mathcal{R}$$,

$$
\mu(F \mathbin{\dot{\cup}} \tilde{F}) =
J(\1_F+\1_{\tilde{F}}) = J(\1_F) + J(\1_{\tilde{F}}) =
\mu(F)+\mu(\tilde{F}).
$$

For the uniqueness: Let $$\tilde{\mu}\from\mathcal{R}\to[0,\infty)$$
be another additive extension and let $$F =
\mathop{\dot{\bigcup}}_{k=1}^m B_k \in\mathcal{R}$$ with $$B_1, \ldots, B_m\in\H$$.
Then

$$\tilde{\mu}(F)=\tilde{\mu}(\mathop{\dot{\bigcup}}
B_k)=\sum \tilde{\mu}(B_k)=\sum \mu(B_k)=\mu(F).  \qquad//$$

If $$G$$ left-continuous, $$\mu$$ can be shown to be
$$\sigma$$-additive (and hence a pre-measure). One can then use
Carathéodory's extension theorem to extend $$\mu$$ to a measure on the
$$\sigma$$-algebra generated by $$\mathcal{R}$$, which is the Borel
$$\sigma$$-algebra $$\mathcal{B}(\R)$$.

Later in the theory, Lemma 1 proves the well-definedness of the
Lebesgue integral for simple functions:

**Lemma 5.** Let $$(\Omega, \mathcal{A}, \mu)$$ be a measure space and
let $$f=\sum_{j=1}^n a_j \1_{A_j}$$ be a simple function.
Then $$\int_\Omega f {~d}\mu:=\sum_{j=1}^n a_j \mu(A_j)$$ is well-defined.

*Proof.* For $$K\subseteq K_0:=\{1, \ldots, n\}$$, define

$$ B_K:=\bigcap_{k\in K}
A_k \cap \bigcap_{k \in K_0 \setminus
K}(\Omega \setminus A_k) $$

Then $$(B_K\st \emptyset \neq K
\subseteq K_0)$$ is a partition as in Corollary 2, and hence
$$\int f {~d}\mu=J(f)$$ is well-defined. //

This defines the Lebesgue integral for simple functions. Since simple
functions are dense in $$L_1(\mu)$$, one is tempted to just use the
[BLT
theorem](https://en.wikipedia.org/wiki/Continuous_linear_extension)
now. That doesn't quite work however, since the norm of $$L_1(\mu)$$
is defined via that integral in the first place. Instead, one can now
define the integral for positive functions via pointwise convergence
almost everywhere from below, then extend to real-valued (and
complex-valued) functions.
