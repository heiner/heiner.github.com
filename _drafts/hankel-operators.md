# Some specific integrals

## Early years

Two decades ago I was a math undergrad in Dresden, Germany.

At some point in the _Analysis I_ course they taught us about
solving integrals with the usual tricks: Integration by parts, substitution,
partial fractions. Unlike physics or some engineering undergrads, math
students would only see one or two examples and move on. I still
remember my
undergrad instructor Gerd Kayser mentioning how this wasn't proper
training and how when he was a student, math undergrads in socialist
East Germany had to do a preparatory course where they "had to solve 50
integrals".

"50 integrals is a lot", he said, "but when we
complained we were told students in the Sovient Union have to solve 500. But
afterwards they know how to solve integrals!"

The grace of my relatively late birth spared me having to do anywhere
close that many and I never got good at it. The art of detecting if
$$\tan\frac\theta 2$$ is the right substitution continues to be lost
on me.

In fact I was so bad at that sort of problem that my smart friends
gave me a personalized set of integration exercises a few years later:

<div class="centered">
<a href="/img/integrale_page1.jpeg" target="_blank"><img
src="/img/integrale_page1.jpeg" alt="42 integrals" style="width:200px;" /></a>
<a href="/img/integrale_page2.jpeg" target="_blank"><img
src="/img/integrale_page2.jpeg" alt="42 integrals" style="width:200px;" /></a>
<a href="/img/integrale_page3.jpeg" target="_blank"><img
src="/img/integrale_page3.jpeg" alt="42 integrals" style="width:200px;" /></a>

<div class="centered small">
42 integrals to solve. I still got until 2035!
</div>
</div>

Lucky for me most of math isn't about solving integrals. I eventually
got my diploma and moved on.

## Explicit but tricky

Moved on to doing a PhD in Mathematical Physics, that is. The quantum
mechancial problem discussed in my thesis ultimately doesn't
matter[^1] but it turned out that after applying a [trick by
Feynman](https://en.wikipedia.org/wiki/Feynman_parametrization)
to each term of a certain series I was left with,
ironically, an _explicit integral that required solving!_

[^1]: If you need to know, **Anderson's orthogonality catastrophe** —
    a phenomenon where the ground states of a Fermi
    gas before and after a tiny perturbation become *orthogonal* to
    each other as the system grows large. The overlap between them
    decays as a power law, and expanding the exponent into a series
    expression produced the integral $$I_n$$ for the $$n$$th term.
    But you don't actually need to know any of that.

Specifically, the $$n$$th term for $$n \ge 2$$ produced the
$$n$$-dimensional cyclic integral

$$I_n := \int_{(0,\infty)^n} \frac{e^{-\sum_{j=1}^n u_j}} {\prod_{j=1}^{n-1} (u_j +
u_{j+1})}\d u$$

where $$(0,\infty)^n$$ is the set of $$n$$-dimensional vectors
$$u\in\R^n$$ with positive entries $$u_j > 0$$, and $$u_{n+1} := u_1$$.

For small $$n$$, I could solve this: $$I_2 = 1$$, $$I_3 =
\frac{\pi^2}{4}$$, and $$I_4 = \frac{2\pi^2}{3}$$. I could also do
numerics and find that $$I_5 \approx 18.2642 \approx \frac{3\pi^4}{16}$$ and
$$I_6 \approx 51.9325\approx\frac{8\pi^4}{15}$$. But the iterated
integrals turned complicated very quickly. For $$n=6$$ the conjecture
$$I_6 = \frac{8\pi^4}{15}$$ is equivalent to

$$\int_0^1\mathrm{d}x \Bigl(\mathrm{Li}_2(\frac{x-1}{x})\Bigr)^2 =
\frac{17}{180}\pi^4$$

for the [dilogarithm](https://en.wikipedia.org/wiki/Dilogarithm)
$$\mathrm{Li}_2$$. This is not exactly an obvious formula, although it
turned out to be implied by results in the literature, which confirmed
the value for $$n=6$$.

#### Faith in math

The numerical results gave me a conjecture. It looked like
$$I_{2n+2} = (2\pi)^{2n} \frac{(n!)^2}{(2n+1)!}$$ might be correct.

When I plugged this result into my series expansion, the right power
series coefficients (the one for $$\arcsin^2$$)
would pop out and make the result of my thesis beautiful. The
conjecture _had_ to be true -- the result was too good to be false!

How to prove it though?

I asked [the
internet](https://mathoverflow.net/questions/129955/evaluation-of-an-n-dimensional-integral)
but without receiving a super satisfactory result. However, after I massaged
the integral a bit my collaborator Peter Otte found a solution using
insights from operator theory, in particular Hankel operators.

The integral for all $$n$$ turned out to be a implied by results
from the 1950s and earlier. To describe these, I have to go on a
slight tangent.

## The Hilbert Matrix

The "infinite matrix"

$$H =
\begin{pmatrix}
1 & \frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \cdots \\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \iddots \\
\frac{1}{3} & \frac{1}{4} & \iddots \\
\frac{1}{4} & \iddots \\
\vdots
\end{pmatrix}
$$

is known as the *Hilbert matrix*. Its entries at position $$j, k$$ are
$$\frac{1}{j + k - 1}$$. In numerical analysis, it
usually serves as cautionary tale about ill-conditioned systems.

Since the entries depend only on $$j+k$$, they are constant along the
anti-diagonals. Matrices with this property are called *Hankel
matrices*. The Hilbert matrix is the most famous example; below we
will see others.

On the space $$\ell_2(\N)$$ of square-summable sequences, it turns out
this matrix is *unitarily equivalent* (aka essentially the same under
a Hilbert space isomorphism) to the integral operator $$L_2(0, \infty)
\ni f \mapsto Tf \in L_2(0,\infty)$$ defined by

$$
(Tf)(x) = \int_0^\infty \frac{e^{-(x+y)/2}}{x+y}f(y)\,\d y.
$$

This integral operator is of the form $$(Tf)(x) = \int k(x, y) f(y)\,\d
y$$ with a _kernel_ $$k(x, y)$$ that depends only on $$x+y$$, not on
$$x$$ and $$y$$ separately. Such operators are known as *Hankel
operators*.

The orthonormal basis of $$L^2(0,\infty)$$ that makes this
correspondence to the Hilbert matrix work is given by the weighted [Laguerre
polynomials](https://en.wikipedia.org/wiki/Laguerre_polynomials)
$$\phi_n(x) = e^{-x/2}L_n(x)$$.

Rosenblum (1958) and later Rovnyak (1970) gave an explicit
diagonalization of this operator $$T$$. As with matrix
diagonalization, this allows us to compute "functions of the
operator", including its powers $$T^n$$. The details are a bit messy
and require a number of functions from the special functions zoo
(the Gamma function and the [Whittaker
functions](https://dlmf.nist.gov/13.14)). If you must know the details
you can check out my thesis.

Using these results, my integral expression could be turned into
something much more managable which eventually yields

% ??? do at least one scalar product with T^n

$$
I_n = (2\pi)^{n-2}
\frac{\bigl(\Gamma(\frac{n}{2})\bigr)^2}{\Gamma(n)},
$$

in particular $$I_{2n+2} = (2\pi)^{2n} \frac{(n!)^2}{(2n+1)!}$$, my
conjecture. My faith wasn't misplaced; through faith we understand the
universe.

Note that these kind of explicit integral expressions are unusual in
research mathematics -- in fact, some follow-up work by other
mathematicians lightly criticized our approach as "curious".

But I had fun with this integral. But not enough fun to stay in
research mathematics.

My co-author Martin Gebert pushed these results much
further. Curiously, that yielded more interesting integrals.

## A generalization of the Dirichlet integral and a failure

#### Dirichlet integral

The improper integral

$$
\int_0^\infty \frac{\sin x}{x} \d x = \frac{\pi}{2}.
$$

is a well-known classical result known as the [Dirichlet
integral](https://en.wikipedia.org/wiki/Dirichlet_integral). It's also the
final integral exercise in the above list of 42 integrals to solve.

Dirichlet's integral is "improper" in the sense that
the integrand $$\sinc(x) = \frac{\sin x}{x}$$ isn't actually integrable (the
integral $$\int_0^\infty \abs{\sinc(x)}\d x$$ isn't finite). While the
specific limit $$\lim_{L\to\infty}\int_0^L \sinc(x)\d x$$ exists, that
is due to cancellation from the sign change of $$\sin$$. This
cancellation depends on how the limit is done; this makes $$\sinc$$
not Lebesgue-integrable on unbounded intervals.

One way to prove Dirichlet's result is to use an [Abelian
theorem](https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems)
which in this form is also known as the ["final value theorem" of the
Laplace
transform](https://en.wikipedia.org/wiki/Final_value_theorem). It
states that _if_ the limit $$\lim_{L\to\infty} \int_0^L \frac{\sin
x}{x}\d x$$ exists, its value is the same as the limit of the
regularization of its integrand via the Laplace transform

$$
\lim_{s \downarrow 0} \int_0^\infty e^{-st} \frac{\sin(t)}{t} \d t.
$$

This expression can be evaluated for $$s > 0$$ with Laplace transform
tricks (essentially differentiating by $$s$$ to turn this into the
Laplace transform of $$\sin$$ itself). Its value turns out to be
$$\frac{\pi}{2} - \arctan s$$ and the $$\arctan$$ term goes to zero as
$$s\to 0$$.

This is an "Abelian theorem" which requires existence of the original
limit as one of its ingredients though. In this case, the existence is
provided by [Dirichlet's
test](https://en.wikipedia.org/wiki/Dirichlet%27s_test).

It's also an example of a common pattern in mathematics (which also is
the main approach in my PhD thesis): The quantity of interest is not
quite well behaved, but it's the limit of well-behaved expressions. So
one does a "regularization" (in this case the Laplace transform) which
turns it into a well-behaved expressions, does the required
calculations there, then goes back to something like the
original. There is extra work involved in doing and undoing the
regularization, but the benefit is that the main work can be done in a
better space.

However, that doesn't always work -- I failed to do the same for the
following problem:

#### A generalization of Dirichlet's integral

It turns out that in connection to the same quantum mechanical
phenomenon that lead to the $$I_n$$ integral, the integral

$$
S_n = \lim_{L\to\infty} \int_{(0, L)^n} \prod_{j=1}^n \frac{\sin(x_j +
x_{j+1})}{x_j + x_{j+1}} \d x \where{n \in 2\N + 1}
$$

pops up. I attempted to solve this using Hankel operator
diagonalizations from the literature. That seemed tempting because it
turns out the operator with $$\sinc$$ kernel is understood in the
literature -- it's been studied by Krein and others and while it's not
well-behaved (in particular, it's not trace class), it is the
_limit_ of well-behaved operators.

But ultimately I did not manage to make that approach work;
I did not understand regularized versions of it well enough.

or $$n=3$$ one can prove that $$S_3 = \frac{\pi^3}{16}$$, see [this stackexchange
question](https://math.stackexchange.com/q/2541613/5051).
It seems plausibe the general odd case is $$S_n =
\frac{\pi^n}{2^{n+1}}$$ but I know of no proof of that.

In attempting to solve $$S_n$$ along the same ways as $$I_n$$, I found
some interesting Hankel operator results in the literature. I didn't
ultimately find a way to use these, but they are fun on their own
right.[^2]

[^2]: Or perhaps they are not fun, but I wanted to write them down
      somewhere regardless.

## More Hankel matrices and operators

Modifications of the Hilbert matrix yield other interesting operators,
including the one involved in $$S_n$$:

#### Hilbert matrix

This one we saw above. With a $$\frac{1}{\pi}$$ normalization, this
operator has spectrum $$[0, 1]$$.

$$
\frac{1}{\pi}\begin{pmatrix}
1 & \frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \cdots \\
\frac{1}{2} & \frac{1}{3} & \frac{1}{4} & \iddots \\
\frac{1}{3} & \frac{1}{4} & \iddots \\ \vdots
\end{pmatrix}

\quad\longleftrightarrow\quad

\frac{1}{\pi}\int_0^\infty \frac{e^{-(x+y)/2}}{x+y} f(y) \, \d y
$$

#### Carleman operator

If we take the Hilbert matrix but put zeros into every other
anti-diagonal, it becomes unitarily equivalent to the *Carleman
operator* $$\int_0^\infty \frac{f(y)}{x+y}dy$$. Power (1980) shows
this via a chain of equivalences through the Hardy spaces
$$H_2(\R)$$ and $$H_2(\C_{\Im>0})$$. Carleman (1923) original work
showed its spectrum is $$[0, 1]$$.

$$
\frac{2}{\pi}
\begin{pmatrix}
1 & 0 & \frac{1}{3} & 0 & \frac{1}{5} \\
0 & \frac{1}{3} & 0 & \frac{1}{5} & \iddots \\
\frac{1}{3} & 0 & \frac{1}{5} & \iddots \\ \vdots
\end{pmatrix}

\quad\longleftrightarrow\quad

\frac{1}{\pi}\int_0^\infty \frac{1}{x+y} f(y) \, \d y
$$

#### Krein's example

An even more interesting operator was studied in "On Krein's example"
by Kostrykin and Makarov (2006) in connection with a perturbation
problem. They show its spectrum is $$[-1, 1]$$.
This sinc kernel $$\frac{\sin(x+y)}{x+y}$$ also shows up in
random matrix theory and many other places.

$$
\frac{2}{\pi}\begin{pmatrix}
\phantom{-}1 & \phantom{-}0 & -\frac{1}{3} & 0 & \frac{1}{5} \\
\phantom{-}0 & -\frac{1}{3} & \phantom{-}0 & \frac{1}{5} & \iddots \\
-\frac{1}{3} & \phantom{-}0 & \phantom{-}\frac{1}{5} & \iddots \\
\vdots
\end{pmatrix}

\quad\longleftrightarrow\quad

\frac{2}{\pi}\int_0^\infty \frac{\sin(x+y)}{x+y} f(y) \, \d y
$$

This is precisely the operator involved in $$S_n$$. But Krein's matrix
isn't trace-class, and I was unable to get a diagonalization for
a regularized version of it. So ultimately I did not find a good way
of using Krein's example for the $$S_n$$ integral above.

But I learned about the following:

## More Hilbert space equivalences

One thing I learned is how exactly these Hilbert spaces relate to each
other. Long story short, this diagram commutes:

<div class="centered">
  <img src="/img/hardy_commute.png" alt="Hardy spaces" />
</div>

This is the unitary equivalence that Power (1980) and others use. So
one could attempt to start with a regularized version of $$S_n$$ in
$$L_2(0, \infty)$$ and find what the equivalent matrix in
$$\ell_2(\N_0)$$ is. But the calculations involved look hard and I
didn't make too much progress.

However, I learned some interesting theory about Hardy spaces and the
Payley-Wiener theorem in the process. And finally solved some
integrals -- technically infinitely many, and therefore more than 500.

And yet I still am not great at integration exercises.


## Bibliography

- T. Carleman, *Sur les équations intégrales singulières à noyau réel et symétrique*, Almqvist and Wiksell, Uppsala, 1923. *(Introduces and analyzes the $$\frac{1}{\pi(x+y)}$$ operator; determines its spectrum as $$[0,1]$$.)*
- D. Hilbert, "Ein Beitrag zur Theorie des Legendre'schen Polynoms," *Acta Mathematica* **18** (1894), 155–159. *(Original appearance of the Hilbert matrix.)*
- H. Küttler, "Anderson's Orthogonality Catastrophe," dissertation, Ludwig-Maximilians-Universität München, 2014.
- V. Kostrykin and K. A. Makarov, "On Krein's example," arXiv:math/0606249 (2006). *(Proves the sinc-kernel operator $$K_\mu$$ has purely absolutely continuous spectrum $$[-1,1]$$; makes the connection to Hankel operator theory via Power's results explicit.)*
- S. C. Power, "Hankel operators on Hilbert space," *Bulletin of the London Mathematical Society* **12** (1980), 422–442. *(Excellent survey; contains the explicit unitary equivalence chain from the alternating matrix to Carleman's operator.)*
- M. Rosenblum, "On the Hilbert matrix, I," *Proceedings of the American Mathematical Society* **9** (1958), 137–140. *(Identifies the $$L_2(0,\infty)$$ operator via Laguerre functions and Whittaker functions.)*
{: refdef .simplelist}
