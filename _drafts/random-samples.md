---
layout: post
title:  "Leetcode-style interviews and my favorite question"
---

* Table of contents
{:toc}

I'm going to describe my favorite interview question. I used it
probably hundreds of times when interviewing for xAI and other places,
to the extend that it's slightly worn out.

I learned about this question when Greg Chanan interviewed me for FAIR
in 2018. I probably did okay-but-not-great but I did end up getting
and offer and I did join Facebook (soon to be renamed to Meta) in
early 2019.

Without further ado, here's the question.

## Random sampling question, version 1.

> Given an array `L` of length `N` and a number `k` with `0 <= k <= N`,
> sample `k` elements from `L`, uniform and without replacement.

I typically would suggest some kind of source of randomness, e.g. the
Python standard library functions
[`random.random`](https://docs.python.org/3/library/random.html#random.random)
and
[`random.randrange`](https://docs.python.org/3/library/random.html#random.randrange),
with the following behavor[^randrange]

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

Some candidates want some explanation of the terms: "uniform" means
every entry of the array has the same chance of being sampled;
"without replacement" means elements are discarded after being sampled
and cannot be sampled again (in the "urn model", the balls taken out
of the urn are not being put back into the urn, so they are not being
replaced).

This opens the door to a first clarification: What is a "same element"
for the purpose of this question? It's overall more interesting if
there's no object identity check a la `__eq__` in Python here but
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

This is very decent if `k/N` is a small number but catastrophically
slow when `k` is close to `N`. However, in the case `k/N >= 0.5` one
can just chose to sample _rejected_ instead of _selected_ items and
arrive at a decent solution overall. This way, the algorithm makes
progress in each iteration with probabilty $$>= 0.5$$, which means the
chance of _not_ making progress after $$m$$ steps decays exponentially
in $$m$$. Note though that the worst case
time complexity is still unbounded ("$$O(\infty)$$").

That's a decent solution, good enough for most practical
applications - but not good enough for a coding interview. So let's
say we are looking for a solution with deterministic
complexity.

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
$$O(1)$$ lookups in place_, deletion requires _shifting all latter
elements_ which is $$O(N)$$.

In memory, an array is just a buffer that starts at `start_ptr` and ends at
`start_ptr + buffer_len`:

```
[ a b c d e f g h i j k l m ]
  ^                       ^
  start_ptr               |
     start_ptr + buffer_len
```

Looking up the element at index `i` just means resolving
a pointer to `start_ptr + i`. This makes lookups $$O(1)$$ and very
cheap even within that class.

Deleting an element -- say, `g` -- creates a hole:

```
[ a b c d e f _ h i j k l m ]
```

The only way to keep simple $$O(1)$$ lookups is to shift later
elements into the whole:

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
"physical" capacity and a "logical" length. When it needs to grow
beyond its capacity a new buffer is created and all elements (which
pointers of type `PyObject*`) are copied. Candidates often _think_ they
don't know that that is the case but they typically can infer this once
the "contract" of the list is pointed out, which is that random
access is $$O(1)$$. See
[listobject.c](https://github.com/python/cpython/blob/main/Objects/listobject.c)
in the CPython source for the details.




### Keeping track of gaps?

Some people, myself included, find it natural to try
to track already selected elements. In step `i`, one could attempt to
sample from `randrange(N - i)` and then add the number of gaps already
chosen left of `i`. While natural, this is complicated and yields at
best some kind of tree structure and a $$O(k \log k)$$ solution, while
$$O(k)$$ should be and is possible.

Some folks propose all kinds of dictionary/hash map approaches, most
of which fail (with an exception, not realistically findable in an
interview, see below!). The fundamental problem is that arrays allow
$$O(1)$$ lookup of the $$i$$th element but require $$O(N)$$ deletions,
while hash maps _might_ allow for $$O(1)$$ deletions but looking up
the $$i$$th element costs $$O(N)$$.

### Swapping to the end

Candidates often find a better solution when they are explicitly told
that they are allowed to modify the array. For instance, one could do

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
generally. With swapping instead of just moving one can also avoid the
`results` array:

```python
from random import randrange

def sample(L, k):
    N = len(L)
    for i in range(k):
        j = randrange(N - i)
        L[i], L[j] = L[j], L[i]
    return L[N - k :]
```

This is pretty short and $$O(k)$$ in time with essentially no extra
space (assuming the slice at the end doesn't create a copy -- true if
`L` is an object like a Numpy array but not true for plain Python
lists). If `k` is not zero, the slice at the end can be written
as `L[-k :]` but that fails presicely when `k == 0`.

### Via partial shuffle

Sometimes candidates find that "shuffle the list and take the first
`k` items" is a more intuitive solution:

```python
def sample(L, k):
   shuffle(L)
   return L[:k]
```

The question is, of course, how to shuffle. A moment reflection shows
that "go through all slots and swap with a random one" is promising:

```python
def shuffle(L):
    for i in range(len(L)):
        j = i + rangrange(N - i)
        L[i], L[j] = L[j], L[i]
```

The logic of this algorithm (known as Fisher-Yates in the literature)
is to keep a range of not-yet-chosen elements that is initially the
full array and then shrinks from the left by one element each
iteration. (Since the last random "choice" is chosing from the
one-element `range(1)`, the loop could actually use `range(len(L) - 1)`.)

This has the nice property that each to-be-filled slot is chosen,
once, and then the algorithm sticks to its choice.

It can be turned into a "partial shuffle" where one stops after `k`
slots:

```python
def shuffle(L, k):
    for i in range(k):
        j = i + rangrange(N - i)
        L[i], L[j] = L[j], L[i]
```

With this, `suffle(L, k)` and then returning `L[: k]` is equivalent to
the swapping-to-the-end solution, but easier to find for some people.

#### A fun side quest

Here's a side question: What if we don't stick with out choices, but
instead allow the full array to be selected every time (this means
that we potentially swap already chosen elements)?

```python
def alt_shuffle(L):
    for i in range(len(L)):
        j = rangrange(N)
        L[i], L[j] = L[j], L[i]
```

As an algorithm, this feels worse - for instance, the original
`shuffle` allows us to `yield` results as they come (but we still need
the buffer `L` to keep track of what we have chosen, see below for a
discussion of that). But is it any worse otherwise? Is it correct? Are
both `shuffle` and `alt_shuffle` correct, or only one of them? (Or,
less plausibly, neither?)

<details markdown="1">
<summary>Click here to find out about <tt>shuffle</tt> vs. <tt>alt_shuffle</tt>.</summary>
It turns out, `alt_shuffle` is wrong in that it doesn't result in a
_uniform_ shuffle.

This is true in general but one easy way to see this is to assume that
$$k = N = p$$ for a prime number $$p$$. The number of different random
inputs from `randrange` for `shuffle` is exactly $$N(N-1)\cdots
1 = N!$$. This is also the number of random permutations of $$N$$
items; what this algorithm is doing is selecting one such permutation,
step by step.

For `alt_shuffle`, the number of different random inputs the
algorithm uses is $$N^N$$. That is a vastly larger number than
$$N!$$, but that by itself doesn't mean `alt_shuffle` is
incorrect, assuming the $$N^N$$ random choices can be mapped to
$$N!$$ choices in a way that divides the $$N^N$$ choices evenly. However, the
expression $$N!$$ has prime factors for every prime up to $$N$$, while
$$N^N$$ only has $$p$$ as a prime factor. $$N^N/N!$$ is not an
integer; $$N^N$$ isn't divisible by $$N!$$. This means `alt_shuffle`
selects some of the $$N!$$ permutations with higher probabilty than
others and isn't uniform.
</details>

### Floyd's algorithm

**What is optimal?** In a sense, the partial shuffle/swapping-based
solution is optimal -- it's $$O(k)$$ with mimimal space overhead. It's
only imperfection is the
fact that the input array `L` is modified. Of course this can be
avoided by making a copy, but that means we are no longer $$O(k)$$.

Can we avoid modifying the input? No simple change to the
swapping-based solution will achieve that, because the algorithm uses
the buffer as a scratchpad to keep track which of the `N!`
permutations has been selected.

A $$O(k)$$ _space and time_ solution to this exercise could dispense
with the array altogether, since it really just selects $$k$$
indices. One could simply ask:

> Generate `k` distinct uniformly random integers in `range(N)` in
> $$O(k)$$ space and time.

I had asked this sampling question to many candidates already before I found
this is possible. I learned that by reading the innocently stated [Exercise 5-2 of the AWK
programming
book](https://archive.org/details/pdfy-MgN0H1joIoDVoIC7/page/n123/mode/2up). Their
proposed solution, translated to Python, reads like this:

```python
from random import randrange

def sample(N, k):
    result = set()
    for i in range(N - k, N):  # k steps.
        r = randrange(i)
        if r in result:
            r = i
        result.add(r)
    return result
```

This is known as _Floyd's algorithm_, due to R.W. Floyd, 1978 Turing
Award winner and close colaborator of Donald Knuth at Stanford.

It wasn't immediately obvious to me why this algorithm is correct. The
fact that the math of "if seen already, chose one past the end" works
is somewhat magical. For a discussion of Floyd's algorithm,
check out ["A Sample of Brilliance" in Jon Bentley's _Programming
Pearls_](https://dl.acm.org/doi/10.1145/30401.315746).

Very few people will be able to derive something like that
in the scope of a coding interview. In fact, only a handful people
even know this algorithm in the first place -- as far as I remember,
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

Let's say we also get information of the eventual length of the
stream. In that case, sampling $$k$$ out of the $$N$$ items we will
see, naively, is just[^random0]

```python
from random import random

def sample(it, N, k):
    for e in it:
        if random() < k/N:
            yield e
```

[^random0]: Note that `random() < k/N` with a strict `<` (and not
    `<=`) is the correct comparision; this matches the property where
    the return value of `random()` _can_ be `0.0` but can not be
    `1.0`.

The issue with this algorithm is that it could sample both fewer and
more than $$k$$ elements. It's correct "on average" but each run has
some variation.

Sampling too much is easily fixable -- we can just stop after $$k$$
samples. But it's unclear if that maintains uniformity, and anyway
what can we do about sampling too little? What we should do is
increasing the probability as we go along, for instance in a situation
where we have sampled $$k - 1$$ elements and the stream only contains
a single final element, that one has to be sampled with probability
$$1$$.

To achive that, note that regardless of whether we chose to sample or
not to sample an element in a given round, we modified the problem by
reducing the size of the remaining stream by one, and if we sampled we
reduced the number of yet-to-be-sampled elements by one as well. In a
situation where only a single element is left to be sampled and we
need another sample, we have a $$k=1$$, $$N=1$$ subproblem. This
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

This algorithm is Knuth's Algorithm S, "selection sampling" (from The
Art of Computer Programming, Vol. 2, §3.4.2). It is short, sweet, and
"online" (we can yield instead of waiting for the stream to finish)
and is the right approach for many applications, including handling
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

Somewhat surprisingly, heapify is implementable in $$O(k)$$. The use
of `heappushpop` here makes sence since heap operations are typically
"modify the heap as requested, then recreate the heap property". Since
here each push is followed by a pop, `heappushpop` allows us to skip
one heap recreation. It runs in $$O(\log k)$$ for a heap of size
$$k$$.

Overall this algorithm is $$O(k) + O(N \log k)$$ in time.

There is an issue with this approach though: It relies on each
`random()` number being truly different from each other one. Since
Python's `float`s don't have infinite precision (on a typical
contemporary computer it will be a double aka `float64`), collitions
are not impossible and due to the birthday paradox are actually
somewhat more likely than intuitively expected. If our streamed
elements are not comparible, this will make the above algorithm crash
at runtime -- and even if they are, uniformity will be violated. The
only real solution to this I can see is to modify the comparision to
have random tie breaks which breaks the deterministic runtime behavor
and is not pleasant to implement.

#### Quickselect

While it doesn't apply in the streaming case, it's good to remember
that quickselect is the standard algorithm for finding the $$k$$th
smallest element in an unsorted list, or the $$k$$ smallest
elements. However since it requires modifying the full array, it isn't
the best approach for the problem at hand.

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
it as some sort of adverserial game: Let's say you are the algorithm,
and the interviewer is the stream. The algorithm can do whatever it
wants with its inputs, but the stream can decide to either give
another element or end itself and ask you to "show your work" in the
least convienient moment possible.

Thinking along these lines creates one realisation: We have to be
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
see another element after the first $$k$$ (which are guarenteed), what
choice do we have? We can chose it or reject it with a certain
probability, and if we chose it, we can evict a previously chosen
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
            # Chose `e`.

    return results
```

This is almost the full algorithm. The remaining question is what to
evict? Given the uniform sample we want to produce, it stands to
reason that we want to evict all currently chosen elements in the pool
`results` -- let's actually call it a reservoir -- with the same
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

In fact, a slight optimization requires only a single random choice
here:

```python
from random import randrange

def sample(it, k):
    reservoir = [next(it) for _ in range(k)]

    for stream_len, e in enumerate(it, k + 1):
        if (i := randrange(stream_len)) < k:
           reservoir[i] = e

    return reservoir
```

That is a very neat algorithm. But is it correct? We arrived at it by
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

This magic algorithm is called _reservoir sampling_. It's a classic
from the literature; Knuth calls it Algorithm R in TAOCP Volume 2.

#### Reservoir sampling with skipping ahead

Fancier versions of reservoir sampling exist. One
interesting variant is if we assume we can cheaply skip ahead in the
iterator. If the length of the stream `N` is large compared to the
number of selected elements and there is processing work for each
element that pays of to be avoided where possible, this can be a
powerful idea.

Let's invent an iterator method where say `skip(it, j)` skips and
discards `j` elements from the iterator (making `skip(it, 0)` a
no-op). The skipping version of reservoir sampling can then be written
as

```python
from math import exp, floor, log
from random import random, randrange

def sample(it, k, done=object()):
    reservoir = [next(it) for _ in range(k)]
    w = 1.0
    while True:
        w *= exp(log(random()) / k)
        skip(it, floor(log(random()) / log(1 - w)))
        if (e := next(it, done)) is done:
            break
        reservoir[randrange(k)] = e

    return reservoir
```

This version of reservoir sampling was published in 1994 by Kim-Hung
Li, see [Reservoir-sampling algorithms of time complexity $$O(n(1 +
\log(N/n)))$$](https://dl.acm.org/doi/10.1145/198429.198435).

Other versions exists, including for sampling from non-uniform
distributions. Your favorite LLM will happily explain all about them.

## Online shuffling

There is a related idea that is underappreciated.

Let's say we have a large dataset (e.g., a table in SQL)
which comes in the form

```
row |
-------------
  0 |  entry0
  1 |  entry1
  . | .
  . | .
  . | .
  N |  entryN
```

We now want to do "online shuffling", i.e., go through the dataset in
a random order, visiting each sample exactly once. We want to do that
while being preemptible -- our algorithm can be stopped and later
restarted from a checkpoint.

Let's further say the number of samples $$N$$ is large enough such
that even an array like `np.arange(N)` does not fit into the memory of
a single machine (this will be true around hundred billion entries or
so).

What we are asking for is equivalent to selecting one of the $$N!$$
many permutations of $$N$$ items, then doing lookups of the form

```python
for i in range(N):
    sample = samples[p(i)]
    ...
```

This is similar to the sampling question in that doing this requires a
scratch buffer of size $$O(N)$$ to keep track what has been sampled so
far. For instance, this could be done like:

```python
import numpy as np

def permit(N):
    L = np.arange(N)
    for i in range(N):
        j = i + rangrange(N - i)
        L[i], L[j] = L[j], L[i]
        yield L[i]
```

However, this is a heavy amount of state for our checkpoint and
requires special handling in our case where `np.arange(N)` exceeds the
available memory.

### Block ciphers

If we want to deal with far less state (say, a few kilobytes), the
problem cannot be solved _exactly_. But it can be
solved approximately, and one can prove the approximation is an
extremely good one.

The trick is to use an idea from cryptography: A _block cipher_ is a
symmetric encryption algorithm which takes a secret key and buffers of
a fixed length and maps them to encrypted buffers of the same length:

```
plain text buffer: B
encrypted buffer:  encrypt(B, k)
decrypted buffer:  B == decrypt(encrypt(B, k), k)
```

Both the unencrypted input `B` and the encrypted buffer `encrypt(B, k)`
have the same amount of bits, say $$N = 2^n$$. In particular, this means
that the functions

$$
\begin{align}
\mathtt{encrypt}(\dotid, \mathtt{k}) & \from \set{0, 1}^{N} \to \set{0,
1}^{N}, \\
\mathtt{decrypt}(\dotid, \mathtt{k}) & \from \set{0, 1}^{N} \to \set{0,
1}^{N}
\end{align}
$$

are bijections (one-to-one) and each is the inverse of the
other. Here, $$\set{0, 1}^{N}$$ is the set of all buffers of 0s or 1s
of size $$N = 2^n$$.

{% comment %}

### Feistel network

There are many ways to create block ciphers. A popular one is a
_Feistel cipher_ (also known as _Feistel network_). It works by taking
some non-invertible "secure" function like a hash function that takes
(part of) the key `k` and a buffer half the length of `B` and produces some
output (not assumed to be invertible) of half the length of `B`.

The input is then split into a left part and a right part; the new
right part is the current left part xor'ed with that hash of `k` and
the current right part, the new left part is simply the current right
part:

```
next_right = left ^ hash(right, key)
next_left  = right
```

This procedure is repeated for a number of rounds (e.g.,
four). Decryption works essentially the same way by undoing the xor
operations.

{% endcomment %}

### Pseudorandom permutations

How are we goint to use this block cipher? We will use $$n = 64$$ and
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
permutation of the set of `uint64`s which has $$2^{64}$$ elements.

This permutation is parameterized only by the key `k`. If `k` has `m`
bits, that means we can only produce $$2^m$$ different permutations,
which is vastly fewer than the full number of permutations of the set
of `uint64`s, which is $$(2^{64})!$$, a number that has about $$3.47
\times 10^{20}$$ digits.[^digits] By contrast, the number of atoms in the
universe has about 80 digits! Combinatorics creates large numbers very
fast. The actual fraction of permutations reachable by this scheme is
very close to $$0\%$$.

[^digits]: How do I know that number? It turns out the Log-gamma
    function $$\ln\circ\,\Gamma$$ is a well understood object with a
    fast converging series representation. Since $$\Gamma(n + 1) =
    n!$$ and Python has bignums, we can literally just compute
    `math.lgamma(2**64 + 1)` and convert $$\ln$$ to $$\log_{10}$$.

So what gives? It turns out that even though we only get an absurdly
tiny fraction of all possible permutations this way, there is a result
around such _pseudorandom permutations_ by Luby and Rackoff from 1988
that gives strong cryptographic guarantees (assuming the pseudorandom
hash function we used is strong enough, and we use it correctly, and
we use enough Feistel rounds).

The crytographic setup is that an attacker is given a black box which either
does `encrypt` and `decrypt` Feistel operations _or_ is a "real"
permutation drawn uniformly from all $$2^{64}!$$ permutations, plus
its inverse. The attacker can make $$q$$ "queries" (forward or
backward operations of his choice) against the black box. Afterwards,
the attacker says whether he believes the black box to be of the
Feistel type or the "real" type. The _advantage_ the attacker gained
from doing $$q$$ queries is the (absolute value of the) difference of
the probability of saying "real" if it is actually Feistel and the
probability of saying "real" if it is in fact real. If the attacker
learned nothing, the advantage is zero; if he can always tell the
difference, it is one. The Luby-Rackoff result is that the advantage
of the best attacker is bounded by rougly

$$\frac{q^2}{2^{d/2}} + \varepsilon_h$$

where $$d = 64$$ is the block size and $$\varepsilon_h$$ is the best
distinguishing advantage against the underlying pseudorandom hash
function at comparable resources.

In essence, this means a cryptographic attacker requires thousands of
dedicated probes to tell the two cases apart. For our simple
statistical purpose, the permutation looks close enough to having been
chosen truly at random.
