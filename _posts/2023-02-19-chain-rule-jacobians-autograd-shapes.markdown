---
layout: post
title:  "The chain rule, Jacobians, autograd, and shapes"
---

{::options parse_block_html="true" /}

<div class="right">
<cite>&ldquo;Man muss immer umkehren&rdquo;</cite> <br>
-- Carl Gustav Jacob Jacobi[^1]
</div>

[^1]: Did Jacobi actually say that? Googling this is hard because
      [Charlie Munger likes the supposed quote so
      much](https://fs.blog/inversion/).
      However, there's a [1916
      source](https://www.ams.org/journals/bull/1916-23-01/S0002-9904-1916-02863-1/S0002-9904-1916-02863-1.pdf#page=3)
      claiming &ldquo;[t]he great mathematician Jacobi is said to have
      inculcated upon his students the dictum&rdquo;. A [1968 source](https://books.google.de/books?id=pVNR7-6XeCQC&pg=PA1214&lpg=PA1214&dq=%22man+muss+alles+umkehren%22+jacobi&source=bl&ots=MAEDG85f23&sig=ACfU3U1AEZdgV7tqBzSLUxTojqAQLVihuQ&hl=en&sa=X&redir_esc=y#v=onepage&q=%22man%20muss%20alles%20umkehren%22%20jacobi&f=false)
      gives a slightly different version. Perhaps it's a
      matter of <em>invent, always invent</em>.


This is a short explainer about the chain rule and autograd in PyTorch and JAX,
from the perspective of a mathematical user.

<div class="floated centered">
<img src="/img/jacobi.jpeg" alt="Carl Gustav Jacob Jacobi" style="width:200px;" />
<br />
<s>The Joker</s>
Carl Gustav Jacob Jacobi
<div class="small">
(1804 -- 1851)<br>
"Die Haare immer nach hinten kehren"<br>
Image source: <a
href="https://en.wikipedia.org/wiki/Carl_Gustav_Jacob_Jacobi#/media/File:Carl_Jacobi.jpg">Wikipedia</a>
</div>
</div>

There are many, many explanations of this on the web. Many are likely
better than this one. I'll still write my own, which in the spirit of
this blog is meant to be written, not read. I'll also don't focus on
the implementation of the system, just on its observable behavior.

Other, perhaps better sources for the same info are:

  * [A gentle introduction to
    `torch.autograd`](https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html#sphx-glr-beginner-blitz-autograd-tutorial-py)
    from the tutorials at pytorch.org.
  * [Autograd
    mechanics](https://pytorch.org/docs/stable/notes/autograd.html)
    from pytorch.org.
  * Zachary DeVito's excellent [colab with an example implementation
    of reverse-mode
    autodiff](https://colab.research.google.com/drive/1VpeE6UvEPRz9HmsHh1KS0XxXjYu533EC)
    from scratch. I highly recommend studying this one.
  * [The Autodiff
    Cookbook](https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html)
    in the JAX docs. Also very good.

The JAX docs especially are delightfully mathematical. There are many more
sources on the web. I like the more extensive treatment is in [Thomas Frerix's
PhD thesis](https://mediatum.ub.tum.de/doc/1638886/document.pdf#page=25).

Still, let me add my own spin on the issue. One reason is that many
other articles write things like `dL/dOutputs` and `dL/dInputs` and
generallly use a "variable"-based notation that, while entirely
reasonable from an implementation standpoint, would [make Spivak
sad](https://twitter.com/HeinrichKuttler/status/1262337725161771009).

## The chain rule

### One dimensional functions

Given two differentiable functions $$f,g\from\R\to\R$$, the chain rule
says

$$(g\circ f)'(x) = g'(f(x))f'(x)  \where{x\in\R}. \label{eq:cr1}\tag{1}$$

Here, $$(g\circ f)(x) = g(f(x))$$ is the composition, i.e., chained
evaluation of first $$y = f(x)$$, then $$g(y)$$.

### Multidimensional functions

It's one of the wonders of analysis that this rule keeps being correct
for differentiable multidimensional functions $$f\from\R^n\to\R^m$$,
$$g\from\R^m\to\R^k$$, if &ldquo;differentiable&rdquo; is defined
correctly. Skipping over some technicalities, this requires $$f$$ and
$$g$$ to be *totally differentiable* (also called
*Fr&eacute;chet differentiable*), which implies that all components
$$f_j\from\R^n\to\R$$ are partially differentiable; the derivative
$$f'(a)$$ for $$a\in\R^n$$ can then be shown to be equal to the
*Jacobian matrix*

$$f'(a) = J_f(a)
 := \bigl(\partial_k f_j(a)\bigr)_{\substack{j=1,\ldots,m\\ k=1,\ldots,n}}
  = \begin{pmatrix}
      \partial_1 f_1(a) & \cdots & \partial_n f_1(a) \\
      \vdots && \vdots \\
      \partial_1 f_m(a) & \cdots & \partial_n f_m(a)
    \end{pmatrix}
    \in\R^{m\times n}.
$$

The idea is to view $$f(a) = (f_1(a), \ldots, f_m(a))^\top\in\R^m$$
as a column vector and add one column per partial derivative, i.e.,
dimension of its input $$a$$.

With this definition, the multidimensional chain rule reads like its
1D version $$\eqref{eq:cr1}$$,

$$(g\circ f)'(x) = g'(f(x))\cdot f'(x)  \where{x\in\R^n}.  \label{eq:crN}\tag{2}$$

However, in this case this is the matrix multiplication
$$\cdot\from\R^{k\times m}\times\R^{m\times n}\to\R^{k\times n}$$ of
$$J_g(f(x))$$ and $$J_f(x)$$ and their order is important. Jacobi
would have called this *nachdifferenzieren*.

Via the nature of this rule it iterates, i.e. the derivative of the
composition $$h\circ g\circ f$$ is

$$
(h\circ g\circ f)(x)
=
h'(g(f(x)))\cdot g'(f(x))\cdot f'(x)
=
(h'\circ g\circ f)(x)\cdot (g'\circ f)(x)\cdot f'(x),
$$

and likewise for a composition of $$n$$ functions

$$
(f_n\circ \cdots \circ f_1)'(x)
=
(f_n'\circ f_{n-1}\circ\cdots\circ f_1)(x)\cdot
(f_{n-1}'\circ f_{n-2}\circ\cdots\circ f_1)(x)
\,\cdots\,
(f_2'\circ f_1)(x) \cdot f_1'(x).  \label{eq:crNn}\tag{3}
$$

Note that subscripts no longer mean components here, we are talking
about $$n$$ functions, each with multidimensional inputs and outputs.

### Backprop

Now, while matrix multiplication isn't commutative, meaning in general
$$AB \ne BA$$, it is associative: For a product of several matrices
$$ABC$$, it does not matter if one computes $$(AB)C$$ or $$A(BC)$$;
this is what makes the notation $$ABC$$ sensible in the first
place. However, this only means the same output is produced by those
two alternatives. It does not mean the same amount of "work" (or
"compute") went into either case.

Counting scalar operations, a product $$AB$$ with
$$A\in\R^{k\times m}$$ and $$B\in\R^{m\times n}$$ takes $$nkm$$
multiplications and $$nk(m-1)$$ additions, since each entry in the
output matrix is the sum of $$m$$ multiplications. In a chain of
matmuls like $$ABCDEFG\cdots$$, it's clear that some groupings like
$$((AB)(CD))(E(FG))\cdots$$ might be better than others. In
particular, there may well be better and worse ways of computing the
Jacobian $$\eqref{eq:crNn}$$. However, to quote
[Wikipedia](https://en.wikipedia.org/wiki/Automatic_differentiation#Beyond_forward_and_reverse_accumulation):

> The problem of computing a full Jacobian of $$f\from\R^n\to\R^m$$ with a
> minimum number of arithmetic operations is known as the optimal
> Jacobian accumulation (OJA) problem, which is NP-complete.

The good news is that in important special cases, this problem is
easy. In particular, if the first matrix in the product has only one
row, or the last only one column, it makes sense to compute the
product "from the left" or "from the right", respectively. And those
cases are not particularly pathological either, as they correspond to
either the final function $$f_n$$ mapping to a scalar or the whole
composition depending only on a scalar input $$x\in\R$$. The former
case is especially important as that's what happens whenever we
compute the gradients of a scalar *loss function*, such as in bascially all
cases where neural networks are used.[^2]
The corresponding orders of multiplications in the chain rule
$$\eqref{eq:crNn}$$ are known as
*reverse mode* or *forward mode*, respectively. Ignoring some
distinctions not relevant here, reverse mode is also known as
*backpropagation*, or *backprop* for short.

[^2]: To illustrate the extremes this is pushed to for large scale
    cases: A large language model like GPT3 can have billions or even
    trillions of weights (corresponding to the dimension of
    $$x\in\R^n$$) but still computes a scalar (one dimensional) loss.

In this case, the image of $$f_n$$ is one dimensional, and therefore
its Jacobian matrix $$f_n'$$ has only one row -- it's a row
vector. After multiplication with the next Jacobian $$f_{n-1}'$$, this
property is preserved: All matmuls in the chain turn into
*vector-times-matrix*. Specifically, they are
vector-times-Jacobian-matrix, more commonly known as a vector-Jacobian
product, or VJP. To illustrate:

$$
\begin{pmatrix}
  \unicode{x2E3B}
\end{pmatrix}_1
\begin{pmatrix}
  | & | & | \\
  | & | & | \\
  | & | & |
\end{pmatrix}_2
\begin{pmatrix}
  | & | & | \\
  | & | & | \\
  | & | & |
\end{pmatrix}_3
\cdots
\begin{pmatrix}
  | & | & | \\
  | & | & | \\
  | & | & |
\end{pmatrix}_n
=
\begin{pmatrix}
  \unicode{x2E3B}
\end{pmatrix}
\begin{pmatrix}
  | & | & | \\
  | & | & | \\
  | & | & |
\end{pmatrix}_3
\cdots
\begin{pmatrix}
  | & | & | \\
  | & | & | \\
  | & | & |
\end{pmatrix}_n
=
\text{etc.}
$$

What this means is that for neural network applications, a system like
PyTorch or JAX *doesn't need to actually compute* full Jacobians -- all
it needs are vector-Jacobian products. It turns out that
(classic) PyTorch does and can in fact do nothing else.

Also notice that the column vector
$$\begin{pmatrix}\unicode{x2E3B}\end{pmatrix}$$ multiplied from the
left is "output-shaped" from the perspective of the Jacobian it gets
multiplied to. This is the reason `grad_output` in PyTorch always has
the shape of the operation's output and why
[`torch.Tensor.backward`](https://pytorch.org/docs/stable/generated/torch.Tensor.backward.html)
receives an argument described as the "gradient w.r.t. the
tensor".

You may wonder what it means for it to have a specific shape vs just
being a "flat" column vector as it is here. I certainly wondered about
this; the answer is below.


## In PyTorch

Here's a very simple PyTorch example (lifted from
[here](https://medium.com/@monadsblog/pytorch-backward-function-e5e2b7e60140)):

```python
import torch

x = torch.tensor([1.0, 2.0], requires_grad=True)

y = torch.empty(3)
y[0] = x[0] ** 2
y[1] = x[0] ** 2 + 5 * x[1] ** 2
y[2] = 3 * x[1]

v = torch.tensor([1.0, 2.0, 3.0])
y.backward(v)  # VJP.

print("y:", y)
print("x.grad:", x.grad)

# Manual computation.
dydx = torch.tensor(
    [
        [2 * x[0], 0],
        [2 * x[0], 10 * x[1]],
        [0, 3],
    ]
)

assert torch.equal(x.grad, v @ dydx)
```

In PyTorch. `Tensor.backward` computes the backward pass via
vector-Jacobian products. If the tensor in question is a scalar, an
implicit `1` is assumed, otherwise one has to supply a tensor of the
same shape which is used as the vector in the VJP, as in the example
above.

## But wait, tensor or vector?

For the typical mathematian, the term "tensor" for the
multidimensional array in PyTorch and JAX is a bit on an acquired (or
not) taste -- but to be fair, so is anything about the real tensor
product $$\otimes$$ as well.

The situation here seems especially confusing -- the chain rule from
multidimensional calculus makes a specific point of what's a row and
what's a column and treats functions $$\R^n\to\R^m$$ by introducing
$$m\times n$$ matrices. In PyTorch, functions depend on and produce one (or
several) multidimensional "tensors". What gives?

The answer turns out to be relatively simple: The math part of the
backward pass doesn't depend on these tensor shapes in any deep
way. Instead, it does the equivalent of "reshaping" everything into a
vector. Example:

```python
x = torch.tensor(
    [
        [1.0, 2.0],
        [3.0, 4.0],
    ],
    requires_grad=True,
)

y = torch.empty((3, 2))
y[0, 0] = x[0, 0] ** 2
y[1, 0] = x[0, 0] ** 2 + 5 * x[0, 1] ** 2
y[2, 0] = 3 * x[1, 0]
y[0, 1] = x[1, 1]
y[1, 1] = 0
y[2, 1] = torch.sum(x)

v = torch.tensor(
    [
        [1.0, 2.0],
        [3.0, 4.0],
        [5.0, 6.0],
    ]
)

print("y:", y)
y.backward(v)  # VJP.
print("x.grad:", x.grad)
```

What did this even compute? It's the equivalent of reshaping inputs
and outputs to be vectors, then applying the standard calculus from
above:

```python
dydx = torch.tensor(  # y.reshape(-1) x x.reshape(-1) Jacobian matrix.
    [
        [2 * x[0, 0], 0, 0, 0],  # y[0, 0]
        [0, 0, 0, 1],  # y[0, 1]
        [2 * x[0, 0], 10 * x[0, 1], 0, 0],  # y[1, 0]
        [0, 0, 0, 0],  # y[1, 1]
        [0, 0, 3, 0],  # y[2, 0]
        [1, 1, 1, 1],  # y[2, 1]
    ]
)

print("dydx", dydx)
assert torch.equal(
    x.grad,
    (v.reshape(-1) @ dydx).reshape(x.shape),
)
```

To be clear: PyTorch does not actually compute the Jacobian only to
multiply it from the left with this vector, but what it does has the
same output as this less efficient code.

## In JAX

PyTorch is great. But it's not necessarily principled. This tweet
expresses this somewhat more aggressively:

{::options parse_block_html="false" /}

<blockquote class="twitter-tweet tw-align-center"><p lang="en" dir="ltr">The Aesthetician in me wants to be constantly annoyed by how ugly PyTorch is but frankly I’m consistently impressed with how easy it is to develop in.</p>&mdash; Aidan Clark (@_aidan_clark_) <a href="https://twitter.com/_aidan_clark_/status/1568052833030897664?ref_src=twsrc%5Etfw">September 9, 2022</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

JAX is, arguably, different, at least on the first account. It comes
with vector-Jacobian products, Jacobian-vector products, and also the
option to compute full Jacobians if required. I couldn't write up the
details better than the [JAX Autodiff
Cookbook](https://jax.readthedocs.io/en/latest/notebooks/autodiff_cookbook.html)
does, so I won't try. To quote just one relevant portion, adjusted
slightly to our notation:

> The JAX function `vjp` can take a Python function for evaluating $$f$$
> and give us back a Python function for evaluating the VJP $$(x, v)\mapsto(f(x), v^\top f'(x))$$.


## So what does it really do?

For the autodiff details, read either Zachary DeVito's [colab with an
example implementation of what PyTorch does](https://colab.research.google.com/drive/1VpeE6UvEPRz9HmsHh1KS0XxXjYu533EC),
or the JAX Autodiff Cookbook, or ideally both.

But to round things out, let's look at how one defines a "custom
function" with its own forward and backward pass in PyTorch.

We'll take elementwise multiplication as our first example; the fancy
mathematics name of this simple operation is
[*Hadamard
product*](https://en.wikipedia.org/wiki/Hadamard_product_(matrices))
(also known as *Schur product* -- their moto was "*name, always name*"[^3]). We'll
denote it by $$\odot.$$ To fit it within the
standard calculus above, we reinterpret
$$\odot\from\R^n\times\R^n\to\R^n$$ as $$\odot\from\R^{2n}\to\R^n$$, multiplying
the first and second "half" of its single-vector input, i.e.,
$$\R^{2n}\ni x\mapsto\odot(x) = (x_jx_{n+j})_{j=1,\ldots,n}\in\R^n.$$ Its derivative
is

$$
\odot'(x) =
  \begin{pmatrix}
    x_{n+1} &   &   &                & x_1 &   &  &  \\
      & x_{n+2} &   &                &   & x_2 &  &  \\
      &   & {\lower 3pt\smash{\ddots}}   &   &   &  & {\lower 3pt\smash{\ddots}} &  \\
      &   &           & x_{2n}       &   &   &  & x_n
  \end{pmatrix}
  \in\R^{n\times 2n},  \where{x\in\R^{2n}}
$$

where empty cells are zeros. It should be immediately obvious that
there's no need to "materialize" these diagonal Jacobians. In fact,
given a vector $$v = (v_1, \ldots, v_{2n})\in\R^{2n}$$, the VJP here
is just

$$
v\cdot \odot'(x) = (v_1x_{n+1}, \ldots, v_nx_{2n},
v_{n+1}x_1, \ldots, v_{2n}x_n) \in \R^{2n}.
$$

(And that already seems like a needless complication of such a simple
thing als elementwise multiplication!)

[^3]: This is a joke. In reality, mathematians are taught that if
    something is named after someone, that is a good indication that
    person *didn't* invent that.

The PyTorch version of this is ... well,
it's just `x * y`, and PyTorch knows full well how to compute and
differentiate that. But if we wanted for some reason to add this from
scratch, it might look like this:

```python
class HadamardProduct(torch.autograd.Function):
    """Computes lhs * rhs and its backward pass."""
    @staticmethod
    def forward(ctx, lhs, rhs):
        ctx.save_for_backward(lhs, rhs)
        return lhs * rhs

    @staticmethod
    def backward(ctx, grad_output):
        lhs, rhs = ctx.saved_tensors
        grad_lhs = grad_output * rhs
        grad_rhs = grad_output * lhs
        return grad_lhs, grad_rhs

mul = HadamardProduct.apply
```

The `ctx` argument is used to stash the tensors required for the
backward pass somewhere (in Zachary's
[colab](https://colab.research.google.com/drive/1VpeE6UvEPRz9HmsHh1KS0XxXjYu533EC),
this is done via a closure) and the `grad_output` argument is the
output-shaped "vector" of the VJP. It's a single argument in this case
since the function has a single output. PyTorch may reuse this tensor,
so it's important even in cases where the gradient computed has the same
shape to "NEVER modify [this argument] in-place", as the [PyTorch docs
say](https://pytorch.org/docs/stable/notes/extending.html#how-to-use).

Testing this:

```python
lhs = torch.tensor([1.0, 2.0], requires_grad=True)
rhs = torch.tensor([3.0, 4.0], requires_grad=True)

y = mul(lhs, rhs)

print("y =", y)
v = torch.tensor([5.0, 6.0])
y.backward(v)
assert torch.equal(lhs.grad, v * rhs)
assert torch.equal(rhs.grad, v * lhs)
```

This example is typical for elementwise operations, where the
Jacobian matrices are diagonal and VJPs are just elementwise
operations themselves.

To contrast this with another example, let's look at a real, genuine
linear function. Remember that for a matrix $$W\in\R^{m\times n}$$,
the function $$\R^n\ni x \mapsto Wx \in \R^m$$ is Fr&eacute;chet
differentiable an its derivative is the constant $$W$$.[^4] Taking $$x$$
as a constant and $$W=(W_{jk})_{j=1,\ldots,m;\; k=1,\ldots,n}$$ as the "dependent variable", and "reshaping to
vector form" as above, the derivative at $$W$$ is

$$
  \begin{pmatrix}
      x_1 & \cdots & x_n &     &        &     &        &     &        & \\
          &        &     & x_1 & \cdots & x_n &        &     &        & \\
          &        &     &     &        &     & \ddots &     &        & \\
          &        &     &     &        &     &        & x_1 & \cdots & x_n
  \end{pmatrix}
  \in\R^{m\times nm}.
$$

Forming the VJP with a vector $$v\in\R^m$$ and reshaping back to the
shape of $$W$$ results in VJP of $$v\cdot x^\top$$, with entries
$$(v_jx_k)_{j,k}$$.

[^4]: In fact, the underlying idea of the Fr&eacute;chet derivative is linear
      approximations like that, Unlike partial deriviatives, this idea
      carries over to the infinite dimensional case, where it's a stronger
      requirement than weaker notions of differentiability like the
      existence of the [Gateaux derivative](https://en.wikipedia.org/wiki/Gateaux_derivative).

The PyTorch code for that is (cf. the [PyTorch
docs](https://pytorch.org/docs/stable/notes/extending.html#example)):

```python
class ActuallyLinear(torch.autograd.Function):
    @staticmethod
    def forward(ctx, input, weight):
        ctx.save_for_backward(input, weight)
        output = weight @ input
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input, weight = ctx.saved_tensors
        grad_input = grad_weight = None
        # Checks for extra efficiency -- only compute VJP with vector != zero.
        if ctx.needs_input_grad[0]:
            grad_input = grad_output @ weight
        if ctx.needs_input_grad[1]:
            grad_weight = grad_output.unsqueeze(1) @ input.unsqueeze(0)
        return grad_input, grad_weight
```

Testing this:

```python
W = torch.tensor(
    [
        [1.0, 2.0],
        [3.0, 4.0],
        [5.0, 6.0],
    ],
    requires_grad=True,
)

x = torch.tensor([10.0, 11.0], requires_grad=True)
y = ActuallyLinear.apply(x, W)
print("y =", y)
v = torch.tensor([1.0, 2.0, 3.0])
y.backward(v)

# Save for comparing.
x_grad = x.grad
W_grad = W.grad

x.grad = None  # Reset to zero.

torch_linear = torch.nn.Linear(W.shape[1], W.shape[0], bias=False)

# Set weight without touching gradient tape.
torch_linear.weight.data[...] = W
torch_y = torch_linear(x)
torch_y.backward(v)

assert torch.equal(x_grad, x.grad)
assert torch.equal(torch_linear.weight.grad, W_grad)
```


## One final comment

I could go on, but this is plenty for now. The last thing worth
mentioning is that $$\eqref{eq:crNn}$$ doesn't quite fit the actual
situation of deep neural networks, where one takes the gradient of all
weights, and each layer $$f_j$$ depends both on the outputs
("activations") of the previous layer and its own weight, and the
inputs of the first layer $$f_1$$ (and potentially some later layers,
e.g. for "targets") are just "data", which is treated as
a parametrization of the functions. One way to apply the Calculus 102
rule above would be to have earlier layers pass on all weights they
don't need as an identity function (with identity matrix for that part
of its Jacobian). This can also be written in other ways, but the
[`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/margin-bottom)
here is too small to contain it.
