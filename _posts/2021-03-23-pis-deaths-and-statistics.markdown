---
layout: post
title:  "πs, deaths, and statistics"
---

This is part 1 of a 2 part series on Gompertz's law.

After enjoying a [podcast interviewing Moshe
Milevsky](https://rationalreminder.ca/podcast/122), I got interested
in Milevsky's work and read his book _The 7 Most Important Equations for Your
Retirement_.

It's a bit of a weird book. I can't say I didn't enjoy it. But it
gave me the impression Moshe Milevsky didn't expect his readers to enjoy the
book, or at least he didn't seem to expect them to like the formulas. That
seems like a weird proposition for a book with "equations" in its
very title. Perhaps the readers were imagined to be part of a
captured audience of students, asked to read the book as an
assignment? At any rate the author apologizes every time he actually
discusses formulae, and having to resort to _logarithms_ seems to make
him positively embarrassed.

Then again, Prof. Milevsky wrote many books and this is apparently one
of his bestsellers. And
the anecdotes of Fibonacci, Gompertz, Halley, Fisher, Huebner, and
Kolmogorov[^1] in the book are lovely, as is Milevsky's account of his
experience of economist Paul Samuelson. Perhaps the professor just
knows his audience.

[^1]: For Kolmogorov, I'd love to have another reference for his
      supposed _War and Peace_-inspired nickname "ANK". The book in question
      is the only reference I could find.

But so do I, being well acquainted with the empty set. So there's no
issue with too much math on this blog.

Let's therefore discuss what Milevsky doesn't do in his book and try
to explain why his equation #2 might be true: Let's talk about the
Gompertz distribution.

### Gompertz's discovery

<div class="floated">
<img src="/img/gompertz.png" alt="Benjamin Gompertz" style="width:200px;" />
<br />
<div class="centered small">
Image source: <a href="https://en.wikipedia.org/wiki/Benjamin_Gompertz#/media/File:Gompertz.png">Wikipedia</a>
</div>
</div>


Benjamin Gompertz (1779--1865) was a British mathematician and actuary
of German Jewish descent. According to Milevsky, Gompertz was looking
for a law of human mortality, comparable to Newton's laws of
mechanics. At his time, statistics of people's lifespan were already
available and formed the basis for Gompertz's discovery. For instance,
one could compile a _mortality table_ of a (hypothetical) group of
45-year-olds as they age. The data might look like this:


Age|Alive at Birthday|Die in Year
-|-|-
45|	98,585|	146
46|	98,439|	161
47|	98,278|	177
48|	98,101|	195
49|	97,906|	214
50|	97,692|	236

What does this tell us? It doesn't immediately tell _me_ anything not
very obvious: The older one gets, the more likely one dies soon.

But let's
compute the _mortality rate_: How likely were people to die at a given
age in this cohort? To be precise, we compute "_Which proportion of
people alive at age $$t$$ died before age $$t+1$$?"_

Age|Alive at Birthday|Die in Year| Mortality Rate
-|-|-|-
45 | 98,585 | 146 | 0.148%
46 | 98,439 | 161 | 0.164%
47 | 98,278 | 177 | 0.180%
48 | 98,101 | 195 | 0.199%
49 | 97,906 | 214 | 0.219%
50 | 97,692 | 236 | 0.242%

So again, so much so obvious: The probability of dying the next year,
conditional on having lived until the current year,
increases with age.

But _how much_ does it increase? This is
Gompertz's discovery, now called Gompertz's law: The mortality rate
appears to increase exponentially. One way of seeing this is to take
logs and compute their difference:

Age|Alive at Birthday|Die in Year| Mortality Rate|Log of Mortality Rate|Difference in Log Values
-|-|-|-|-
45 | 98,585 | 146 | 0.148% | −6.515 | ---
46 | 98,439 | 161 | 0.164% | −6.416 | 0.0993
47 | 98,278 | 177 | 0.180% | −6.319 | 0.0964
48 | 98,101 | 195 | 0.199% | −6.221 | 0.0987
49 | 97,906 | 214 | 0.219% | −6.126 | 0.0950
50 | 97,692 | 236 | 0.242% | −6.026 | 0.1000

The difference in log values increases by about 0.1, regardless of the
current age. Since $$\exp(0.1) \approx 1.1$$, this works out to
roughly a 10% increase in the mortality rate per year.

<b>According to Gompertz's discovery, the likelihood of dying in the
next year (conditional on having lived until this year) increases
exponentially by a fixed percentage every year.<b>

How do we model this mathematically? And if Gompertz's law has a
rate growing by a rate, how come everything stays a probability, i.e.,
$$\le 1$$?

Keep reading to learn about hazard functions and find out!

### PDFs, CDFs, and Hazard Functions

<div class="floated">
<img src="/img/gompertz-pdf.svg" alt="pdf" style="width:250px;" />
<br />
<div class="centered small">
Some probability density functions<br />
Image source: <a
href="https://en.wikipedia.org/wiki/File:GompertzPDF.svg">Wikipedia</a>
</div>
<img src="/img/gompertz-cdf.svg" alt="cdf" style="width:250px;" />
<br />
<div class="centered small">
Some cumulative distribution functions<br />
Image source: <a
href="https://en.wikipedia.org/wiki/File:GompertzCDF.svg">Wikipedia</a>
</div>
</div>

If you have taken a probability or statistics course, you probably
(ha!) know about _probability density functions_ (pdfs). A pdf is a
positive function that we use as a density and to make it a
_probabilty_ density it needs to integrate to one. If $$f$$
is a pdf and $$X$$ is a random variable with that distribution then

$$\P(a < X\le b) = \int_a^b f(x) \dx,$$

i.e., the probability of $$X$$ landing between $$a$$ and $$b$$ is the
integral from $$a$$ to $$b$$ of $$f$$.[^2] Let's say our random
variable takes only positive values, then for $$a=0$$ and $$b=\infty$$
this value will be $$1$$, i.e., 100%. For smaller values of $$b$$ this
will be the so-called cumulative distribution function (cdf):

$$F(b) := \P(X\le b) = \int_0^b f(x)\dx.$$

[^2]: This works for probability measures that are absolutely
      continuous with respect to the Lebesgue measure, meaning such a
      Lebesgue density exists. All measures on the reals can be decomposed
      into such a measure, a discrete measure and a so-called singular
      continuous measure. Let's just stay with Lebesgue densities here.

While pdfs are positive and integrate to $$1$$, cdfs are positive, $$0$$
at $$0$$, monotone (non-decreasing), and $$1$$ at the limit to
$$\infty$$. They are also typically assumed to be
right-continuous. To compute the previous expression one can then
take

$$\P(a < X \le b) = \int_a^b f(x) \dx = F(b) - F(a).$$

Moreover the fundamental theorem of calculus tells us that (barring a
few exceptional points),

$$F'(x) = f(x).$$

What this means is that the cdf determines the pdf and therefore the
probability distribution itself: Any function $$F$$ with the properties
above can serve as a cdf and gives rise to a pdf $$f$$, and vice
versa.

If you made it this far, you likely knew this in principle. So on to
hazard functions now (which I learned about from
[Wikipedia](https://en.wikipedia.org/wiki/Survival_analysis#Hazard_function_and_cumulative_hazard_function)
only recently).

#### Hazard functions

<div class="floated">
<img src="/img/gompertz-hazard.svg" alt="hazard" style="width:250px;" />
<br />
<div class="centered small">
Some hazard functions<br />
<a href="/img/gompertz.gp">Gnuplot source</a>
</div>
</div>

If we imagine $$f$$ to describe deaths (or failure rates) over time,
$$F(t)$$ will be the probability to have died by time
$$t$$. Conversely, $$S(t) := 1 - F(t)$$ (the _survival function_) is
the chance to still be alive at time $$t$$. If $$f$$ is the
corresponding pdf and $$X$$ is a random variable with this
distribution,

$$S(t) = \P(X > t) = \int_t^\infty f(x)\dx = 1 - F(t).$$

Suppose we made it until some time $$t_0 \ge 0$$. How will the future
look like? We will need to condition on having lived so far and
renormalize with $$S(t_0)$$ to get the pdf going forward. This is the
same as finding the probability of not surviving an additional
infinitesimal time:

$$h(t_0) := \frac{f(t_0)}{S(t_0)}
  = \lim_{t\downarrow 0} \frac{\P(t_0\le X < t_0 + t)}{t S(t_0)}
  = -\frac{S'(t_0)}{S(t_0)} = - \frac{\d}{\d t}\ln(S(t))\Biggr\rvert_{t=t_0}.$$

This is the _hazard function_, also known as _force of mortality_ or
_force of failure_. It takes positive values and the last equation
indicates that it will not be integrable, i.e., $$\int_0^\infty
h(x)\dx = \infty$$.

There is also the _cumulative hazard function_, which is

$$H(t) = \int_0^t h(x)\dx = -\ln S(t).$$

This last equation, which follows from the above, tells us something
interesting: We ought to be able to retrieve $$S$$, and therefore the cdf
$$F$$, and therefore the pdf $$f$$, from $$h$$ itself, because

$$S(t) = e^{-H(t)}.$$

This means, just as any one of a pdf or a cdf determines the other, so
does a hazard function: Given either a pdf, a cdf, or a hazard
function (or a cumulative hazard function), the probability density and
therefore all of these functions and the entire distribution are
uniquely determined. The criteria
for $$h$$ are: (1) being nonnegative and (2) not being integrable.

### Back to Gompertz

So how do we model Gompertz's discovery? We choose the most
simple exponentially growing function we know and take it as our hazard
function:

$$h(t) := b \eta e^{bt}$$

where $$\eta, b > 0$$ are parameters to be determined from the
data (see below). This also tells us why our "rate increase of a rate"
doesn't lead to probabilities greater than one over time: It's a rate
increase for the conditional probability at that fixed point in time
$$t_0$$. The hazard function itself does grow to infinity.

Given this, what is the cdf for this _Gompertz distribution_? Well,

$$H(t) = \int_0^t h(x)\dx = b \eta\int_0^t e^{bx}\dx
  = \eta(e^{bt} - 1)$$

and therefore

$$F(t) = 1 - S(t) = 1 - e^{-H(t)} = 1 - \exp\bigl(-\eta(e^{bt} -
1)\bigr)$$

and

$$f(t) = h(t)S(t) = b\eta\exp\bigl(bt - \eta(e^{bt} - 1)\bigr).$$

So the simple exponential choice for the hazard function yields this not
quite so simple double exponential as a pdf for the Gompertz
distribution.

<div class="centered">
<img src="/img/gompertz-pdf.svg" alt="pdf" style="width:30%;"/>
<img src="/img/gompertz-cdf.svg" alt="cdf" style="width:30%;"/>
<img src="/img/gompertz-hazard.svg" alt="hazard" style="width:30%;"/>
<br />
The pdf, cdf and hazard function of the Gompertz distribution for some
choices of \(\eta\) and \(b\). <br />
(See above for source.)
</div>

We could proceed to compute the mean, variance or
moment-generating function (aka Laplace transform) of this
distribution, but the math gets somewhat hairy and special functions
(mainly the [generalized exponential
integral](https://dlmf.nist.gov/8.19), a special function related to
the incomplete gamma function) are involved. We
will return to this for other reasons in a future blogpost. The
[infobox on
Wikipedia](https://en.wikipedia.org/wiki/Gompertz_distribution) has
the data if necessary.

For now, let's note that $$h(t) = b \eta e^{bt}$$ describes a hazard
function where the chance of dying in the next moment increases
throughout life, but there's only this time-dependent component. If
there are time-independent causes of death or failure (war, some kinds of
diseases, voltage surges), one could consider modelling this
differently. William Makeham, another British 19th century
mathematician, proposed such an addition via the hazard function

$$h(t) = b \eta e^{bt} + \lambda.$$

The result is known as the [Gompertz-Makeham
distribution](https://en.wikipedia.org/wiki/Gompertz%E2%80%93Makeham_law_of_mortality).

As simple as this change may seem, it does complicate the resulting
integrals quite a bit. So much so that finding closed-form expressions
of the [quantile
function](https://dl.acm.org/doi/abs/10.1016/j.matcom.2009.02.002) or
the [moments of this
distribution](https://www.researchgate.net/publication/261641522_On_Order_Statistics_from_the_Gompertz-Makeham_Distribution_and_the_Lambert_W_Function)
is still an active field of research!

#### Gompertz from here on out

If a random variable $$X \sim \textrm{Gompertz}(\eta, b)$$ describes
the expected time of death of a newborn (or, less morbidly, the
expected time of failure for a newly built device), how does the world
look like at time $$t_0$$? That's an important question for,
e.g., retirement planning.

So let's compute the pdf after surviving until $$t_0$$:

$$\frac{f(t_0 + t)}{S(t_0)} = b\eta\frac{b\eta\exp\bigl(b(t_0+t) -
\eta(e^{b(t_0+t)} - 1)\bigr)}{\exp\bigl(-\eta(e^{bt} - 1)\bigr)}
= b\eta e^{bt_0}\exp\bigl(-\eta e^{bt_0}(e^{bt}-1) + bt\bigr).
$$

This is the pdf of $$\textrm{Gompertz}(\eta e^{bt_0}, b)$$. So the
future stays Gompertz-distributed with new parameters. This is a
useful property of the Gompertz distribution: truncated
renormalized versions of it stay within the family, in contrast to,
e.g., the Gaussian distribution.

This helps us answer questions like "How long will I spend in
retirement?", which is why Milevsky discusses Gompertz in his book
about retirement planning.

Before we can do that, let's discuss how one could fit the parameters
$$\eta$$ and $$b$$.

#### How to fit the data: Modal value of human life

The modal value(s) of a distribution is the maximum (or set of maxima)
of the pdf. In general, it is distinct from both the mean as well as the
median. In the case of Gompertz it's also an easy
computation:

$$
\frac{\d}{\d t}f(t) = 0
\ \Rightarrow\
b\eta\exp\bigl(bt - \eta(e^{bt} - 1)\bigr)(b - \eta b e^{bt}) = 0
\ \Rightarrow\
\eta e^{bt} = 1
$$

and therefore $$\eta = e^{-bt_m}$$ for the modal value $$t_m$$.

So once we have $$b$$ we can get $$\eta$$ from the data by looking for
the year (or month) with the most deaths.

The $$b$$ parameter we also get from the data as it determines the
year-on-year increase in the mortality rate: From the data above we
would estimate $$b=0.1$$. Milevsky suggests using $$1/b = 9.5$$ years
and calls this the _dispersion coefficient of human life_.

As the modal value of human life Milevsky suggests using $$t_m=87.25$$
for the general population in North America. Obviously $$t_m$$ was lower
in Gompertz's time; for a population of healthy females in a modern
society Milevsky suggests using up to $$t_m=90$$.


#### Plugging it all together

For a member of the general population in a developed country we can
take $$b = 1/9.5$$, $$t_m=87.25$$ and therefore $$\eta = e^{- bt_m} =
e^{-87.25 / 9.5} \approx 1.026\cdot 10^{-4}$$. If that person is
$$t_0\ge 0$$ years old, the Gompertz pdf for their future looks like

$$
b\eta e^{bt_0}\exp\bigl(-\eta e^{bt_0}(e^{bt}-1) + bt\bigr)
=
b e^{b(t_0 - t_m)} \exp\bigl(-e^{b(t_0 - t_m)}(e^{bt}-1) + bt\bigr)
$$

while the cdf is

$$
1 - \exp\bigl(- e^{b(t_0-t_m)} (e^{bt} - 1)\bigr).
$$

Therefore, the survival function conditioned on having lived until
year $$t_0$$ is

$$
p_{t_0}(t) := \exp\bigl(- e^{b(t_0-t_m)} (e^{bt} - 1)\bigr).
$$

This is also the chance of still being alive at year $$t_0 + t$$ given
being alive at year $$t_0$$ and constitutes an answer to the question
of "How long will I spend in retirement?", or more precisely "How
likely am I to be alive $$t$$ years into my retirement?". It's also
Milevsky's equation #2.

In a future blogpost, we will use this to compute values of
annuities. For now, let's wrap up with a quick discussion of how
realistic this model is.

### Is this model any good?

The first thing to say is that sadly, human babies are more likely to
die than the Gompertz distribution would indicate. That's partially a
sad fact of life and partially a consequence of the fact that severe
medical problems in unborn babies or during birth are less likely to
cause outright death at the point of delivery for the baby in
question, but may still cause death after a few days, months, or even
years.

On a potentially more positive note, the Gompertz distribution might
_overestimate_ the chance of dying next year for very old people. As
[Wikipedia has
it](https://en.wikipedia.org/wiki/Gompertz%E2%80%93Makeham_law_of_mortality):

> At more advanced ages, some studies have found that death rates
> increase more slowly -- a phenomenon known as the late-life mortality
> deceleration -- but more recent studies disagree.

Generally, there seems to be consensus that the Gompertz distribution
models mortality really well between the ages of 30 and 80.

A question very dear to "transhumanists" is to what
extent the gains in longevity seen in the last centuries can be
expected to continue to happen in the future. Obviously a simple
two-parameter model won't tell us a lot about that, and neither will
the three-parameter Gompertz-Makeham distribution. Still, I found it
interesting if a bit discouraging to read, again in
[Wikipedia](https://en.wikipedia.org/wiki/Gompertz%E2%80%93Makeham_law_of_mortality):

> The decline in the human mortality rate before the 1950s was mostly
> due to a decrease in the age-independent (Makeham) mortality
> component, while the age-dependent (Gompertz) mortality component
> was surprisingly stable. Since the 1950s, a new mortality
> trend has started in the form of an unexpected decline in mortality
> rates at advanced ages and "rectangularization" of the survival
> curve.

So apparently $$\eta$$ and $$b$$ have been stable over a long time
periods. Whatever that says about human longevity, it also says the
Gompertz (or the Gompertz-Makeham) model is not so bad.

That's it for today. My apologies for not actually having any $$\pi$$s in all of
this after all :)
