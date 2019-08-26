---
layout: post
title:  "Annuity loans"
date:   2019-08-20 00:25:06 +0100
---

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
$$\frac{1 + np/2}{12}$$ of it (**bold**).

|          |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 2$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 5$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 7$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 10$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 15$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 20$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 25$$|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$$n = 30$$|
|---------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|-------:|
|$$p =  0.5\%$$|$$4.188\%$$<br />$$\bf 4.188\%$$| $$1.688\%$$<br />$$\bf 1.688\%$$| $$1.212\%$$<br />$$\bf 1.211\%$$| $$0.854\%$$<br />$$\bf 0.854\%$$| $$0.577\%$$<br />$$\bf 0.576\%$$| $$0.438\%$$<br />$$\bf 0.438\%$$| $$0.355\%$$<br />$$\bf 0.354\%$$| $$0.299\%$$<br />$$\bf 0.299\%$$|
|$$p =  1.0\%$$|$$4.210\%$$<br />$$\bf 4.208\%$$| $$1.709\%$$<br />$$\bf 1.708\%$$| $$1.233\%$$<br />$$\bf 1.232\%$$| $$0.876\%$$<br />$$\bf 0.875\%$$| $$0.598\%$$<br />$$\bf 0.597\%$$| $$0.460\%$$<br />$$\bf 0.458\%$$| $$0.377\%$$<br />$$\bf 0.375\%$$| $$0.321\%$$<br />$$\bf 0.319\%$$|
|$$p =  1.5\%$$|$$4.232\%$$<br />$$\bf 4.229\%$$| $$1.731\%$$<br />$$\bf 1.729\%$$| $$1.254\%$$<br />$$\bf 1.253\%$$| $$0.897\%$$<br />$$\bf 0.896\%$$| $$0.620\%$$<br />$$\bf 0.618\%$$| $$0.482\%$$<br />$$\bf 0.479\%$$| $$0.399\%$$<br />$$\bf 0.396\%$$| $$0.345\%$$<br />$$\bf 0.340\%$$|
|$$p =  2.0\%$$|$$4.253\%$$<br />$$\bf 4.250\%$$| $$1.752\%$$<br />$$\bf 1.750\%$$| $$1.276\%$$<br />$$\bf 1.274\%$$| $$0.919\%$$<br />$$\bf 0.917\%$$| $$0.643\%$$<br />$$\bf 0.639\%$$| $$0.505\%$$<br />$$\bf 0.500\%$$| $$0.423\%$$<br />$$\bf 0.417\%$$| $$0.369\%$$<br />$$\bf 0.361\%$$|
|$$p =  3.0\%$$|$$4.296\%$$<br />$$\bf 4.292\%$$| $$1.795\%$$<br />$$\bf 1.792\%$$| $$1.320\%$$<br />$$\bf 1.315\%$$| $$0.964\%$$<br />$$\bf 0.958\%$$| $$0.689\%$$<br />$$\bf 0.681\%$$| $$0.553\%$$<br />$$\bf 0.542\%$$| $$0.472\%$$<br />$$\bf 0.458\%$$| $$0.419\%$$<br />$$\bf 0.403\%$$|
|$$p =  5.0\%$$|$$4.382\%$$<br />$$\bf 4.375\%$$| $$1.882\%$$<br />$$\bf 1.875\%$$| $$1.408\%$$<br />$$\bf 1.399\%$$| $$1.055\%$$<br />$$\bf 1.042\%$$| $$0.785\%$$<br />$$\bf 0.764\%$$| $$0.654\%$$<br />$$\bf 0.625\%$$| $$0.578\%$$<br />$$\bf 0.542\%$$| $$0.530\%$$<br />$$\bf 0.486\%$$|
|$$p =  7.0\%$$|$$4.468\%$$<br />$$\bf 4.458\%$$| $$1.970\%$$<br />$$\bf 1.958\%$$| $$1.499\%$$<br />$$\bf 1.482\%$$| $$1.150\%$$<br />$$\bf 1.125\%$$| $$0.887\%$$<br />$$\bf 0.847\%$$| $$0.762\%$$<br />$$\bf 0.708\%$$| $$0.693\%$$<br />$$\bf 0.625\%$$| $$0.651\%$$<br />$$\bf 0.569\%$$|
|$$p = 10.0\%$$|$$4.595\%$$<br />$$\bf 4.583\%$$| $$2.104\%$$<br />$$\bf 2.083\%$$| $$1.638\%$$<br />$$\bf 1.607\%$$| $$1.298\%$$<br />$$\bf 1.250\%$$| $$1.048\%$$<br />$$\bf 0.972\%$$| $$0.937\%$$<br />$$\bf 0.833\%$$| $$0.878\%$$<br />$$\bf 0.750\%$$| $$0.846\%$$<br />$$\bf 0.694\%$$|
|$$p = 20.0\%$$|$$5.010\%$$<br />$$\bf 5.000\%$$| $$2.560\%$$<br />$$\bf 2.500\%$$| $$2.124\%$$<br />$$\bf 2.024\%$$| $$1.826\%$$<br />$$\bf 1.667\%$$| $$1.637\%$$<br />$$\bf 1.389\%$$| $$1.572\%$$<br />$$\bf 1.250\%$$| $$1.547\%$$<br />$$\bf 1.167\%$$| $$1.537\%$$<br />$$\bf 1.111\%$$|

For low interests $$p$$ our approximation is rather good. For larger
interests over many years it starts underestimating the true
factor. In this regime using $$0.6$$ or higher in place of $$1/2$$
will yield better results.

This doesn't mean you should invest in real estate though.
