---
layout: post
title:  "More on linear regression: Capital asset pricing models"
---

This is the long-awaited second part of February's post on [Linear
Regression]({% post_url 2020-02-19-linear-regression %}). This time,
without the needlessly abstract math, but with some classic portfolio
theory as an example of "applied linear regression".

We'll be discussing two papers: [_The performance of mutual funds in
the period 1945-1964_ (1968) by Michael
Jensen](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1968.tb00815.x){:target="_blank"}
and [_Common Risk
Factors in the Returns On Stocks And Bonds_ (1993) by Eugene Fama
and Kenneth French](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.139.5892){:target="_blank"}.

Some disclaimers:

* I am by no means an expert on this topic. I learned about these
investing concepts on the [Rational Reminder
podcast](https://rationalreminder.ca){:target="_blank"} by the
excellent Benjamin Felix and Cameron Passmore.
* There's many more results on this, both classic and
recent. The two papers discussed here added some delta at the time,
but previous results by others were essential too, and get no
mention here. I chose these two papers because they are relatively easy to
follow and their main message can be explained well in a blog post.
* All of this is just for fun. Capital at risk.

## Jensen (1968): Standard stuff.

#### On models

The papers we discuss present _models_. Models have assumptions as
well as domains in which they are valid and domains in which they are
not. We are not going to make precise statements about either of
these, but it's useful to not confuse models with reality. 'Whereof one
has no model thereof one must be silent' (otherwise, _philosophus
mansisses_). This is also known as [searching under the
streetlights](https://en.wikipedia.org/wiki/Streetlight_effect){:target="_blank"}.

The _aim_ of our model will be to evaluate, or assess, the performance
of any given portfolio. Specifically, the model should evaluate
a portfolio manager's ability to increase returns by successfully
predicting future prices for a _given level of riskiness_. For
instance, if stock market returns are positive in expectation, a
leveraged portfolio could outperform an unleveraged portfolio without
any special forecasting ability on the manager's side. Conversely, a
classical [60/40 mix of stocks and
bonds](https://www.investopedia.com/articles/financial-advisors/011916/why-6040-portfolio-no-longer-good-enough.asp){:target="_blank"}
would likely do worse than a 100% equity portfolio in this case, but
may still be preferable due to its reduced risk. We won't go into
detail how risk is measured, but we should mention that under certain
assumptions, it is precisely its riskiness that causes a given asset
to yield a higher returns (_ceteris paribus_, and on average): If
investors are risk-averse, they will need to be compensated for
taking on the additional risk of a specific asset compared to some
other asset, and higher expected future returns (expected future
prices relative to its current price) are the way that
compensation happens in a liquid market. Of course, the actual
expectation of any given investor may also just be wrong, but over
time one may expect the worst investors to drop out, improving the
accuracy of the average investor's expectations.

#### Time series regressions

The specific models here do linear regression on time series. Suppose
we have one data point per time interval, e.g. per trading day:

| day             | |  value |
|:----------------|-|-------:|
| 5 January 1970  | |  388.8K|
| 6 January 1970  | |  475.2K|
|              |&#8942;|     |

We will use this data as an $$n$$-dimensional feature vector (aka explanatory
variable). Think of it as coming from the value of an index,
specifically from the capitalization-weighted value of the
whole stock market on that trading day. We will call this the _market
portfolio_.

The portfolio (or individual stock) we want to assess will also have a
value each trading day. This puts us in a situation in which we could
try to use linear regression to express our assessed portfolio as a
linear combination of the market value and a constant intercept
vector. However, little would be gained by just doing that -- we'll
have to at least normalize things a bit, otherwise this is what the
model will use its capacity (two numbers!) for. And while we are at
it, we remember that there used to be a time when the (almost, or by
definition) risk-free return offered by central banks was not
basically zero. To tease out the "risk factor", we will use the market
return minus this risk-free rate as our feature vector. Our data thus
could look like this:

| day             | |  market | risk-free |
|:----------------|-|--------:|----------:|
| 5 January 1970  | |  1.21%  | 0.029%    |
| 6 January 1970  | |  0.62%  | 0.029%    |
|              |&#8942;|      |

For the risk-free rate, one could use the 1 month treasury bill rate;
some care needs to be taken to properly get annualized numbers. All these
numbers can in principle be retrieved from the historical
records (and in practice downloaded from [Kenneth French's
homepage](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html){:target="_blank"}).

Let's call the market return $$R_M$$ and the risk-free return
$$R_F$$. A sensible regression without an intercept term could then
read as

$$R \approx R_F + \beta(R_M - R_F), \label{eq:1}\tag{1}$$

where $$R$$ is vector the observed returns of the portfolio or stock
we want to assess, and $$\beta$$ is computed via the least-squares
condition of linear regression, i.e., $$\beta = \argmin\{\abs{R - R_F -
\beta(R_M - R_F)}_2\st \beta\in\R\}$$, as in the [last blog post]({%
post_url 2020-02-19-linear-regression %}){:target="_blank"}. Notice that the $$R_F$$s
make sense here: It's deviations from this risk-free return that we
want to model, and we want $$\beta$$ to scale the non risk-free
portion of the market portfolio.

**Example.**&nbsp; For a classic 60/40
portfolio with 60% whole market and 40% risk free return (historically
not realistic for private investors, but easy to compute) we have

$$R - R_F= 0.6R_M + 0.4R_F - R_F = 0.6(R_M - R_F)\in\R^{n\times 1}$$

and therefore, by the [normal equation]({% post_url 2020-02-19-linear-regression %}){:target="_blank"}),

$$\beta = \bigl((R_M - R_F)^\top (R_M - R_F)\bigr)^{-1}
          (R_M - R_F)^\top (R - R_F) = 0.6.$$

That seems sensible in this case.

#### Finding Alpha

However, \eqref{eq:1} isn't quite good enough: More precisely, it
reads

$$ R = R_F + \beta(R_M - R_F) + e, \label{eq:2}\tag{2} $$

with an error term $$e\in\R^n$$. As Jensen (1968) argues,

> [W]e must be very careful when applying the equation to managed portfolios. If the manager is a superior forecaster (perhaps because of
special knowledge not available to others) he will tend to systematically select
securities which realize [$$e_j > 0$$].

This touches on a subject glossed over in the last blog post: Most
statements about linear regression models depend on certain
statistical assumptions, among them that
the error terms are elementwise iid, ideally with a mean of zero. There's
autocorrelation tests like
[Durbin-Watson](https://en.wikipedia.org/wiki/Durbin%E2%80%93Watson_statistic){:target="_blank"}
to test if this is true for a particular dataset. In this
particular modeling exercise, we can do better by
adding the constant $$\1=(1,\ldots,1)\in\R^n$$ intercept vector to the
subspace we project on, which turns \eqref{eq:2} into

$$
R - R_F = \alpha + \beta(R_M - R_F) + u, \label{eq:3}\tag{3}
$$

with an error term $$u\in\R^n$$.

_Ever wondered where the
"[alpha](https://en.wikipedia.org/wiki/Alpha_(finance)){:target="_blank"}" in the
clickbait website [Seeking Alpha](https://seekingalpha.com/){:target="_blank"} comes
from?_ It is this $$\alpha$$, the coefficient of the
$$\1$$ intercept vector in \eqref{eq:3}. To quote
Jensen (1968) again:

> Thus if the portfolio manager has an ability to forecast security prices, the
intercept, [$$\alpha$$, in eq. \eqref{eq:3}] will be positive. Indeed,
it represents the average incremental rate of return on the portfolio
per unit time which is due solely to
the manager's ability to forecast future security prices. It is
interesting to
note that a naive random selection buy and hold policy can be expected to
yield a zero intercept. In addition if the manager is not doing as
well as a
random selection buy and hold policy, [$$\alpha$$] will be
negative. At first glance it
might seem difficult to do worse than a random selection policy, but such
results may very well be due to the generation of too many expenses in unsuccessful forecasting attempts.
>
> However, given that we observe a positive intercept in any sample of returns on a portfolio we have the difficulty of judging whether or not this
observation was due to mere random chance or to the superior forecasting
ability of the portfolio manager. [...]
>
> It should be emphasized that in estimating [$$\alpha$$], the measure
of performance,
we are explicitly allowing for the effects of risk on return as implied by the
asset pricing model. Moreover, it should also be noted that if the model is
valid, the particular nature of general economic conditions or the particular
market conditions (the behavior of $$\pi$$) over the sample or evaluation period
has no effect whatsoever on the measure of performance. Thus our measure
of performance can be legitimately compared across funds of different risk
levels and across different time periods irrespective of general economic and
market condition.

About the error term $$u$$, first notice that thanks to the intercept
term we can expect it to have a mean of zero. Further, Jensen (1968)
argues it "should be serially [i.e., elementwise] independent" as
otherwise "the manager could increase his return even more by
taking account of the information contained in the serial dependence
and would therefore eliminate it."


### Just show me the code!

After introducing this model, Jensen (1968) continues with "the data
and empirical results". In ca. 2015 AI parlance, this part could be
called "Experiments". Take a look at Table 1 in the paper to get a
list of quaint mutual fund names. Notice too that it's not immediately
obvious how to get the market portfolio's returns from historical
trading data, as companies enter and leave the stock market, and how
they leave will play a huge role. (Bankruptcy? Taken private at
$420?)

For our purposes though, all of this has been taken care of and
[Kenneth French's
homepage](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html){:target="_blank"})
has the data, including data for each trading day, in usable
formats.

Let's start by getting the data and sanity-checking our 60/40 example
above. All of the code in this post can also be [downloaded
separately](/src/ff3f.py) or
run in a [Google Colab](https://colab.research.google.com/drive/1iqpYDgpElizyAWW-6xXHMTpatw0Hqm1c?usp=sharing){:target="_blank"}.

```python
import os
import re
import urllib.request
import zipfile

import numpy as np

FF3F = (  # Monthly data.
    "https://mba.tuck.dartmouth.edu/pages/faculty/"
    "ken.french/ftp/F-F_Research_Data_Factors_TXT.zip"
)


def download(url=FF3F):
    archive = os.path.basename(url)
    if not os.path.exists(archive):
        print("Retrieving", url)
        urllib.request.urlretrieve(url, archive)
    return archive


def extract(archive, match=re.compile(rb"\d" * 6)):
    with zipfile.ZipFile(archive) as z:
        name, *rest = z.namelist()
        assert not rest
        with z.open(name) as f:
            # Filter for the actual data lines in the file.
            return np.loadtxt((line for line in f if match.match(line)), unpack=True)


date, mktmrf, _, _, rf = extract(download())

mkt = mktmrf + rf

# Linear regression using the normal equation.
A = np.stack([np.ones_like(mktmrf), mktmrf], axis=1)
alpha, beta = np.linalg.inv(A.T @ A) @ A.T @ (0.6 * mkt + 0.4 * rf - rf)

print("alpha=%f; beta=%f" % (alpha, beta))
```

As expected, this prints
```
alpha=0.000000; beta=0.600000
```

If we are seeking $$\alpha$$, we'll have to look elsewhere.

Let's try some real data. The biggest issue is getting hold of
the daily returns of real portfolios. Real researchers use data
sources like the [Center for Research in Security Prices
(CRSP)](http://www.crsp.org/){:target="_blank"}, but their data isn't available for
free. Instead, let's the data for iShares S&P Small-Cap 600 Value ETF
(IJS) from [Yahoo
finance](https://finance.yahoo.com/quote/IJS/history?period1=964742400&period2=1599350400&interval=1mo&filter=history&frequency=1mo){:target="_blank"}.

```python
# Continuing from above.

import time

IJS = (
    "https://gist.githubusercontent.com/heiner/b222d0985cbebfdfc77288404e6b2735/"
    "raw/08c1cacecbcfcd9e30ce28ee6d3fe3d96c07115c/IJS.csv"
)


def extract_csv(archive):
    with open(archive) as f:
        return np.loadtxt(
            f,
            delimiter=",",
            skiprows=1,  # Header.
            converters={  # Hacky date handling.
                0: lambda s: time.strftime(
                    "%Y%m", time.strptime(s.decode("ascii"), "%Y-%m-%d")
                )
            },
        )


ijs_data = extract_csv(download(IJS))

ijs = ijs_data[:, 5]  # Adj Close (includes dividends).

# Turn into monthly percentage returns.
ijs = 100 * (ijs[1:] / ijs[:-1] - 1)
ijs_date = ijs_data[1:, 0]

ijs_date, indices, ijs_indices = np.intersect1d(date, ijs_date, return_indices=True)

# Regression model for CAPM.
A = np.stack([np.ones_like(ijs_date), mktmrf[indices]], axis=1)
y = ijs[ijs_indices] - rf[indices]
B = np.linalg.inv(A.T @ A) @ A.T @ y
alpha, beta = B

# R^2 and adjusted R^2.
model_err = A @ B - y
ss_err = model_err.T @ model_err
r2 = 1 - ss_err.item() / np.var(y, ddof=len(y) - 1)
adjr2 = 1 - ss_err.item() / (A.shape[0] - A.shape[1]) / np.var(y, ddof=1)

print(
    "CAPM: alpha=%.2f%%; beta=%.2f. R^2=%.1f%%; R_adj^2=%.1f%%. Annualized alpha: %.2f%%"
    % (
        alpha,
        beta,
        100 * r2,
        100 * adjr2,
        ((1 + alpha / 100) ** 12 - 1) * 100,
    )
)
```

This prints:
```
CAPM: alpha=0.13%; beta=1.14. R^2=77.8%; R_adj^2=77.7%. Annualized alpha: 1.58%
```

Since $$\alpha$$ is the weight for the constant intercept vector $$\1
= (1,\ldots,1)$$, we can think of it as having percentage points as
its unit. Note that fees are not included in this calculation.
However, as for many ETFs fees for IJS are low, currently at 0.25%
per year. (Managed mutual funds will typically have an
annual fee of at least 1%, historically often more than that.)

It seems bit strange that this ETF tracking the  S&P Small-Cap 600
Value index has significant $$\alpha$$: Presumably, the index just
includes firms based on simple rules, not genius insights by some
above-average fund manager. Looking at the $$R^2$$ value, we "explain"
only 77% of the variance of the returns of IJS (the usual caveats
to the wording "explain" apply).

Clearly more research was needed. Or just a larger subspace for the
linear regression to project onto?

## Fama & French (1993): More factors.

During the 1980s at the latest, research
into financial economics noticed that certain segments of the market
outperformed other sections, and thus the market as a whole, on
average. There are several possible explanations for this effect with
different implications for the future. For example: Are these segments
of the market just inherently riskier such that rational traders
demand higher expected returns via sufficiently low prices for these
stocks? Or were traders
just irrationally disinterested in some 'unsexy' firms and have
perhaps caught on by now (or not, hence TSLA)? The latter is the
behavioural explanation, while the former relates tends to be put
forth by proponents of the [Efficient-market hypothesis
(EMH)](https://en.wikipedia.org/wiki/Efficient-market_hypothesis){:target="_blank"},
which includes
[Jensen](https://en.wikipedia.org/wiki/The_Superinvestors_of_Graham-and-Doddsville){:target="_blank"}
as well as Fama and French.
We won't be getting into this now. Let's instead take
a look at which 'easily' identifiable subsections of the market have
historically outperformed.

Citing previous literature, Fama & French (1993) mention _size_
(market capitalization, i.e., price per stock times number of shares),
_earnings per price_ and _book-to-market_ (book value divided by
market value) as variables that appear to have "explanatory power",
which I take to mean that some model that includes these variables has
nonzero regression coefficients and a relatively large $$R^2$$ or other
appropriate statistics.

The specific way in which Fama & French (1993) introduce these variables into
the model is through the construction of portfolios that mimic these
variables. This approach contributed to their being awarded the
Nobel (Memorial) Prize in Economic Sciences in 2013. The specific
construction goes as follows:

Take all stocks in the overall market and order them their size
(i.e., market capitalization). Then take the top and bottom halves and
call them "_big_" (_B_) and "_small_" (_S_), respectively.

Next, again take all stocks in the overall market and order them by
book-to-market equity. Then take the bottom 30% ("_low_", _L_), the middle 40%
("_medium_", _M_) and the top 30$ ("_high_", _H_). In both cases, some care
needs to be taken: E.g., how to handle firms dropping in and out of the
market, how to define book equity properly in the presence of deferred
taxes, and other effects.

Then, construct the six portfolios containing stocks in the
intersections of the two size and the three book-to-market equity
groups, e.g.

|          | low   | medium | high  |
|---------:|:-----:|:------:|:-----:|
|**small** | _S/L_ | _S/M_  | _S/H_ |
|**big**   | _B/L_ | _B/M_  | _B/H_ |

Out of these six building blocks, Fama & French build a _size_ and a
_book-to-market equity_ portfolio:

* The _size_ portfolio is "small minus
  big" (_SMB_) consisting of the monthly difference of the three
  small-stock portfolios _S/L_, _S/M_, and _S/H_ to the three big-stock
  portfolios _B/L_, _B/M_, and _B/H_.

* The _book-to-market equity_ portfolio is "high minus low" (_HML_),
  the monthly difference of the two high book-to-market
  portfolios _S/H_ and _B/H_ to the two low book-to-market
  portfolios _S/L_ and _B/L_. This is also known as the _value_
  factor.

Additionally, the authors also use the _market portfolio_ as "market
return minus risk free return (one-month treasury bill rate)" in the
same way as Jensen (1968).

#### An aside

I'm not sure why _SMB_ and _HML_ need the to have their
two terms be equally weighted among the splits of the other
ordering. The authors mention

> [For _HML_] the difference between the two returns should be largely free of
the size factor in returns, focusing instead on the different return
behaviors of high- and low-[book-to-market] firms. As testimony to the
success of this simple procedure, the correlation between the
1963--1991 monthly mimicking returns for the size and
book-to-market factors is only $$- 0.08$$.

Taking "correlation" to mean the Pearson correlation coefficient, we
can test this using the data from French's homepage:

```python
date, mktmrf, smb, hml, rf = extract(download())
print(np.corrcoef(smb, hml))
```

This prints

```
[[1.         0.12889074]
 [0.12889074 1.        ]]
```

which implies a coefficient of $$0.13$$. In 1993, Fama and French had
less data available: The paper uses the 342 months from July 1963 to
December 1991. Let's check with this range:

```python
orig_indices = (196307 <= date) & (date <= 199112)
assert len(smb[orig_indices]) == 342
print(np.corrcoef(smb[orig_indices], hml[orig_indices]))
```

This yields

```
[[ 1.         -0.09669641]
 [-0.09669641  1.        ]]
```

a coefficient of roughly $$-0.10$$, not the $$-0.08$$ the authors
mention, but relatively close. I guess the data has been cleaned a bit
since 1993?

As a further aside, accumulating this data and analyzing it was a true
feat in 1993. These days, we can do the same using the internet and
a few lines of Python (or, spoiler alert, using just a
[website](https://www.portfoliovisualizer.com/)){:target="_blank"}.

#### Back to modelling

So what are we to do with _SMB_ and _HML_? You guessed it -- just add
them to the regression model. Of course, this makes the subspace we
project on larger, which will always decrease the "fraction of
variance unexplained", without necessarily explaining much. However,
in the case of IJS it appears to explain a bit:

```python
# Continuing from above.
A = np.stack(
    [np.ones_like(ijs_date), mktmrf[indices], smb[indices], hml[indices]], axis=1
)
y = ijs[ijs_indices] - rf[indices]
B = np.linalg.inv(A.T @ A) @ A.T @ y
alpha, beta_mkt, beta_smb, beta_hml = B

model_err = A @ B - y
ss_err = model_err.T @ model_err
r2 = 1 - ss_err.item() / np.var(y, ddof=len(y) - 1)
adjr2 = 1 - ss_err.item() / (A.shape[0] - A.shape[1]) / np.var(y, ddof=1)

print(
    "FF3F: alpha=%.2f%%; beta_mkt=%.2f; beta_smb=%.2f; beta_hml=%.2f."
    " R^2=%.1f%%; R_adj^2=%.1f%%. Annualized alpha: %.2f%%"
    % (
        alpha,
        beta_mkt,
        beta_smb,
        beta_hml,
        100 * r2,
        100 * adjr2,
        ((1 + alpha / 100) ** 12 - 1) * 100,
    )
)
```

This prints:

```
FF3F: alpha=0.04%; beta_mkt=0.97; beta_smb=0.79; beta_hml=0.51. R^2=95.8%; R_adj^2=95.8%. Annualized alpha: 0.43%
```

In other words, we dropped from an (annualized) $$\alpha_{\rm CAPM} = 1.58\%$$ to
only $$\alpha_{\rm FF3F} = 0.43\%$$. The explained fraction of
variance has increased to above 95%.

Remembering that Jensen (1968) talked about assessing fund managers
with this model, we could try the same with actual managed
funds. While I couldn't produce any impressive results there, French
and Fama did go into the question of [_Luck versus Skill in the
Cross-Section of Mutual Fund
Returns_](http://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S8C-FamaFrench-LuckvSkill-JF10.pdf){:target="_blank"}
in a 2010 paper. The results, on average, don't look good for fund
managers' skill. The story for individual fund managers may be better,
but don't hold your breath.

### Was this worth it?

We discussed academic outputs of Jensen, French and Fama. The latter
two even got a Nobel for
their work on factor models. But nowadays, we can do (parts) of their
computations in a few lines of Python.

It's actually easier than that still. The website
portfoliovisualizer.com allows us to do [all
of](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&symbols=IJS&sharedTimePeriod=true&factorDataSet=0&marketArea=0&factorModel=1&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&__checkbox_ffmkt=true&__checkbox_ffsmb=true&__checkbox_ffsmb5=true&__checkbox_ffhml=true&__checkbox_ffmom=true&__checkbox_ffrmw=true&__checkbox_ffcma=true&__checkbox_ffstrev=true&__checkbox_ffltrev=true&__checkbox_aqrmkt=true&__checkbox_aqrsmb=true&__checkbox_aqrhml=true&__checkbox_aqrhmldev=true&__checkbox_aqrmom=true&__checkbox_aqrqmj=true&__checkbox_aqrbab=true&__checkbox_aamkt=true&__checkbox_aasmb=true&__checkbox_aahml=true&__checkbox_aamom=true&__checkbox_aaqmj=true&__checkbox_qmkt=true&__checkbox_qme=true&__checkbox_qia=true&__checkbox_qroe=true&__checkbox_qeg=true&__checkbox_trm=true&__checkbox_cdt=true&timePeriod=2&rollPeriod=12&marketAssetType=1&robustRegression=false){:target="_blank"}
[these
computations](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&symbols=IJS&sharedTimePeriod=true&factorDataSet=0&marketArea=0&factorModel=3&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&__checkbox_ffmkt=true&__checkbox_ffsmb=true&__checkbox_ffsmb5=true&__checkbox_ffhml=true&__checkbox_ffmom=true&__checkbox_ffrmw=true&__checkbox_ffcma=true&__checkbox_ffstrev=true&__checkbox_ffltrev=true&__checkbox_aqrmkt=true&__checkbox_aqrsmb=true&__checkbox_aqrhml=true&__checkbox_aqrhmldev=true&__checkbox_aqrmom=true&__checkbox_aqrqmj=true&__checkbox_aqrbab=true&__checkbox_aamkt=true&__checkbox_aasmb=true&__checkbox_aahml=true&__checkbox_aamom=true&__checkbox_aaqmj=true&__checkbox_qmkt=true&__checkbox_qme=true&__checkbox_qia=true&__checkbox_qroe=true&__checkbox_qeg=true&__checkbox_trm=true&__checkbox_cdt=true&timePeriod=2&rollPeriod=12&marketAssetType=1&robustRegression=false){:target="_blank"}
and more with a few clicks. In that sense, this blog post was perhaps
not worth it.

Another question is how useful these models are. This touches on _why_
_SMB_ and _HML_ 'explain' returns of portfolios (e.g., the risk
explanation vs the behavioural explanation mentioned above, or perhaps
both or neither). In
2014, Fama and French presented another updated model with five
factors, adding _profitability_ and _investment_; judged by $$R^2$$,
this five-factor model 'explains' even more of the variance of example
portfolios. Other research
suggesting alternative factors abounds.

How well do these models
really 'explain' the phenomenal historical returns of star investors
like Warren Buffett? Given that Buffett is a proponent of the [Benjamin
Graham](https://en.wikipedia.org/wiki/Benjamin_Graham){:target="_blank"} school of
_value investing_, including a value factor like _HML_ could perhaps
be the key to explain his success?
For the Fama & French five-factor model, we can
check
[portfoliovisualizer.com](https://www.portfoliovisualizer.com/factor-analysis?s=y&regressionType=1&symbols=BRK.A&sharedTimePeriod=true&factorDataSet=0&marketArea=0&factorModel=5&useHMLDevFactor=false&includeQualityFactor=false&includeLowBetaFactor=false&fixedIncomeFactorModel=0&__checkbox_ffmkt=true&__checkbox_ffsmb=true&__checkbox_ffsmb5=true&__checkbox_ffhml=true&__checkbox_ffmom=true&__checkbox_ffrmw=true&__checkbox_ffcma=true&__checkbox_ffstrev=true&__checkbox_ffltrev=true&__checkbox_aqrmkt=true&__checkbox_aqrsmb=true&__checkbox_aqrhml=true&__checkbox_aqrhmldev=true&__checkbox_aqrmom=true&__checkbox_aqrqmj=true&__checkbox_aqrbab=true&__checkbox_aamkt=true&__checkbox_aasmb=true&__checkbox_aahml=true&__checkbox_aamom=true&__checkbox_aaqmj=true&__checkbox_qmkt=true&__checkbox_qme=true&__checkbox_qia=true&__checkbox_qroe=true&__checkbox_qeg=true&__checkbox_trm=true&__checkbox_cdt=true&timePeriod=2&rollPeriod=12&marketAssetType=1&robustRegression=false){:target="_blank"}:
With $$R^2 \approx 33\%$$, and an annualized $$\alpha$$ of 4.87%, the results
don't look too good for the math nerds but very good for the 'Oracle
of Omaha'.

This is obviously not a new observation. There is even a paper by a
number of people from investment firm AQR about [_Buffett's
Alpha_](https://www.tandfonline.com/doi/full/10.2469/faj.v74.n4.3){:target="_blank"}
that aims to explain Buffett's successes with leveraging as well as
yet another set of new factors in a linear regression model:

> [Buffett's] alpha became insignificant, however, when we controlled
  for exposure to the factors “betting against beta” and “quality
  minus junk.”

Nice as this may sound, it would appear more convincing to this author
if the financial analysis community could converge on a small common
set of factors instead of seemingly creating them _ad hoc_. Otherwise,
von&nbsp;Neumann's line comes to mind: "With four parameters I can fit an
elephant, and with five I can make him wiggle his trunk."

### And now what?

We discussed two financial economics papers and the linear regression
models they propose, merely to give us a sense of what's done in this
field. One may get a sense that this research should be useful for
more than just amusement, perhaps it could even inform our investment
choices? Many good [financial
advisors](https://www.youtube.com/watch?v=ViTnIebSzj4){:target="_blank"} will make use
of data analyses
like this and suggest _factor-tilted_ portfolios. However, value
investing, both with factors as well as the Buffett/Munger variety,
has trailed the overall market in the last 10--15
years. Statistically, this is to be expected to happen every now and
then, so we cannot read too much into that. But it's _possible_ the
market has just caught on, past performance is not indicative of
future results and value investing should be cancelled in 2020.
That would at least match the _zeitgeist_. However, it's also
entirely possible it's exactly times like the present that make value
investing hard but ultimately worthwhile and we should be greedy when
others are fearful.

Time will tell.


#### References
* Frazzini, Andrea & Kabiller, David & Pedersen, Lasse Heje.
[_Buffett's Alpha_](https://www.tandfonline.com/doi/full/10.2469/faj.v74.n4.3){:target="_blank"}.
Financ. Anal. J. 74 (4), 35--55
<span class="smallcaps">[DOI:10.2469/faj.v74.n4.3](https://doi.org/10.2469/faj.v74.n4.3){:target="_blank"}</span>.
* Fama, Eugene F. & French, Kenneth R.
[_Common risk factors in the returns on stocks and bonds_](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.139.5892){:target="_blank"}.
J. Financ. Econ. 33, (1), 3--56 (1993).
<span class="smallcaps">[DOI:10.1016/0304-405X(93)90023-5](https://doi.org/10.1016/0304-405X(93)90023-5){:target="_blank"}</span>.
* &mdash;&mdash;&mdash;.
[_Luck versus skill in the cross‐section of mutual fund
returns_](http://mba.tuck.dartmouth.edu/bespeneckbo/default/AFA611-Eckbo%20web%20site/AFA611-S8C-FamaFrench-LuckvSkill-JF10.pdf){:target="_blank"}.
J. Financ. 65 (5), 1915--1947 (2010).
<span class="smallcaps">[DOI:10.1111/j.1540-6261.2010.01598.x](https://doi.org/10.1111/j.1540-6261.2010.01598.x){:target="_blank"}</span>.
* &mdash;&mdash;&mdash;.
[_A five-factor asset pricing model_](https://tevgeniou.github.io/EquityRiskFactors/bibliography/FiveFactor.pdf){:target="_blank"}.
J. Financ. Econ. 116 (1), 1--22 (2015).
<span class="smallcaps">[DOI:10.1016/j.jfineco.2014.10.010](https://doi.org/10.1016/j.jfineco.2014.10.010){:target="_blank"}</span>.
* Jensen, Michael C.
[_The performance of mutual funds in the period 1945--1964_](https://onlinelibrary.wiley.com/doi/full/10.1111/j.1540-6261.1968.tb00815.x){:target="_blank"}.
J. Financ. 23 (2), 389--416 (1968).
<span class="smallcaps">[DOI:10.1111/j.1540-6261.1968.tb00815.x](https://doi.org/10.1111/j.1540-6261.1968.tb00815.x){:target="_blank"}</span>.
{: refdef .simplelist}
