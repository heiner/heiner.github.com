---
layout: post
title:  "πs, deaths, and statistics"
---

This is part 1 of a 2 part series on Gompertz law.

After enjoying a [podcast interviewing Moshe
Milevsky](https://rationalreminder.ca/podcast/122), I got interested
in his work and read his book _The 7 Most Important Equations for Your
Retirement_.

It's a bit of a weird book. I can't say I didn't enjoy it. But it
gave me the impression Moshe Milevsky didn't expect his readers to enjoy the
book, or at least he didn't seem to expect them to like the formulas. That
seems like a weird proposition given a book with "equations" in its
very title. Perhaps the readers were imagined to be part of the
captured audience of students who are asked to read the book as an
assignment? At any rate the author apologizes every time he actually
discusses formulae, and having to resort to _logarithms_ seems to make
him positively embarrassed.

Then again, Prof. Milevsky wrote many books and this is apparently one
of his bestsellers. And
the anecdotes of Fibonacci, Gompertz, Halley, Fisher, Huebner, and
Kolmogorov[^1] in the book sure are lovely, as are the author's personal
experience with economist Paul Samuelson. Perhaps the professor just
knows his audience.

[^1]: For Kolmogorov, I'd love to have another reference for his
      supposed _War and Peace_-inspired nickname "ANK". The book in question
      is the only reference I could find.

But so do I, being well acquainted with the empty set. So there's no
issue with too much math on this blog.

And with that, let's discuss Moshe's equation #2: The Gompertz
distribution.

### Gompertz's discovery

<center>
<img src="/img/Gompertz.png" alt="Benjamin Gompertz"
style="width:200px;"/><br />
Image source: <a href="https://en.wikipedia.org/wiki/Benjamin_Gompertz#/media/File:Gompertz.png">Wikipedia</a>
</center>


Benjamin Gompertz (1779--1865) was a British mathematician and actuary
of German Jewish descent. According to Milevsky, Gompertz was looking
for a law of human mortality, comparable to Newton's laws of
mechanics. At his time, statistics of people's lifespan were already
available and formed the basis for Gompertz's discovery. For instance,
one could compile a _mortality table_ of a (hypothetical) group of
45-year-olds as they age. The data might look like this:


Age&nbsp;|Alive at Birthday&nbsp;|Die in Year
-|-|-
45|	98,585|	146
46|	98,439|	161
47|	98,278|	177
48|	98,101|	195
49|	97,906|	214
50|	97,692|	236
51|	97,456|	259
52|	97,197|	285
53|	96,912|	313
54|	96,599|	345

What does this tell us? It doesn't immediately tell me anything not
very obvious: The older one gets, the more likely one dies soon. Let's
compute the _mortality rate_: How likely were people to die at a given
age in this cohort? To be precise, we compute "_Which proportion of
people alive at age $$t$$ died before age $$t+1$$?"_

Age&nbsp;|Alive at Birthday&nbsp;|Die in Year&nbsp;| Mortality Rate
-|-|-|-
45 | 98,585 | 146 | 0.148%
46 | 98,439 | 161 | 0.164%
47 | 98,278 | 177 | 0.180%
48 | 98,101 | 195 | 0.199%
49 | 97,906 | 214 | 0.219%
50 | 97,692 | 236 | 0.242%
51 | 97,456 | 259 | 0.266%
52 | 97,197 | 285 | 0.293%
53 | 96,912 | 313 | 0.323%
54 | 96,599 | 345 | 0.357%

So again, so much so obvious: The probability of dying the next year
increases with age. But _how much_ does it increase? This is
Gompertz's discovery, now called Gompertz's law: The mortality rate
appears to increase exponentially. One way of seeing this is to take
logs and compute their difference:

Age&nbsp;|Alive at Birthday&nbsp;|Die in Year&nbsp;| Mortality Rate&nbsp;|Log of Mortality Rate|Difference in Log values
-|-|-|-|-
45 | 98,585 | 146 | 0.148% | -6.515 | --
46 | 98,439 | 161 | 0.164% | -6.416 | 0.0993
47 | 98,278 | 177 | 0.180% | -6.319 | 0.0964
48 | 98,101 | 195 | 0.199% | -6.221 | 0.0987
49 | 97,906 | 214 | 0.219% | -6.126 | 0.0950
50 | 97,692 | 236 | 0.242% | -6.026 | 0.1000
51 | 97,456 | 259 | 0.266% | -5.930 | 0.0954
52 | 97,197 | 285 | 0.293% | -5.832 | 0.0983
53 | 96,912 | 313 | 0.323% | -5.735 | 0.0967
54 | 96,599 | 345 | 0.357% | -5.635 | 0.1006

The difference in log values increases by about 0.1