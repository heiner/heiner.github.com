---
layout: post
title:  "Annuity loans"
date:   2019-08-20 00:25:06 +0100
---

<small>Edit June 2023: Via
[Twitter](https://twitter.com/HeinrichKuttler/status/1673272830560022529?s=20),
I found that the same formula I arrive at here has been published in
P. Milanfar, "_A Persian Folk Method of Figuring Interest_", Mathematics
Magazine, vol. 69, no. 5, Dec. 1996 and apparently was known and used
"in the bazaar's of Iran (and elsewhere)". The mnemonics in [that
paper](https://www.maa.org/sites/default/files/Peyman_Milanfar45123.pdf)
are
$$
\textrm{Monthly payment}
=
\frac{1}{\textrm{Number of months}}(\textrm{Principal} + \textrm{Interest})
$$
where
$$
\textrm{Interest} = \tfrac{1}{2} \textrm{Principal} \cdot
\textrm{Number of years} \cdot \textrm{Annual interest rate}
$$.
</small>


I'm fond of small mental calculation helpers like the [rule of
72](https://en.wikipedia.org/wiki/Rule_of_72). Not that I am good at
mental math ([I once tried to fix that and got
sidetracked](https://play.google.com/store/apps/details?id=org.kuettler.mathapp)),
but I am good at spending time contemplating how I'd do it if I was
better at it.

Another thing I'm not good at is finance. Lack of capital usually
saves me from the worst mistakes, but despite the [brilliant advice
from Ben Felix](https://www.youtube.com/watch?v=Uwl3-jBNEd4), I sometimes
contemplate spending money on real estate. Real estate tends to be
financed with a morgage, which often is a type of annuity loan. What
is an annuity loan and is there a neat rule of thumb for it? Read on
to find out.

## What's an annuity loan?

We receive a loan of size $$S_0$$ and pay it back. Each period we'll
pay the same amount

$$R = T_k + Z_k$$

with a principal repayment $$T_k$$ and an interest payment $$Z_k$$ for
the $$k$$th payment out of $$n$$ total payments.

The interest payment is going to be a fixed percentage of the
outstanding principal balance and thus $$Z_1 = pS_0,$$ where we set
e.g. $$p=0.02$$ for a 2% interest rate.

## So we always pay the same amount. How much?

Let's consider an interest rate of $$p$$ and $$n$$ periods with one
payment per period. We note that the payment

$$R = T_1 + pS_0 = T_2 + p(S_0 - T_1),$$

since $$S_0 - T_1$$ is the outstanding balance after the first
payment. Hence $$T_2 = (1 + p)T_1$$. After $$k$$ and $$k+1$$ periods

$$ R = T_k + p\Bigl(S_0 - \sum_{j=1}^{k-1} T_j\Bigr)
 = T_{k+1} + p\Bigl(S_0 - \sum_{j=1}^k T_j\Bigr),$$

hence $$T_{k+1} = (1+p)T_k$$ and

$$T_k = (1 + p)^{k-1}T_1.$$

To impose another condition, let's say we want to fully pay back the
loan after $$n$$ periods, i.e.,

$$S_0 = \sum_{j=1}^{n} T_k = T_1 \sum_{j=1}^{n}(1+p)^{k-1} =
T_1\frac{(1+p)^n - 1}{p},$$

where, as so often, we made use of the sequence of partial sums
$$\sum_{k=0}^{n} q^k = \frac{q^{n+1}-1}{q-1}$$ of the geometric
series. Thus we find

$$R = T_1 + Z_1 = pS_0\frac{1}{(1+p)^n - 1} + pS_0
    = pS_0\frac{(1+p)^n}{(1+p)^n - 1}$$

The regular annuity payment $$R$$ is therefore a constant factor of
the loaned amount $$S_0$$, the _annuity factor_

$$\af(p, n) = p\frac{(1+p)^n}{(1+p)^n - 1}.$$

Not quite incidentelly, the annuity factor also shows up in formulas
for computing the equivalent annual cost from the net present
value. We won't go into that here.

Note that the condition to fully pay back $$S_0$$ does not in practice
constrain us very much -- if less is paid back, say $$S_1$$, we would
do the calculation with $$S_1$$ in place of $$S_0$$ and add a regular
interest payment of $$p(S_0 - S_1)$$.

## Months and years

Typically we'll make a monthly payment over many years. This is where
some treatments get confusing and also where banks make a bit of an
extra buck. For $$n$$ years and $$p$$ interest per year, for our
purposes we'll just take $$12n$$ periods and a monthly interest of
$$\sqrt[12]{1 + p} - 1 = \frac{p}{12} + O(p^2)$$. For small $$p$$,
e.g. not more than 10%, this is a good approximation. The monthly
payment is then

$$\frac{p}{12}\frac{(1 + p/12)^{12n}}{(1 + p/12)^{12n} - 1}S_0.$$

## Taylored for mental arithmetic

We started this looking for a simple approximation we can use for
mental arithmetic, like the rule of 72 (it takes $$72/x$$ periods for an
investment to double in value if it appreciates $$x$$% per
period). The above isn't that. The binomial theorem helps:

$$\Bigl(1 + \frac{p}{12}\Bigr)^{12n}
  = \sum_{k=0}^{12n} \binom{12n}{k} \Bigl(\frac{p}{12}\Bigr)^k
  = 1 + np + \binom{12n}{2}\Bigl(\frac{p}{12}\Bigr)^2 + O(p^3).$$

If we want to forget about the $$p^2$$ term as well we end up at

$$\af(p/12, 12n) \approx \frac{p}{12}\frac{1 + np}{np} = \frac{1 +
np}{12n},$$

which is nice. But not great. A short calculation with the binomial
coefficient $$\binom{12n}{2}$$ yields

$$\binom{12n}{2}\Bigl(\frac{p}{12}\Bigr)^2
  = \frac{(np)^2}{2} - \frac{np^2}{24}.$$

For typical $$n$$ and $$p$$ (e.g., $$n = 20$$ and $$p = 0.02$$) the
second term won't play any role. With the first term we improve our
approximation to

$$\af(p/12, 12n)
 \approx \frac{p}{12}\frac{1 + np + (np)^2/2}{np + (np)^2/2}
 = \frac{1}{12n}\frac{1 + np(1 + np/2)}{1 + np/2}
 = \frac{1}{12n}\Bigl(\frac{1}{1 + np/2} + np\Bigr).$$

Now, this is clearly unsuitable. But using the geometric series again
we see that $$\frac{1}{1 + np/2} = 1 - np/2 + (np/2)^2 + O(p^3)$$ and
hence

$$\af(p/12, 12n) \approx \frac{1 + \frac{np}{2}(1 +
\frac{np}{2})}{12n}.$$

This, too, is not too convienient. But if we drop the $$(np)^2$$ term
we end up with

$$\af(p/12, 12n) \approx \frac{1 + np/2}{12n}.$$

This isn't too bad. For slightly larger $$n$$ and $$p$$ we could also
have taken $$1 + \frac{np}{2} = 1.2$$, which would give us $$0.6$$
instead of $$1/2$$ in the above formula. Of course we can also do the
division by 12 and arrive at another formula.

Let's look at this from a slightly different perspective. A naive,
"interest-free" calculation on what the monthly payment for an $$n$$
year loan of $$S_0$$ is would be $$\frac{S_0}{12n}.$$

Our formula $$\af(p/12, 12n) \approx \frac{1 + np/2}{12n}$$ says: **Do
the naive thing, then add x% to the result, where x is "$$n$$ times
the interest rate over 2".**

## Example

A loan of $400000 with 2% interest over 20 years:

$$ \frac{\$400000}{12\cdot 20} \ \cdot\ \frac{20\cdot 2}{2}\%
  = \$1666 \ \cdot\ 20\% = \$333,$$

so the monthly rate will be $$\$1666 + \$333 = \$2000$$. This isn't
too far from the exact value of $$\af(\sqrt[12]{1.02} - 1, 12n) \cdot
\$400000 = \$2020$$.

## More numbers

The following table compares exact monthly rates as a percentage of
the total loan with our estimate, i.e., the true annuity factor
$$\af(\sqrt[12]{1 + p} - 1, 12n)$$ and our approximation
$$\frac{1 + np/2}{12n}$$ of it (**bold**).

{::options parse_block_html="true" /}

<div class="centered overflow">

|          |$$n = 2$$|$$n = 5$$|$$n = 7$$|$$n = 10$$|$$n = 15$$|$$n = 20$$|$$n = 25$$|$$n = 30$$|
|---------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|$$p = 0.5\%$$| $$4.19\%$$<br />$$\bf 4.19\%$$| $$1.69\%$$<br />$$\bf 1.69\%$$| $$1.21\%$$<br />$$\bf 1.21\%$$| $$0.85\%$$<br />$$\bf 0.85\%$$| $$0.58\%$$<br />$$\bf 0.58\%$$| $$0.44\%$$<br />$$\bf 0.44\%$$| $$0.35\%$$<br />$$\bf 0.35\%$$| $$0.30\%$$<br />$$\bf 0.30\%$$|
|$$p = 1.0\%$$| $$4.21\%$$<br />$$\bf 4.21\%$$| $$1.71\%$$<br />$$\bf 1.71\%$$| $$1.23\%$$<br />$$\bf 1.23\%$$| $$0.88\%$$<br />$$\bf 0.88\%$$| $$0.60\%$$<br />$$\bf 0.60\%$$| $$0.46\%$$<br />$$\bf 0.46\%$$| $$0.38\%$$<br />$$\bf 0.38\%$$| $$0.32\%$$<br />$$\bf 0.32\%$$|
|$$p = 1.5\%$$| $$4.23\%$$<br />$$\bf 4.23\%$$| $$1.73\%$$<br />$$\bf 1.73\%$$| $$1.25\%$$<br />$$\bf 1.25\%$$| $$0.90\%$$<br />$$\bf 0.90\%$$| $$0.62\%$$<br />$$\bf 0.62\%$$| $$0.48\%$$<br />$$\bf 0.48\%$$| $$0.40\%$$<br />$$\bf 0.40\%$$| $$0.34\%$$<br />$$\bf 0.34\%$$|
|$$p = 2.0\%$$| $$4.25\%$$<br />$$\bf 4.25\%$$| $$1.75\%$$<br />$$\bf 1.75\%$$| $$1.28\%$$<br />$$\bf 1.27\%$$| $$0.92\%$$<br />$$\bf 0.92\%$$| $$0.64\%$$<br />$$\bf 0.64\%$$| $$0.51\%$$<br />$$\bf 0.50\%$$| $$0.42\%$$<br />$$\bf 0.42\%$$| $$0.37\%$$<br />$$\bf 0.36\%$$|
|$$p = 3.0\%$$| $$4.30\%$$<br />$$\bf 4.29\%$$| $$1.80\%$$<br />$$\bf 1.79\%$$| $$1.32\%$$<br />$$\bf 1.32\%$$| $$0.96\%$$<br />$$\bf 0.96\%$$| $$0.69\%$$<br />$$\bf 0.68\%$$| $$0.55\%$$<br />$$\bf 0.54\%$$| $$0.47\%$$<br />$$\bf 0.46\%$$| $$0.42\%$$<br />$$\bf 0.40\%$$|
|$$p = 4.0\%$$| $$4.34\%$$<br />$$\bf 4.33\%$$| $$1.84\%$$<br />$$\bf 1.83\%$$| $$1.36\%$$<br />$$\bf 1.36\%$$| $$1.01\%$$<br />$$\bf 1.00\%$$| $$0.74\%$$<br />$$\bf 0.72\%$$| $$0.60\%$$<br />$$\bf 0.58\%$$| $$0.52\%$$<br />$$\bf 0.50\%$$| $$0.47\%$$<br />$$\bf 0.44\%$$|
|$$p = 5.0\%$$| $$4.38\%$$<br />$$\bf 4.38\%$$| $$1.88\%$$<br />$$\bf 1.88\%$$| $$1.41\%$$<br />$$\bf 1.40\%$$| $$1.06\%$$<br />$$\bf 1.04\%$$| $$0.79\%$$<br />$$\bf 0.76\%$$| $$0.65\%$$<br />$$\bf 0.62\%$$| $$0.58\%$$<br />$$\bf 0.54\%$$| $$0.53\%$$<br />$$\bf 0.49\%$$|
|$$p = 7.0\%$$| $$4.47\%$$<br />$$\bf 4.46\%$$| $$1.97\%$$<br />$$\bf 1.96\%$$| $$1.50\%$$<br />$$\bf 1.48\%$$| $$1.15\%$$<br />$$\bf 1.13\%$$| $$0.89\%$$<br />$$\bf 0.85\%$$| $$0.76\%$$<br />$$\bf 0.71\%$$| $$0.69\%$$<br />$$\bf 0.62\%$$| $$0.65\%$$<br />$$\bf 0.57\%$$|
|$$p = 10.0\%$$| $$4.59\%$$<br />$$\bf 4.58\%$$| $$2.10\%$$<br />$$\bf 2.08\%$$| $$1.64\%$$<br />$$\bf 1.61\%$$| $$1.30\%$$<br />$$\bf 1.25\%$$| $$1.05\%$$<br />$$\bf 0.97\%$$| $$0.94\%$$<br />$$\bf 0.83\%$$| $$0.88\%$$<br />$$\bf 0.75\%$$| $$0.85\%$$<br />$$\bf 0.69\%$$|
|$$p = 20.0\%$$| $$5.01\%$$<br />$$\bf 5.00\%$$| $$2.56\%$$<br />$$\bf 2.50\%$$| $$2.12\%$$<br />$$\bf 2.02\%$$| $$1.83\%$$<br />$$\bf 1.67\%$$| $$1.64\%$$<br />$$\bf 1.39\%$$| $$1.57\%$$<br />$$\bf 1.25\%$$| $$1.55\%$$<br />$$\bf 1.17\%$$| $$1.54\%$$<br />$$\bf 1.11\%$$|

</div>

{::options parse_block_html="false" /}


<div class="centered">
<img src="/img/afapprox.svg" alt="AF" style="width:70%;"/>
<br />
Our linear approximation \(\frac{1 + np/2}{12n}\), solid, and the true annuity factor
\(\af(\sqrt[12]{1 + p} - 1, 12n)\), dashed, for different number of years \(n\).
<a href="/img/afapprox.gp">Gnuplot source</a>
</div>

For low interests $$p$$ our approximation is rather good. For larger
interests over many years it starts underestimating the true
factor. In this regime using $$0.6$$ or higher in place of $$1/2$$
will yield better results.

This doesn't mean you should invest in real estate though.
