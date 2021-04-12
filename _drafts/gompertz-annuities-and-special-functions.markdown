---
layout: post
title:  "Gompertz, annuities, and special functions"
---

This is part 2 of a 2 part series on Gompertz's law. [Part 1 is
here](/blog/2021/03/23/pis-deaths-and-statistics.html).

The [first part of this
series](/blog/2021/03/23/pis-deaths-and-statistics.html) discussed the
Gompertz distribution and gave a formula for "How
likely am I to live until at least age $$t_0 + t$$ conditional on
having lived until age $$t_0$$?". In this post, we will use this to
compute the present value of an annuities. This is a riff on chapter 3
of [Moshe Milevsky's book _The 7 Most Important Equations for Your
Retirement_](https://www.goodreads.com/book/show/13838804-7-most-important-equations-for-your-retirement)
with a more mathy twist.

### Present value

A standard idea in finance is that getting $$\$1000$$ today is worth more
than getting $$\$1000$$ in a year from now. This should be true even if
these are inflation-adjusted dollars: If we assume some bank will give
us the expected rate of inflation as their interest rate if we deposit
the $$\$1000$$, we could just do that and create the "$$\$1000$$ a year
from now" situation. Ignoring the dilemma of choice, the first situation
gives us more options and should therefore be worth more to us.

How much more should it be worth? Or, equivalently, what's the value
for $$y$$ at which point we become ambivalent about $$\$x$$ now and
$$\$y$$ in one year?

The answer will be different for different people (you may really need
that money _now_), but generally this is modeled with an
interest/discount rate as well: $$\$x$$ today will be worth $$\$x\cdot(1+r)$$
a year from now (and therefore $$\$x\cdot (1+r)^2$$ two years from now) for some
discount rate $$r$$. Why the temporal structure is exponential as
opposed to some other increasing function is a topic all for itself
(look up _hyperbolic discounting_), but it's a common choice in
various fields including finance, economics, psychology, neuroscience,
and reinforcement learning.

Conversely, $$\$y$$ in one year should be worth $$\frac{\$y}{1+r}$$
today.

### Getting money _forever_

A nice property of this discounting rule is that the option of getting
a neverending stream of money (say, $$a = \$1000$$ every month) is worth a
finite amount today by the magic of the geometric series:

$$
\sum_{n=0}^\infty \frac{a}{(1+r)^n} = \frac{a}{1-\frac{1}{1+r}}
= a \frac{1+r}{r} = a(1 + \tfrac{1}{r})
$$

for a monthly discount rate $$r\ne 0$$. Just to be extra clear: The
$$n$$th term of this sum is the present value of the payment we
receive in the $$n$$th period.

Such an arragement is called an _annuity_. We [talked about annuity
loans before on this blog](/blog/2019/08/20/annuity-loans.html) and
just as in that case, the present value of a neverending stream of
$$a$$ per month is $$a$$ times an _annuity factor_, in this case
$$\af(r)=1 + \frac{1}{r}$$.

The same is true if the annuity runs out after a fixed number of
periods. However, as a component of retirement planning, annuities
that pay for the rest of ones natural life (or the life of ones
spouse) tend to be a better option, as they
help covering _longevity risk_. In fact, annuities are (in theory,
although maybe not psychologically in practice) a great component for
retirement planning as they allow pensioners to take more risk with
the rest of their funds, e.g., stay invested in the stock market
where expected returns are higher (but so is the variance of returns).

### Getting money until you die

This raises a question: What's the present value of an annuity that
pays for the rest of ones life? It ought to be less than
$$1+\frac{1}{r}$$ times the annual amount (unless one expects to live
forever), but how much less exactly?

Our answer, of course, is the survival function of the Gompertz
distribution, as per the [last blog
post](/blog/2021/03/23/pis-deaths-and-statistics.html#plugging-it-all-together). Of
course this depends on the current age of the pensioner. As per the
last blog post, the survival function of the Gompertz distribution,
conditioned on having lived until year $$t_0$$, is

$$
p_{t_0}(t) := \exp\bigl(- e^{b(t_0-t_m)} (e^{bt} - 1)\bigr)
$$

where $$b \approx 1/9.5$$ is the inverse dispersion coefficient and
$$t_m \approx 87.25$$ is the modal value of human life.

The value of a pension that starts now (with a pensioner at age
$$t_0$$) and pays $$\$1$$ per year for the rest of the life is
therefore

$$
\af(r, t_0) =
\sum_{n=0}^\infty \frac{p_{t_0}(n)}{(1 + r)^n}.
\tag{#3} \label{discraf}
$$

The $$n$$th term in this series is the probabilty of alive at year
$$t_0 + n$$ given having been alive at year $$t_0$$ times the discount
rate that turns it into a present value.

This is equation #3 in Milevsky's book _The 7 Most Important Equations
for Your Retirement_.

Some insurance contracts allow the pensioner to decide between a lump
sum payment or an annuity; this formula can help to decide between
these options. Some contracts provide payments until death, but with a
minimum of (say) 10 years. Replacing $$p_{t_0}(0), \ldots,
p_{t_0}(9)$$ with $$1$$ in $$\eqref{discraf}$$ would model this situation.

Milevsky suggests using a spreadsheet program to sum this series,
along the lines of

$$n$$	| $$p_{65}(n)$$ | $$(1+r)^{-n}$$	| product
-:|-|-|-
70|93.6%|0.705|0.660
75|83.6%|0.497|0.415
80|69.1%|0.35|0.242
85|50.0%|0.247|0.124
90|29.0%|0.174|0.050
95|11.5%|0.122|0.014
100|2.4%|0.086|0.002
105|0.2%|0.061|0.000
 ||**∑**| **1.507**

In this example a pensioner of age 65 buys an annuity that gives them
$$\$1$$ every 5 years (starting at age 70) with a discount rate of
$$r=7.25\%$$. The present value of that annuity is $$\$1.51$$. If the
payment every 5 years is $$\$50.000$$ instead, the present value of the
annuity at age 65 is $$1.507\cdot \$50.000 = \$ 75369.90$$.

The example uses every 5 years in order to not be unduly
long. Typically, annuities will pay monthly. Even in a spreadsheet,
this becomes somewhat annoying.
Here's an [example in Google
sheets](https://docs.google.com/spreadsheets/d/1IvtfyU9qddNthHRmai9soHpTad79aNgUU_GRnEQlukU/edit#gid=2051005501). Notice
that the difference actually matters.

I wasn't quite satisfied with this.

### The hunt for a closed-form solution

Equation $$\eqref{discraf}$$ is nice and all, but it would be much
better to have a closed-form solution for it. Since $$p_{t_0}$$ is a
doubly-exponential function, this isn't immediately obvious. In fact,
I don't know a closed-form solution for $$\eqref{discraf}$$[^1].

[^1]: Although coming to think of this perhaps
    [Abel-Plana](https://en.wikipedia.org/wiki/Abel%E2%80%93Plana_formula)
    might help? I don't know if I want to try.

But let's imagine a world with continuous banking, where instead of
once a month I get a small portion of my annuity every moment. The
continuous annuity factor would then be

$$
\af_c(r, t_0)
=
\int_0^\infty p_{t_0}(t) e^{-rx} \,dx =
\int_0^\infty \exp\bigl(-\eta(e^{bx} - 1)\bigr) e^{-rx} \,dx
\tag{G.1}
\label{contaf}
$$

where $$\eta = e^{b(t_0 - t_m)}$$ as in the last blog post.[^2]

[^2]: There's some extra confusion regarding the interest rate here:
    For continuous compounding we need something else than the
    effective rate, as $$e^r - 1 \ne r$$ for $$r > 0$$. See [this
    answer](https://math.stackexchange.com/a/4099424/5051) for some
    explanation.

This, too, doesn't look super easy. In fact, it's not solvable with
"elemantary" functions. But somewhere within the large zoo of [special
functions](https://dlmf.nist.gov/) there is a right one for us here.

In this case, Wikipedia already tells us what the moment-generating
function (aka Laplace transform) of the Gompertz distribution is:

$$
\E(e^{-tx})
=
\eta e^{\eta}\mathrm{E}_{t/b}(\eta) \where{t>0}
$$

with the [generalized exponential integral](https://dlmf.nist.gov/8.19#E3)

$$
\mathrm{E}_{t/b}(\eta)=\int_1^\infty e^{-\eta v} v^{-t/b}\,dv \where{t>0}.
$$

The Gompertz distribution has the nice property that "left-truncated"
versions of itself are still Gompertz distributed (see the last blog
post for details). This is a consequence of the fact that its
survival function $$S(x) = \exp(-\eta(e^{bx}-1))$$ shows up in its
pdf $$f(x) = b\eta S(x)e^{bx}$$.

Hence,

$$
\E(e^{-tx}) = b\eta\int_0^\infty S(x) e^{-x(t-b)}\,dx
=
b\eta\af_c(t-b, t_0)  \where{t>0}.
$$

So the moment-generating function at $$t = r + b$$ gives us a
closed-form for $$\eqref{contaf}$$:

$$
\af_c(r, t_0)
=
\frac{1}{b\eta}\E(e^{-(r+b)x})
=
\frac{e^{\eta}}{b} \mathrm{E}_{1+r/b}(\eta)
=
\frac{1}{b}\exp(e^{b(t_0 - t_m)})\mathrm{E}_{1+r/b}(e^{b(t_0 - t_m)}).
\label{contaf-gef}
\tag{G.2}
$$

### Trying to use this

Formula $$\eqref{contaf-gef}$$ is in fact a closed-form solution to
our problem. So let's try to use this in a computations with
Python. [SciPy has the generalized exponential integral
function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.expn.html),
so this should be easy:

```python
import numpy as np
from scipy import special

b = 1 / 9.5
t_m = 87.25


def af(r, t_0):
    eta = np.exp(b * (t_0 - t_m))
    return np.exp(eta) / b * special.expn(1 + r / b, eta)


print(af(0.025, t_0=65))
```

and the output is:

```
gompertz_discount.py:10: RuntimeWarning: floating point number truncated to an integer
  return np.exp(eta) / b * special.expn(1 + r / b, eta)
19.439804660538815
```

Ah, dang! Even though the generalized exponential function is part of
SciPy, the implementation there only supports integer order.

We'll have to visit the special functions zoo a bit longer.

#### More zoo animals: The incomplete gamma function

The classic reference for special functions is [Abramowitz and
Stegun](https://en.wikipedia.org/wiki/Abramowitz_and_Stegun). Wikipedia
has a fun quote about it from the (American) National Institute of
Standards and Technology:

> More than 1,000 pages long, the Handbook of Mathematical Functions
> was first published in 1964 and reprinted many times [...] [W]hen
> New Scientist magazine
> recently asked some of the world’s leading scientists what single
> book they would want if stranded on a desert island, one
> distinguished British physicist said he would take the
> Handbook. [...] During the mid-1990s, the book was cited every 1.5
> hours of each working day.

In the internet age, the [Digital Library of Mathematical Functions
(DLMF)](https://dlmf.nist.gov/) hosts an updated version of this
classic work and it is very useful for situations like the one we are
in now.

In fact, looking at [equation (8.19.1)](https://dlmf.nist.gov/8.19#E1)
in DLMF, we see that the generalized exponential integral is nothing
but the (upper) incomplete gamma function:

$$
\mathrm{E}_p(z) = z^{p-1}\Gamma(1-p, z)  \where{p, z\in\C}
$$

and thus

$$
\af_c(r, t_0)
=
\frac{e^{\eta}}{b} \mathrm{E}_{1+r/b}(\eta)
=
\frac{\eta^{r/b}e^{\eta}}{b} \Gamma(-r/b, \eta).
$$

Alas, this won't do either. [SciPy's implementation of the incomplete
gamma
function](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gammaincc.html)
doesn't allow for a negative first argument.

Why might this be the case? Looking at the definition of the
incomplete gamma functions in DLMF ([8.2.2
there](https://dlmf.nist.gov/8.2#E2)), we read

$$
\Gamma(a, z) = \int_z^\infty t^{a-1}e^{-t}\,dt  \where{a, z\in\C, \
\Re a > 0}.
$$

Note how this is an "incomplete" version of the standard gamma
function $$\Gamma(a) = \Gamma(a, 0)$$. Also note how this integral
won't work for negative $$a$$: There's a singularity when $$z=0$$.

So did our previous formulae not make any sense? They did. We just
have to understand these functions a little bit better.

### Analytic continuation

_Complex analysis_, the theory of differentiable complex functions, is
one of the most beautiful areas of mathematics. In fact, I believe I
once saw a video of Donald Knuth saying it's such a great topic that
he asked his daughter to attend a complex analysis course -- although
she didn't otherwise study at any university.[^3]

At any rate one of the results of complex analysis is that if two nice
(aka complex-differentiable, aka holomorphic, aka analytic) functions
coincide on a set that's not totally discrete, they [are the
same](https://en.wikipedia.org/wiki/Identity_theorem)! This means any
analytic function like $$a\mapsto\Gamma(a, z)$$ has at most one
analytic continuation. This is an important principle which also
applies to the Riemann zeta function $$\zeta$$, the zeros of which
are what the [most important open mathematical problem is
about](https://en.wikipedia.org/wiki/Riemann_hypothesis) (you'll get
[$1M if you solve this
one](https://www.claymath.org/millennium-problems/riemann-hypothesis),
which should help with retirement planning). In fact, $$\zeta$$ and
$$\Gamma$$ are closely linked.

In the case of $$\zeta(s) := \sum_{n=1}^\infty n^{-s}$$ its unique
analytic continuation to the left complex halfplane yields for
instance $$\zeta(-1) = -\frac{1}{12}$$ which gives some sense to
Ramanujan's mysterious
equation $$1 + 2 + 3 + \cdots = -\frac{1}{12}$$.

How is such an analytic continuation found? In the case of both
the zeta and the gamma functions, it's via functional equations. For
instance, $$\Gamma(n) = (n-1)!$$ for integer $$n$$, and more generally
$$\Gamma(z+1) = z\Gamma(z)$$ for complex $$z$$. If we start with some
$$z$$ in the left
halfplane (i.e., $$\Im z \le 0$$), repeatedly applying this formula
eventually yields only terms of $$\Gamma$$ at "known" arguments, which
establishes the value of the analytic continuation of $$\Gamma$$ to
that point $$z$$.

For the incomplete Gamma function, a similar recurrence relation
exists, namely ([8.8.2](https://dlmf.nist.gov/8.8#E2) in DLMF)

$$
\Gamma(a+1, z) = a\Gamma(a,z) + z^ne^{-z}
$$

for, say, $$a$$ and $$z$$ in the right halfplane. This equation can be
used to extend the incomplete gamma function to negative values of
$$a$$. It also gives rise to a corresponding recurrence relation for the
generalized exponential integral
([8.19.12](https://dlmf.nist.gov/8.19#E12) in DLMF)

$$
p\mathrm{E}_{p+1}(z) + z\mathrm{E}_{p}(z) = e^{-z}.
$$

### Applying the functional equation

Since the implementations of $$\mathrm{E}_{p}(z)$$ and $$\Gamma(a,z)$$
that we want to use don't implementation the continued versions of
these functions, we can use the functional equations that define the
continuations ourselves. The recurrence relation for
$$\mathrm{E}_{p+1}$$ yields

$$
\begin{align}
\af_c(r, t_0)
& =
\frac{e^{\eta}}{b} \mathrm{E}_{1+r/b}(\eta)
=
\frac{e^{\eta}}{r}\bigl(e^{-\eta} - \eta\mathrm{E}_{r/b}(\eta)\bigr)
= \frac{1}{r}\bigl(1 - \eta e^\eta\mathrm{E}_{r/b}(\eta)\bigr)
\\
& = \frac{1}{r}\bigl(1 - e^\eta \eta^{r/b} \Gamma(1 - r/b, \eta)\bigr).
\end{align}
$$

For moderate values of $$r$$ (and $$b$$), this is enough. For very
large $$r$$ we'd have to apply the recurrence relation again.

This allows us to finally run this in Python:

```python
import numpy as np
from scipy import special

b = 1 / 9.5
t_m = 87.25


def af(r, t_0):
    eta = np.exp(b * (t_0 - t_m))
    return (
        1
        - np.exp(eta)
        * eta ** (r / b)
        * special.gamma(1 - r / b)
        * special.gammaincc(1 - r / b, eta)  # A normalized version of \Gamma(a, z).
    ) / r


print(af(0.025, t_0=65))
```

Which prints `14.79901377449508`.


[^3]: I might misremember this; at any rate I can't find the reference
    right now. It might have been part of his [1987 course series on
    mathematical writing](https://www.youtube.com/watch?v=mert0kmZvVM).
