---
layout: post
title:  "Leetcode-style interviews and my favorite question"
---

* Table of contents
{:toc}

## A Leetcode-style interviewer's apology

People love to hate leetcode-style interviews. On X, they are
regularly described as a waste of time for all parties
involved. People point out that real programming jobs are nothing like
these artificial 30-60 minute situations, that software engineers can
have decade-long careers without ever implementing the algorithms that
are regularly discussed during these interviews, and that AI means
encyclopedic knowledge of algorithms is even more useless than it
was before.[^failure]

[^failure]: Another reason some people dislike leetcode-style
    questions is that they experienced them and did not end up getting
    an offer. That happened to me too -- when I first applied to Google
    in Munich after my math PhD, I was woefully underprepared and no
    match for the L4 coding interviews (which were on the tough end,
    one of them was asking to implement a parallel regex matching
    engine). Leetcode-style questions certainly are not perfect and
    end up having false negatives. However, precision is _much more_
    important when hiring than recall is. That is true even though
    getting rejected for a position one would have excelled in is sad.

Some of that is true. And yet, the critics of leetcode-style
interviews are mistaken. When faced with the _practical_ question of
assessing within minutes whether a given candidate would be a useful
co-worker, leetcode-style questions are hard to beat.

Why is that? I don't think there is a single mechanism.
It's easy to criticize leetcode-style questions since they assess a
combination of skills and desiderata but don't nail any single
one. Let's therefore describe what leetcode-interviews _do_ assess and
why that's a good thing. To make matters more concrete, I'll then
describe one of my favorite leetcode-style interview questions in detail.

**Leetcode-style questions test if you can code.** It's stupid, but a
good fraction of candidates will [fail even
FizzBuzz](https://blog.codinghorror.com/why-cant-programmers-program/). They
just cannot code. _Any_ interview that involves coding will find that;
having a rule that says a specific interview is for coding exclusively
helps get to fast failure for hopeless cases.

**Leetcode-style questions can be prepared for.** That is the
very business model of [leetcode.com](https://leetcode.com). Becoming
good at these kinds of questions takes a lot of work. Combined with the
supposed uselessness of the skill thereby acquired, this is used as an
argument against them. But not so: One of the practical questions an
interviewer has to answer is just how excited a given candidate is
about the job, and about the occupation of programming for a living in
the first place. Putting in weeks, or months, of prep time is a strong
signal that the candidate is _interested in software_. That is a lot!
In fact, the best programmers I know are _excited_ to discuss new
little questions, not too different from how mathematicians discuss
little exercises. Being interested in how to find unique triplets of
array entries that sum to zero correlates with just being interested
in computers and how they work. Sitting down and preparing for a job
interview means being at least somewhat interested in the job and the
company. That alone eliminates a large fraction of weak candidates.

**Leetcode-style questions test intelligence.** While candidates
sometimes try to brute-force these questions by remembering all
possible answers, people with high IQ have a huge natural
advantage. Smart people are generally useful, and assessing _how
smart a candidate is_ is a core part of interviews (being smart covers
a multitude of other flaws). That is also why universities find SAT
results useful. Of course, measuring IQ directly via a test would
presumably be more precise, but the US has a history of
[disincentivizing](https://en.wikipedia.org/wiki/Griggs_v._Duke_Power_Co.)
this since the outcomes are politically disfavored. And a
pure IQ test would likely be less meaningful since leetcode-style
questions cover more ground, including prior knowledge:

**Leetcode-style questions test knowledge.**
The contrast between rote memorization and skill is
not as strict as it's sometimes made out to be, neither in software
engineering nor in other areas such as math. Knowing what, e.g., a Bloom
filter is is genuinely useful, as is knowing the name of the thing. Since
practically nobody is able to re-derive meaningful parts of computer
science from scratch by themselves (there is _some_ content to the
field after all), knowing what
exists and how to talk about it is a useful skill. During the actual
work of a good software engineer, various design decisions and
judgment calls about systems have to be made. Knowing the toolbox, and
knowing it well, is essential to making these decisions well. This can
be traded off with intelligence or other sources of good intuition
about these practical problems, but ceteris paribus knowing more is
better.

Of course that depends on the type of software engineering role the
candidate wants to fill. Folks writing database lookups for a Django
app may not need to know Fenwick trees. However, that brings me to

**AI's impact on software engineering.** I cannot foresee all
consequences of coding models on the ecosystem but it seems likely it
will change a lot and fast. It's possible the role won't
exist at all in the near term, in which case all interview techniques
are obsolete. It stands to reason though that the more routine, more
obviously automatable tasks will be automated first. Who's got
more job security, the guy who knows about Zobrist hashing or the
hundredth CRUD engineer? I don't know if "be the knowledgeable engineer"
is actionable advice -- since nobody decided to be somewhat
disinterested, most people just are like that -- but "hire the
knowledgeable engineer" is. Knowledgeable engineers work on harder, more interesting
problems and are likely to at some point in their career engage with
"low-level fundamentals". The blunt answer to the "I've never needed
this" argument is ["but the good ones
do"](https://www.smbc-comics.com/comic/why-i-couldn39t-be-a-math-teacher). And
for what it's worth, several of the ideas described below did end up being
relevant in my career.

**Leetcode-style questions are an industry standard for a reason.**
The artificialness of asking a problem from a predefined pool, again
and again and again, is even more obvious to the interviewers than it
is to the critics. Trying to do something smarter is a decades-old
idea. In his 2015 book, the long-time Google head of recruitment
Laszlo Bock described some of the ideas of early Google. They include
nifty ideas like programming-related easter eggs in Google search and
McKinsey-style brainteasers. Few if any of the cool ideas worked, and
Google instead relied on ~four structured interviews from a shared pool
with defined rubrics.[^google]

[^google]: This was when Google was cool.

---

I'm going to describe my favorite interview question. I used it
many dozens of times when interviewing for xAI and other places,
to the extent that it's slightly worn out (and unsurprisingly is
on [actual
leetcode](https://leetcode.com/problem-list/reservoir-sampling/)). However,
as per the above, I don't think I am giving "too much away" by
describing it here, and I may well use this question again. If
candidates read this, all the better -- we can dive in deep then. And
if they have not, despite knowing I'd interview them, that's an ever so
weak signal too.

I first heard this question when Greg Chanan interviewed me for FAIR
in 2018. I probably did okay-but-not-great. I did end up getting
an offer and I did join Facebook (renamed to Meta while I was there) in
early 2019.

Without further ado, here's the question in its first variant.

## Random sampling question, version 1

> Given an array `L` of length `N` and a number `k` with `0 <= k <= N`,
> sample `k` elements from `L`, uniformly and without replacement.

I typically would suggest some kind of source of randomness, e.g. the
Python standard library functions
[`random.random`](https://docs.python.org/3/library/random.html#random.random)
and
[`random.randrange`](https://docs.python.org/3/library/random.html#random.randrange),
with the following behavior:[^randrange]

<dl>
<dt><tt>random.random()</tt></dt>
<dd>Return the next random floating-point number in the range <code
class="docutils literal notranslate"><span class="pre">0.0</span>
<span class="pre">&lt;=</span> <span class="pre">X</span> <span
class="pre">&lt;</span> <span class="pre">1.0</span></code></dd>

<dt>&nbsp;</dt>

<dt><tt>random.randrange(stop)</tt></dt>
<dd>Return a randomly selected element from
<tt>range(stop)</tt>.
</dd>
</dl>

[^randrange]: The Python standard library also has a
    <tt>random.randrange(start, stop[, step])</tt> version, but we
    will use the one-argument version of `randrange` here.

Some candidates want an explanation of the terms: "uniform" means
every entry of the array has the same chance of being sampled;
"without replacement" means elements are discarded after being sampled
and cannot be sampled again: in the "urn model", the balls taken out
of the urn are not being put back into the urn, so they are not being
replaced.

This opens the door to another question: What is a "same element"
for the purpose of this question? It's overall more interesting if
there's no object equality check a la `__eq__` in Python here but
instead all elements of the array can be assumed to be unique. This also
implies their index is the only thing that matters, and what the
elements of the array are is otherwise not important.

### Monte Carlo solution (aka rejection sampling)

A first attempt to solve this could look like[^style]

```python
from random import randrange

def sample(L, k):
    result = set()
    while len(result) < k:
        result.add(L[randrange(len(L))])
    return result
```

[^style]: Yes, we'll be using `L` as a Python variable name,
    regardless of what the [Google Python Style
    Guide](https://google.github.io/styleguide/pyguide.html) says. One
    of the advantages of leaving Google is to be _free_.

This is decent if `k/N` is a small number but catastrophically
slow when `k` is close to `N`. However, in the case `k/N >= 0.5` one
can choose to sample _rejected_ instead of _selected_ items and
arrive at a decent solution overall. This way, the algorithm makes
progress in each iteration with probability $$\ge 0.5$$, which means the
chance of _not_ making progress after $$m$$ steps decays exponentially
in $$m$$. Note though that the worst case
time complexity is still unbounded ("$$O(\infty)$$").

That's good enough for most practical applications -- but not good
enough for a coding interview. So let's say we are looking for a
solution with deterministic complexity.

### Naive deletion

One solution that maps well to "don't replace balls in the urn"
is simply

```python
def sample(L, k):
    result = []
    for _ in range(k):
        j = randrange(len(L))
        result.append(L[j])
        del L[j]
    return result
```

In place of `del L[j]`, some people even go for `L = L[: j] + L[j +
1 :]`. If they have more Python knowledge they might propose

```python
def sample(L, k):
    result = []
    for _ in range(k):
        result.append(L.pop(randrange(len(L))))
    return result
```

All of these are correct solutions, but they suffer from a similar
problem. In order to delete an element of an array _while keeping
$$O(1)$$ lookups in place_, deletion requires _shifting all later
elements_ which is $$O(N)$$.

In memory, an array is a buffer that starts at `start_ptr` and ends at
`start_ptr + buffer_len`:

```
[ a b c d e f g h i j k l m ]
  ^                         ^
  start_ptr                 |
       start_ptr + buffer_len
```

Looking up the element at index `i` means resolving
a pointer to `start_ptr + i`. This makes lookups $$O(1)$$ and
cheap even within that class.

Deleting an element -- say, `g` -- creates a hole:

```
[ a b c d e f _ h i j k l m ]
```

The only way to keep simple $$O(1)$$ lookups is to shift later
elements into the hole:

```
[ a b c d e f h _ i j k l m ]
                  <

[ a b c d e f h i _ j k l m ]
                    <

[ a b c d e f h i j _ k l m ]
                      <

etc.
```

This makes deletion shift $$N/2$$ elements on average and $$O(N)$$.

Note that a Python `list` is also just such a buffer in memory with a
physical capacity and a logical length. When it needs to grow
beyond its capacity a new buffer is created and all elements (which
are pointers of type `PyObject*`) are copied. Candidates often _think_ they
don't know that that is the case but they typically can infer this once
the "contract" of the list is pointed out, which is that random
access is $$O(1)$$. There is simply no alternative to an array under
this contract! See
[listobject.c](https://github.com/python/cpython/blob/main/Objects/listobject.c)
in the CPython source for the details.

### Keeping track of gaps?

Some people, myself included, find it natural to try
to track already selected elements. In step `i`, one could attempt to
sample from `randrange(N - i)` and then add the number of gaps already
chosen left of `i`. While natural, this is complicated and yields at
best some kind of tree structure and an $$O(k \log k)$$ solution, while
$$O(k)$$ should be and is possible.

Some folks propose all kinds of dictionary/hash map approaches, most
of which fail (with an exception, not realistically findable in an
interview, see below!). The fundamental problem is that arrays allow
$$O(1)$$ lookup of the $$i$$th element but require $$O(N)$$ deletions,
while hash maps _might_ allow for $$O(1)$$ deletions but looking up
the $$i$$th element costs $$O(N)$$. Hash maps generally are somewhat
overused due to their convenience. Some
candidates have a really hard time giving them up for this problem.

### Swapping to the end

Still, modifying the array is promising, and candidates often find a
better solution when they are explicitly told that's an okay thing to
do. For instance, one could do

```python
from random import randrange

def sample(L, k):
    N = len(L)
    result = []
    for i in range(k):
        j = randrange(N - i)
        # Take element j, then move in element from the end.
        result.append(L[j])
        L[j] = L[N - i - 1]
    return result
```

Note that `L[j] = L[N - i - 1]` can be a no-op if the sampled index
`j` was the end.

This is an example of a "swap with the end" trick that's useful more
generally. With swapping instead of moving one can also avoid the
`result` array:

```python
from random import randrange

def sample(L, k):
    N = len(L)
    for i in range(k):
        j = randrange(N - i)
        L[j], L[N - i - 1] = L[N - i - 1], L[j]
    return L[N - k :]
```

This is pretty short and $$O(k)$$ in time with essentially no extra
space, assuming the slice at the end doesn't create a copy -- true if
`L` is an object like a NumPy array but not true for plain Python
lists. If `k` is nonzero, the slice at the end can be written
as `L[-k :]` but that fails for `k == 0`.

### Via partial shuffle

Sometimes candidates find that "shuffle the list and take the first
`k` items" is a more intuitive solution:

```python
def sample(L, k):
    shuffle(L)
    return L[:k]
```

The question then is how to shuffle. A moment's reflection shows
that "go through all slots and swap with a random one" is promising:

```python
def shuffle(L):
    for i in range(len(L)):
        j = i + randrange(len(L) - i)
        L[i], L[j] = L[j], L[i]
```

The logic of this algorithm (known as Fisher-Yates in the literature)
is to keep a range of not-yet-chosen elements that is initially the
full array and then shrinks from the left by one element each
iteration. (Since the last random "choice" is choosing from the
one-element `range(1)`, the loop could actually use `range(len(L) - 1)`.)

This has the nice property that each to-be-filled slot is chosen
once and then the algorithm sticks to its choice.

It can be turned into a "partial shuffle" where one stops after `k`
slots:

```python
def shuffle(L, k):
    for i in range(k):
        j = i + randrange(len(L) - i)
        L[i], L[j] = L[j], L[i]
```

With this, `shuffle(L, k)` and then returning `L[: k]` is equivalent to
the swapping-to-the-end solution, but easier to find for some people.

#### A fun side quest

Here's a side question: What if we don't stick with our choices, but
instead allow the full array to be selected every time? This way we
potentially swap already chosen elements:

```python
def alt_shuffle(L):
    for i in range(len(L)):
        j = randrange(len(L))
        L[i], L[j] = L[j], L[i]
```

As an algorithm, this feels worse -- for instance, the original
`shuffle` allows us to `yield` results as they come. But is it any
worse otherwise? Is it correct? Are both `shuffle` and `alt_shuffle`
correct, or only one of them? Or, less plausibly, neither?

<details markdown="1">
<summary>Click here to find out about <tt>shuffle</tt> vs. <tt>alt_shuffle</tt>.</summary>
It turns out, `alt_shuffle` is wrong in that it doesn't result in a
_uniform_ shuffle.

This is true in general for $$N\ge 3$$ but one easy way to see this is
to assume that $$k = N = p$$ for a prime number $$p > 2$$. The number
of different random inputs from `randrange` for `shuffle` is exactly
$$N(N-1)\cdots 1 = N!$$. This is also the number of random
permutations of $$N$$ items; the algorithm is selecting
one such permutation, step by step.

For `alt_shuffle`, the number of different random inputs the
algorithm uses is $$N^N$$. That is a vastly larger number than
$$N!$$, but that by itself doesn't mean `alt_shuffle` is
incorrect, assuming the $$N^N$$ random choices can be mapped to
$$N!$$ choices in a way that divides the $$N^N$$ choices evenly. However, the
expression $$N!$$ has prime factors for every prime up to $$N$$, while
$$N^N$$ only has $$p$$ as a prime factor. $$N^N$$ isn't divisible by
$$N!$$ (that is, $$N^N/N!$$ is not an integer). This means `alt_shuffle`
selects some of the $$N!$$ permutations with higher probability than
others and isn't uniform.
</details>

### Floyd's algorithm

**What is optimal?** In a sense, the partial shuffle/swapping-based
solution is optimal -- it's $$O(k)$$ with minimal space overhead. Its
only imperfection is the
fact that the input array `L` is modified. Of course this can be
avoided by making a copy, but that means we are no longer $$O(k)$$.

Can we avoid modifying the input? No simple change to the
swapping-based solution will achieve that, because the algorithm uses
the buffer as a scratchpad to keep track of which of the $$N!$$
permutations has been selected.

An $$O(k)$$ _space and time_ solution to this exercise could dispense
with the array altogether, since it really just selects $$k$$
indices. One could simply ask:

> Generate `k` distinct uniformly random integers in `range(N)` in
> $$O(k)$$ space and time.

I had asked many candidates the sampling question before I found
this version, innocently stated as [Exercise 5-2 of the AWK
programming
book](https://archive.org/details/pdfy-MgN0H1joIoDVoIC7/page/n123/mode/2up). Their
[proposed
solution](https://archive.org/details/pdfy-MgN0H1joIoDVoIC7/page/n209/mode/2up),
translated to Python, reads like this:

```python
from random import randrange

def sample(N, k):
    result = set()
    for i in range(N - k, N):  # k steps.
        r = randrange(i + 1)
        if r in result:
            r = i
        result.add(r)
    return result
```

This is known as _Floyd's algorithm_, due to R.W. Floyd, 1978 Turing
Award winner and close collaborator of Donald Knuth at Stanford.

It wasn't immediately obvious to me why this algorithm is correct. The
fact that the math of "if seen already, choose the end" works
is somewhat magical. For a discussion of Floyd's algorithm,
check out ["A Sample of Brilliance" in Jon Bentley's _Programming
Pearls_](https://dl.acm.org/doi/10.1145/30401.315746).

Very few people will be able to derive something like that
in the scope of a coding interview. Only a handful of people
even know this algorithm in the first place;
nobody I ever interviewed did.

## Version 2: $$O(N)$$ solutions

One of the neat properties of this problem is its many
variations. Having solved the original version, what if we look to
sample from a _stream_ instead? A stream is an object that we can ask
for its next value, which will either yield another value or tell us
the stream has ended. In Python, that maps to the concept of an
[iterator](https://docs.python.org/3/glossary.html#term-iterator).

For this exercise to make sense, we need some guarantees: The stream
needs to (1) have at least `k` elements, and (2) eventually end.

The point of asking about streams is to force the solution to be
$$O(N)$$, which gives a different landscape of trade-offs. Of course,
we could simply collect all $$N$$ items in an array and apply the
solutions we already saw, but perhaps we can do this in $$O(k)$$ space?

### Streams of known length

#### Selection sampling

Let's say we also get information about the eventual length of the
stream. In that case, sampling $$k$$ out of the $$N$$ items we will
see, naively, is[^random0]

```python
from random import random

def sample(it, N, k):
    for e in it:
        if random() < k/N:
            yield e
```

[^random0]: Note that `random() < k/N` with a strict `<` (and not
    `<=`) is the correct comparison; this matches the property where
    the return value of `random()` _can_ be `0.0` but can not be
    `1.0`.

The issue with this algorithm is that it could sample both fewer and
more than $$k$$ elements. It's correct "on average" but each run has
some variation.

Sampling too much is easily fixable -- we can just stop after $$k$$
samples. But it's unclear if that maintains uniformity, and anyway
what can we do about sampling too little? What we should do is
to increase the probability as we go along, for instance in a situation
where we have sampled $$k - 1$$ elements and the stream only contains
a single final element, that one has to be sampled with probability
$$1$$.

To achieve that, note that regardless of whether we chose to sample or
not to sample an element in a given round, we modified the problem by
reducing the size of the remaining stream by one, and if we sampled an
element we reduced the number of yet-to-be-sampled elements by one as
well. In a situation where only a single element is left to be sampled
and we need another sample, we have a $$k=1$$, $$N=1$$ subproblem. This
suggests the approach

```python
from random import random

def sample(it, N, k):
    for e in it:
        if random() < k/N:
            yield e
            k -= 1
        N -= 1
```

Optionally, we could also short-circuit via something like `if not k:
return`. A moment's reflection shows that this algorithm always
produces $$k$$ elements and is correct.

This algorithm is Knuth's Algorithm S, "selection sampling" (from _The
Art of Computer Programming_, Vol. 2, §3.4.2). It is short, sweet, and
"online" -- we can yield instead of waiting for the stream to finish.
It is the right approach for many applications, including handling
classic magnetic tapes which are linear by nature.

### Streams of unknown length

What should we do if we are not being given the length of the stream
in advance? What _can_ we do?

One obvious thing we cannot do anymore is to have an online solution
that `yield`s its results. Since the stream could go on for many more
elements or stop right now and each element needs to have the same
chance of making it, any solution will have to have the form

```python
def sample(it, k):
    results = []

    for e in it:
        # do things and add to results

    return results
```

#### Heaps

One first idea might be to sort random numbers. We could for instance
maintain a min-heap, along the following lines:


```python
import heapq
from random import random

def sample(it, k):
    h = [(random(), next(it)) for _ in range(k)]
    heapq.heapify(h)  # Tuples compare by first value first.

    for e in it:
        # Push e on heap, then pop smallest.
        heapq.heappushpop(h, (random(), e))

    return [e for _, e in h]
```

Somewhat surprisingly, `heapify` is implementable in $$O(k)$$. The use
of `heappushpop` here makes sense since heap operations are typically
"modify the heap as requested, then recreate the heap property". Since
here each push is followed by a pop, `heappushpop` allows us to skip
one heap recreation. It runs in $$O(\log k)$$ for a heap of size
$$k$$.

Overall this algorithm is $$O(k) + O(N \log k)$$ in time.

There is an issue with this approach though: It relies on each
`random()` number being truly different from each other one. Since
Python's `float`s don't have infinite precision, collisions
are possible and due to the birthday paradox are actually
more likely than intuitively expected.[^birthday] If our streamed
elements are not comparable, this will make the above algorithm crash
at runtime -- and if they are, uniformity will be violated. The
only real solution to this I can see is to modify the comparison to
have random tie breaks which breaks the deterministic runtime behavior
and is not pleasant to implement.

[^birthday]: On a typical contemporary computer, a Python `float` is
    a double aka `float64`. Python's `random()` returns one of $$N =
    2^{53}$$ equally spaced doubles in $$[0,
    1)$$. The birthday threshold is $$\sqrt{2N\ln 2}$$ which is around
    111M. But for this solution we have to worry about collisions
    within the set of $$k$$ elements in the heap only.


#### Quickselect

While it doesn't apply in the streaming case, it's good to remember
that quickselect is the standard algorithm for finding the $$k$$th
smallest element in an unsorted list, or the $$k$$ smallest
elements. However since it requires modifying the full array, it isn't
the best approach for the problem at hand. (It also suffers from the
same floating point collision issue.) It's still very good to know
quickselect, which is why I mention it here.

#### Reservoir sampling

The real beauty of the streaming version of this question comes out in
this solution. Let's go back to the template we know we will require:

```python
def sample(it, k):
    results = []

    for e in it:
        # do things and add to results

    return results
```

We can view this question in several ways. One of them is to think of
it as some sort of adversarial game: Let's say you are the algorithm
and the interviewer is the stream. The algorithm can do whatever it
wants with its inputs, but the stream can decide to either give
another element or end itself and ask you to "show your work" in the
least convenient moment possible.

Thinking along these lines creates one realization: We have to be
correct for all kinds of values of $$N$$ and $$k$$, including $$N =
k$$. In that case there isn't much we can do, we need to return the
first $$k$$ inputs. So let's code that:

```python
def sample(it, k):
    results = [next(it) for _ in range(k)]

    for e in it:
        # do things and add to results

    return results
```

This now is at least correct for the $$N = k$$ case. Can we make it
correct for $$N = k + 1$$ as well? (You see where this is going.) For
$$N = k + 1$$, what's the chance of any given element to be in the
`results` array? It will be $$\frac{k}{k+1}$$. Essentially, _if_ we
see another element after the guaranteed first $$k$$, what
choice do we have? We can choose it or reject it with a certain
probability, and if we choose it, we can evict a previously chosen
element with some probability. Since the stream could end right after
that additional element, _its_ probability of being chosen has to be
correct, namely `k / N` which is `k / stream_len_so_far` in this case.

This is the beauty of this algorithm: We have to _assume_ a solution
can be found, and under that assumption we only have that choice:

```python
from random import random

def sample(it, k):
    results = [next(it) for _ in range(k)]

    for stream_len, e in enumerate(it, k + 1):  # Start with k + 1
        if random() < k / stream_len:
            # Choose `e`.

    return results
```

This is almost the full algorithm. The remaining question is what to
evict? Given the uniform sample we want to produce, it stands to
reason that we want to select elements for eviction from the pool
`results` -- let's actually call it a reservoir -- with
uniform probability:

```python
from random import random, randrange

def sample(it, k):
    reservoir = [next(it) for _ in range(k)]

    for stream_len, e in enumerate(it, k + 1):
        if random() < k / stream_len:
            reservoir[randrange(k)] = e

    return reservoir
```

A slight optimization requires only a single random choice here:

```python
from random import randrange

def sample(it, k):
    reservoir = [next(it) for _ in range(k)]

    for stream_len, e in enumerate(it, k + 1):
        if (i := randrange(stream_len)) < k:
            reservoir[i] = e

    return reservoir
```

That is a neat algorithm. But is it correct? We arrived at it by
assuming something like this is possible; in particular, we chose the
probabilities such that the final element's chance of ending in the
chosen set is correct.

Given enough time, good candidates arrive at a short inductive proof of the
correctness of this algorithm. For a given $$k$$, the probability for
any element to end up in the final set is obviously correct if $$N =
k$$. Assuming the algorithm is correct for a given stream length
$$N$$, moving to a stream length $$N + 1$$ requires one more
iteration. We already know the final new element is chosen with the
right probability, but what happens to the other elements? Their
previous chance to end up in `reservoir` was $$k / N$$. Their chance
to still be in the reservoir after one more iteration is _that_, times (1) the
chance of the final element to be discarded, plus (2) the chance of
the final element to be chosen, but another element to be
evicted. This telescopes nicely since

$$
\frac{k}{N} \cdot \Big(1 - \frac{k}{N+1} + \frac{k}{N+1} \cdot \frac{k-1}{k}\Big)
= \frac{k}{N} \cdot \Big(\frac{N + 1 - k}{N + 1} + \frac{k - 1}{N +
1}\Big)
= \frac{k}{N} \cdot \frac{N}{N+1} = \frac{k}{N+1}.
$$

So the probabilities of the previous elements are updated in the
correct way too.

This algorithm is known as _reservoir sampling_. It's a classic
from the literature; Knuth calls it Algorithm R in TAOCP Volume 2.

#### Reservoir sampling with skipping ahead

Fancier versions of reservoir sampling exist. One
interesting variant is if we assume we can cheaply skip ahead in the
iterator. If the length of the stream `N` is large compared to the
number of selected elements and there is processing work for each
element that pays off to be avoided where possible, this can be a
powerful idea.

Let's invent an iterator method where say `skip(it, j)` skips and
discards `j` elements from the iterator (making `skip(it, 0)` a
no-op). The skipping version of reservoir sampling can then be written
as

```python
from math import exp, floor, log, log1p
from random import random, randrange

def sample(it, k, done=object()):
    reservoir = [next(it) for _ in range(k)]
    w = 1.0
    while True:
        w *= exp(log(random()) / k)
        skip(it, floor(log(random()) / log1p(-w)))
        if (e := next(it, done)) is done:
            break
        reservoir[randrange(k)] = e

    return reservoir
```

Here `w` is the probability that the next element of the stream will
be accepted, and `log1p(-w)` computes $$\log(1 - w)$$ without losing
precision when `w` is small.[^logzero]

This version of reservoir sampling was published in 1994 by Kim-Hung
Li, see [Reservoir-sampling algorithms of time complexity $$O(n(1 +
\log(N/n)))$$](https://dl.acm.org/doi/10.1145/198429.198435).

[^logzero]: Funnily enough, the code isn't quite bug-free as
    written. Since `random()` can be `0.0`,
    `math.log(random())` can raise a `ValueError` with probability
    $$2^{-53}$$. A full implementation should probably special-case
    both `w == 0.0` and `w == 1.0`.

Other versions exist, including for sampling from non-uniform
distributions. Your favorite LLM will happily explain all about them.

## Online shuffling

There is a related idea that is underappreciated.

Let's say we have a large dataset (e.g., a table in SQL)
which comes in the form

```
  # |   value
-------------
  1 |  entry1
  . | .
  . | .
  . | .
  N |  entryN
```

We now want to do "online shuffling", i.e., go through the dataset in
a random order, visiting each sample exactly once. We also want to be
preemptible -- our algorithm can be stopped and later restarted from a
checkpoint. Perhaps we would even like this to be _seekable_: Quickly
asking for the entry that comes at position `i` of the shuffle.

What we are asking for is equivalent to selecting one of the $$N!$$
many permutations of $$N$$ items, then doing lookups of the form

```python
for i in range(N):
    sample = samples[p(i)]
    ...
```

This is similar to the sampling question in that doing this requires a
scratch buffer of size $$O(N)$$ to keep track of what has been sampled so
far. For instance, this could be done like:

```python
import numpy as np
from random import randrange

def permit(N):
    L = np.arange(N)
    for i in range(N):
        j = i + randrange(N - i)
        L[i], L[j] = L[j], L[i]
        yield L[i]
```

However, this is a heavy amount of state for our checkpoint: For a
dataset of 1B entries we would use 8 GiB just for the
`np.arange(N)`. It's also not quickly seekable in that the full array
needs to be assembled before we can do lookups.

### Block ciphers

If we want to deal with far less state (say, a few kilobytes), the
problem cannot be solved _exactly_. But it can be
solved approximately, and one can prove the approximation is good.

One trick is to use an idea from cryptography: A _block cipher_ is a
symmetric encryption algorithm which takes a secret key `k` and buffers of
a fixed length and maps them to encrypted buffers of the same length:

```
plain text buffer: B
encrypted buffer:  encrypt(B, k)
decrypted buffer:  B == decrypt(encrypt(B, k), k)
```

Both the unencrypted input `B` and the encrypted buffer `encrypt(B, k)`
have the same number of bits, say $$n$$. In particular, this means
that for a given key `k` the functions

$$
\begin{align}
\mathtt{encrypt}(\dotid, \mathtt{k}) & \from \set{0, 1}^{n} \to \set{0,
1}^{n}, \\
\mathtt{decrypt}(\dotid, \mathtt{k}) & \from \set{0, 1}^{n} \to \set{0,
1}^{n}
\end{align}
$$

are bijections (one-to-one) and each is the inverse of the
other. Here, $$\set{0, 1}^{n}$$ is the set of all buffers of 0s and 1s
of length $$n$$, which is a set of $$2^n$$ elements.

### Pseudorandom permutations

How are we going to use this block cipher? We will use $$n = 64$$ and
interpret a given index `i` of type `uint64` as a block of 64 bits and
use a block cipher for that block size. We then encrypt that index to
find where it maps to:

```python
import numpy as np

def perm(i):
    B = np.array(i, dtype=np.uint64)
    k = KEY  # Global in this example.
    return encrypt(B, k).item()

def permit(N):
    for i in range(N):
        yield perm(i)
```

Since $$\mathtt{encrypt}(\dotid, \mathtt{k})$$ is one-to-one, each
possible bit pattern is produced exactly once. `perm` is an actual
permutation of the set of `uint64`s (a set of $$2^{64}$$ elements).

This works as described if the (humongous) table has size exactly
$$N = 2^n = 2^{64}$$. Realistically, it's smaller and we need some
additional ideas.[^power] This is a great topic to discuss with an
LLM!

[^power]: Let's say we have a block cipher for any power of two. How
    can we use that to shuffle tables of _arbitrary_ size?

Note that the permutation is parameterized only by the key `k`. If `k`
has `m` bits, that means we can only produce $$2^m$$ different
permutations, which is vastly fewer than the full number of
permutations of the set of `uint64`s, which is $$(2^{64})!$$, a number
that has about $$3.47 \times 10^{20}$$ digits.[^digits] By contrast,
the number of atoms in the observable universe has about 80 digits!
Combinatorics creates large numbers very fast. The actual fraction of
permutations reachable by this scheme is very close to $$0\%$$.

[^digits]: How do I know that number? It turns out the Log-gamma
    function $$\ln\circ\,\Gamma$$ is a well understood object with a
    fast converging series representation. Since $$\Gamma(n + 1) =
    n!$$ and Python has bignums, we can literally compute
    `math.lgamma(2**64 + 1)` and convert $$\ln$$ to $$\log_{10}$$.

So we will only ever get an absurdly tiny fraction of all possible
permutations this way. How far away from truly random permutations
are we with these _pseudorandom permutations_?

The answer depends on the quality of the `encrypt` function. In many
scenarios, cryptographers could prove that one cannot actually tell
the difference! To learn more, check out [Feistel
networks](https://en.wikipedia.org/wiki/Feistel_cipher)[^feistel] and a
result known as the _Luby-Rackoff theorem_.[^lubyrackoff]

[^feistel]: The tl;dr on Feistel networks is: Split the input into its
    left and right part, then compute `right, left = left ^
    hash(right, key), right` for a number of rounds. Decryption is
    doing the same kind of operation in reverse.

[^lubyrackoff]: Note though that the specific mathematical guarantee from
    Luby-Rackoff does not map well to a large table that we shuffle
    completely since the bound is $$q^2 / 2^{n/2}$$ after $$q$$
    queries. For $$n=64$$ this is exhausted after $$q\approx 2^{16} =
    65536$$ queries. Unbalanced Feistel ciphers can help, as can other
    ciphers like
    [Speck64](https://en.wikipedia.org/wiki/Speck_(cipher)), which are
    in the class where "no successful attack is publicly known at
    this point (but people tried)".

### Cheap parameterized permutations

On the other end of the spectrum, very cheap parameterized permutations
come from _mixers_ (or _finalizers_) of hash functions like
MurmurHash3. An [influential 2011 blog post by David
Stafford](https://zimbry.blogspot.com/2011/09/better-bit-mixing-improving-on.html)
proposed using

```c
uint64_t mix13(uint64_t x)
{
    x ^= x >> 30;
    x *= 0xBF58476D1CE4E5B9UL;
    x ^= x >> 27;
    x *= 0x94D049BB133111EBUL;
    x ^= x >> 31;
    return x;
}
```

MurmurHash3 and this blog post were the starting point of all kinds of
results around fast permutations. Stafford's suggestion made it into
[JDK 8 in
2013](https://github.com/openjdk/jdk/commit/231a351a47d4d3fb8034115584bef6847486bc68)
and was also cited as canonical in _Fast Splittable
Pseudorandom Number Generators_ by Steele, Lea and Flood
in 2014. Since 2018, Pelle Evensen has had
[several](http://mostlymangling.blogspot.com/2018/07/on-mixing-functions-in-fast-splittable.html)
[blog
posts](http://mostlymangling.blogspot.com/2020/01/nasam-not-another-strange-acronym-mixer.html)
around improvements. These fast permutations satisfy certain
statistical properties but not others (e.g., `mix13` above sends an
all zero buffer to zero; this can be fixed with extra xors). They are
certainly not "cryptographically strong", but their statistical
properties can be surprisingly good and they are extremely cheap.

Much more can be said about random sampling and shuffling. But this blog
post is long enough and making it longer will not illustrate the point
any better.

{% comment %}

#### Feistel networks

However, it turns out that slightly more costly variants give actual
cryptographic guarantees. For instance, one can start from a strong hash
function and build a block cipher via [Feistel
networks](https://en.wikipedia.org/wiki/Feistel_cipher).[^feistel]
This construction offers some guarantees, although the mathematical
bounds only give strong security up to thousands of queries.

[^feistel]: The tl;dr on Feistel networks is: Split the input into its
    left and right part, then compute `right, left = left ^
    hash(right, key), right` for a number of rounds. Decryption is
    doing the same kind of operation in reverse.

A result by Luby and Rackoff from 1988 shows that Feistel networks
give strong cryptographic guarantees (assuming the pseudorandom
hash function we use is strong enough, and we use it correctly, and
we use at least four Feistel rounds).

[^advantage]: Roughly speaking, the
      cryptographic setup is that an attacker is attempting to classify a
      black box which either does `encrypt` and `decrypt` Feistel operations
      _or_ is a "real" permutation drawn uniformly from all $$2^{64}!$$ permutations,
      plus its inverse. The attacker can make $$q$$ "queries" (forward or
      backward operations of his choice) against the black box. Afterwards,
      the attacker says whether he believes the black box to be of the
      Feistel type or the "real" type. The _advantage_ measures what the
      attacker gained from doing $$q$$ queries. If the attacker learned
      nothing, the advantage is zero; if he can always tell the difference,
      it is one. The Luby-Rackoff result is that the advantage of the best
      attacker is bounded by roughly $$\frac{q^2}{2^{n/2}} + \varepsilon_h$$
      where $$n = 64$$ is the block size and $$\varepsilon_h$$ is the best
      distinguishing advantage against the underlying pseudorandom hash
      function at comparable resources.

In essence, this means a cryptographic attacker requires thousands of
dedicated probes to tell the two cases apart. For our simple
statistical purpose, the permutation looks close enough to having been
chosen truly at random.

{% endcomment %}
