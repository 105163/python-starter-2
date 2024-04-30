# Task 05: Basic Numerics

Open `task05_basic.py` and edit the file to do the following tasks.

## Task 05a

A function `solve_equation(a, b, c)` should solve the equation $ax^2+bx+c=0$. Fix the code.

- Input: three `int` numbers. From -1000000 to +1000000. All can be zero.
- Output: a `tuple` of two numbers.
  - If a = b = 0, you need to `raise ValueError`.
  - If the equation has only one real solution, the second element should be `None`. For example, `(1, None)` for $x^2-2x+1=0$.
  - If the equation has no real solution, both elements should be `None`$. For example, `(None, None)` for $x^2+1=0$.
  - Otherwise, the first element should be the smaller solution and the second element should be the larger solution.

Notice the difference between tuples and lists.

## Task 05b

The Euler's number [can be obtained by](https://en.wikipedia.org/wiki/E_(mathematical_constant)) the following series:

$$ e = \sum_{n=0}^{\infty} \frac{1}{n!}$$

Namely, `1 + 1 + 1/2 + 1/6 + 1/24 + 1/120 + ....`.

Make a function `calc_e()` to calculate `e` by this method, at least up to 9-th digit `2.718281828`.

## Task 05c (optional)

Rewrite `solve_equation(a, b, c)` (Task 05a) with taking care of the cancellation problem. Now the input values can be float.

## Task 05d (optional)

Rewrite `calc_e()` (Task 05b) to calculate `e` as precise as possible.

## Task 05d (optional, advanced)

This is not a coding problem. Explain how many terms you should sum up to get `e` up to `p`-th digit. Explain what is the optimal choice of `n` for Task 05d under the assumption we use IEEE754 64bit (double precision) floating point numbers.
