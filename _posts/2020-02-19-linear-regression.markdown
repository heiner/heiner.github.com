---
layout: post
title:  "On linear regression"
---

<small>[Edit 14 May 2020: Thanks to Marcus Waurick for pointing out $$A$$
needs to be closed for Lemmas 1 and 2 to be true in
general. Unfortunately, there seems no easy way of doing linear
regression in general Hilbert spaces (no equivalent of $$\1$$,
although the idea of using weighted $$L_2$$ spaces and writing a
blog post on _Linear Regression in Hilbert spaces with Morgenstern
norm_ has a certain ring to it.]</small>


Apropos of nothing, this is a post about linear regression. There's a
whole world of information on that out there, but little with the
right point of view: The Hilbert space perspective. That might not
be universally loved, so you might feel more comfortable reading
$$\H_1 = \R^m$$, $$\H_2 = \R^n$$ and "matrix" in place of "linear
operator" below.

We'll do the short theory up front, then look at an example, then
say something about "fraction of variance explained". A later blog
post will discuss the CAPM, French-Fama models and efficient markets as examples.

## Two lemmas.

Let $$\H_1$$, $$\H_2$$ be Hilbert spaces and $$A\in L(\H_1,\H_2)$$ be
a closed linear operator.

**Lemma 1.**&nbsp; $$\H_2 = \im A\oplus\ker A^*$$ in the sense of direct sums
of Hilbert spaces.

*Proof* Let $$x\in\im A$$, $$y\in\ker A^*$$. There is a $$x_1\in\H_1$$
with $$x = Ax_1$$ and

$$\langle x,y\rangle = \langle Ax_1, y\rangle = \langle x_1, A^*
y\rangle = 0.$$

Thus $$\im A\perp\ker A^*$$.

Reversely let $$y\in(\im A)^\perp$$. Then $$0 = \langle Ax_1,
y\rangle = \langle x_1, A^* y\rangle$$ for all $$x_1\in\H_1$$, and
thus $$y\in\ker A^*$$.  &nbsp;//

**Lemma 2.**&nbsp; Let $$P\from\H_2\to\im A$$ be the orthogonal
projection.

(a) Let $$y\in\H_2$$. Then there is a $$b\in\H_1$$ such that $$A^*Ab =
A^*y$$ and $$Py = Ab$$. This is called the *normal equation*.

(b) If $$\ker A = \{0\}$$, i.e., $$A$$ injective, then $$P =
A(A^*A)^{-1}A^*$$.

*Proof.* (a) There is $$b\in\H_2$$ with $$Py = Ab$$. Also $$y - Py\in(\im
A)^\perp$$, and thus by Lemma 1

$$0 = A^*(y -Py) = A^*(y - Ab) = A^*y - A^*Ab.$$

(b) Lemma 1 implies $$\H_1 = \im A^*\oplus\ker A = \im A^*$$,
i.e. $$A^*$$ is surjective. Since $$\im A = (\ker A^*)^\perp$$ and
evidently $$A^*\from(\ker A^*)^\perp\to\H_1$$ is injective, that
mapping is bijective. Additionally
$$A\from\H_1\to\im A$$ is bijective, and thus $$A^*A\from\H_1\to\H_1$$
is bijective and invertible. Using (a) it follows that $$Py = Ab =
A(A^*A)^{-1}A^*y$$.  &nbsp;//


## Linear regression as projection to subspaces.

### Example: Warships

To take a [favorite example from German
Wikipedia](https://de.wikipedia.org/wiki/Bestimmtheitsma%C3%9F#Rechenbeispiel),
let's discuss warships from the Second World War. Let's say we've got
$$x_1\in\R^n$$, a list of lengths of $$n$$ warships, $$x_2\in\R^n$$ a list
of their beams (widths) and $$y\in\R^n$$ a list of their
drafts (distance from bottom to waterline), all in meters. We call
$$x_1$$ and $$x_2$$ *feature vectors* (also known as *explanatory* or
*independent* variables) and can safely assume they are
linearly independent, such that the matrix

$$A = \begin{pmatrix}
  | & | \\
  x_1 & x_2 \\
  | & |
\end{pmatrix}\in\R^{n\times 2}$$

defines an injective operator. Its image is the linear span of $$x_1$$
and $$x_2$$, i.e., $$\im A = \{\alpha x_1 + \beta x_2 \st \alpha,
\beta\in\R\}\subseteq\R^n$$. We wouldn't expect $$y$$ to be an element
of $$\im A$$, but the hope of a linear regression model trying to
predict a warship's draft from its length and beam is that $$y$$
is not too far from $$\im A$$ as a subspace of $$\R^n$$
either. Specifically, the $$\abs{\dotid}_2$$-distance is

$$\dist(\{y\}, \im A) = \min_{y'\in\im A}\abs{y - y'}_2 = \abs{y - P y}_2$$

where $$P\from\R^n\to\im A$$ is the orthogonal projection. We can call
$$Py$$ the model's prediction, and Lemma 2 above tells us how to
compute $$P$$ from $$A$$, namely $$P = A(A^\top A)^{-1}A^\top$$. Moreover, the
normal equation tells us which linear combination[^1] of $$x_1$$ and $$x_2$$
computes $$Py$$:

$$Py = A(A^\top A)^{-1}A^\top y = Ab \;\text{ with }\; b = (A^\top
A)^{-1}A^\top y\in\R^2.$$

[^1]: In situations with very many feature vectors, computing the
    inverse $$(A^\top A)^{-1}$$ may no longer be the best way of
    finding $$b$$. Instead, one could try to minimize $$\abs{y-Ab}_2$$
    in another way, e.g. via gradient descent. This is how "linear
    layers" in machine learning are trained.

Thus, if we are given an additional warship's length and beam as a
vector $$a\in\R^2$$, the model's prediction of its draft will be
$$\langle a, b\rangle$$.

We can implement this idea in simple Python code ([Colab
link](https://colab.research.google.com/drive/1lPXUxTBDrRC8aZ7MqZZDkvKaUz5Ogh5b){:target="_blank"}):

```python
import numpy as np

# Lengths, beams and drafts of 10 warships
data = """
187	31	9.4
242	31	9.6
262	32	8.7
216	32	9
195	32	9.7
227	31	11
193	20	5.2
175	17	5.2
""".split("\n")

lengths, beams, drafts = np.loadtxt(data, unpack=True)
A = np.stack([lengths, beams], axis=1)
b = np.linalg.inv(A.T @ A) @ A.T @ drafts
print("b:", b)
print("model prediction:", np.array([200, 20]) @ b)
```

This will print
```text
b: [-0.00539494  0.34045321]
model prediction: 5.730077087608246
```

So our model would predict a hypothetical warship with length 200m
and beam 20m to have 5.73m of draft.

Notice that the way we built our model makes it predict a draft of
zero for the (nonsensical) inputs of a warship
of zero meters length or beam. While this seems fine enough in this
case, it's not in others. A simple way of fixing this is to add an
"intercept" (in machine learning known as "bias") term: Define
$$\1=(1,\ldots,1)\in\R^n$$ and add that as an additional (say, first)
"feature" vector. This turns our model into an affine function of its
data inputs. Doing this in our Python example changes little:

```python
A = np.stack([np.ones_like(lengths), lengths, beams], axis=1)
b = np.linalg.inv(A.T @ A) @ A.T @ drafts
print("b:", b)
print("model prediction:", np.array([1, 200, 20]) @ b)
```

Result:

```text
b: [ 0.09353128 -0.00580401  0.34027063]
model prediction: 5.738140993529072
```

However, trying to predict crew sizes changes that, see the [Colab for
details](https://colab.research.google.com/drive/1lPXUxTBDrRC8aZ7MqZZDkvKaUz5Ogh5b){:target="_blank"}.

Of course, we can use more than two or three feature vectors as part
of the *design matrix* $$A$$, as long as they are linearly
independent, which is is typically the case in practice with enough
examples $$n$$.

Using a matrix $$Y\in\R^{n\times m}$$ in place of
$$y\in\R^n$$ the same math allows us to succinctly treat the
"multivariate" case in which we're trying to predict more than one
"dependent variable", e.g. a warship's draft and the size of its
crew. This is just doing more than one linear regression at once.


### $$R^2$$ and all that

As mentioned above, the distance $$\abs{y - Py}_2$$ gives us a sense
of the quality of our model's predictions when applied to the data we
built it on. The textbooks, being obsessed with element-wise
expressions, call $$\abs{y - Py}_2^2$$ the *residual sum of squares*.

While this quantity (or a normalized version of it) is a measure of
the error our model produces on the data we know, it doesn't tell us
if it was our input data that was useful in particular. To quantify
that, we can compare it with a minimal, "inputless" model built from only
the intercept entry, i.e., using $$A_\1 = \1$$. The prediction of that model
will be the mean of the data, $$\frac{1}{n}\langle y,
\1\rangle$$, and the orthogonal projection on $$\im A_\1 =
\lin\{\1\}$$ is $$P_1y = \frac{1}{n}\langle y, \1\rangle\1$$. The
squared distance $$\abs{y - P_\1y}_2^2$$ of that minimal model's
predictions from the data is known as the *total sum of squares*. It's
also the unnormalized variance of the data. If our original model used
an intercept term, i.e., $$\1\in\im A$$, then $$Py - P_1y\in\im A$$
and therefore $$y - Py \perp Py - P_1y$$. Hence, the Pythagorean
identity tells us

$$\abs{y - P_1y}_2^2 = \abs{y - Py + Py - P_1y}_2^2
  = \abs{y - Py}_2^2 + \abs{Py - P_1y}_2^2.$$

The last term is known somewhat factitiously as the *explained sum of
squares* with the idea that it measures deviations from the mean
caused by the data.

The ratio $$\abs{y - Py}_2^2 / \abs{y - P_1y}_2^2$$ is called the
*fraction of variance unexplained*, although one has to be careful
with that terminology.
The *coefficient of determination* is one minus that number, or

$$R^2 := 1 - \frac{\abs{y - Py}_2^2}{\abs{y - P_1y}_2^2}
      = \frac{\abs{Py - P_1y}_2^2}{\abs{y - P_1y}_2^2},$$

where the last equality is true if and only if $$\1\in\im A$$.

**Adjustments.**&nbsp; Since including more features in our model matrix
$$A$$ will make
$$\im A$$ a larger subspace of $$\R^n$$, the error $$\abs{y -
Py}_2^2$$ will be monotonically decreasing and $$R^2$$ monotonically
increasing.  While this offers the
opportunity to claim to "explain" more, it might in fact make our
model's predictions on new inputs worse. Various solutions for this
have been proposed. One somewhat principled approach is to use
"adjusted $$R^2$$", defined as

$$\bar{R}^2 = 1 - \frac{\abs{y - Py}_2^2 / (n - p - 1)}{\abs{y -
P_1y}_2^2 / (n - 1)} \le R^2,$$

where $$p$$ is the number of features, i.e., $$A\in\R^{n\times
(p+1)}$$ if we use an intercept term. This substitutes the unbiased
sample variance and error estimators for their biased versions.



That's it for now. We'll add a proper example from finance in a future
blog post.
