# Task 08: Newton Method

In Section 19.2 of Kreyszig, methods for numerical calculations are introduced.
First, see (!= read) that section. You will find a few examples. It is important to implement them when you read the textbook.

So, open `task08_newton.py` and edit the file to do the following tasks.

(These tasks will probably be a part of the "real" coding assignments after the midterm exam.)

## Task 08a

Example 1 demonstrates an iterative method for calculating solutions of $x^2 - 3x + 1 = 0$.

The textbook says that this equation can be solved by Eq. (4a) and shows a sequence `1.0, 0.667, 0.481, 0.411, 0.390, ...`.
So, let us reproduce this sequence.

Complete the function `fixed_point_iteration(g, x0, n)` and reproduce the sequences in Example 1.
Namely, the following code should print-out `[1.0, 0.6666666666666666, 0.48148148148148145]`.

```python
def g(x):
    return (x * x + 1) / 3

print(fixed_point_iteration(g, 1.0, 2))
```

- Input:
  - `g` is a function that receives a float and returns a float. *Yes, we can assign not only a number but also a function to a variable!*
  - `x0` is the initial value (float).
  - `n` is the number of iterations (int).
- Output: a list of n+1 floats. The first element is x0. The last element is xn.

## Task 08b

Table 19.1 summarizes the Newton method. According to the table, the method should receive the following inputs:

- a function `f`,
- its derivative `fp` (standing for f prime),
- the initial value `x0`,
- the error tolerance `eps`, annd
- the maximum number of iterations `n`.

and return x_(n+1) if the method converges. If it does not converge, it should stop.

*(Notice again that we can assign a function to a variable `f` and pass it to another function `newton`.)*

Now, let us implement the Newton method, starting from the skeleton `newton(f, fp, x0, eps=1e-7, n=100000)` in the file.
Our function should return the solution (if converges) or `None` (if it stops).

Namely, according to Example 3, the following code should print out the square-root of 5.

```python
def f0(x):
    return x * x - 5

def f1(x):
    return 2 * x

x0 = 2.0
solution = newton(f0, f1, x0)
print(solution)
```

Complete the function `newton(f, fp, x0, eps=1e-7, n=100000)`, where you need to follow the specification.

- Input: aforementioned `f`, `fp`, `x0` (int/float), `eps` (float), and `n` (int).
- Output: a floating-point number or `None`.

## Task 08c (optional)

Calculate the solution of $x^3 + 2 x + 2 = 0$ (we know it has only one solution) by using your `newton` function.

## Task 08d (optional, advanced)

Calculate the solution of $x^3 - 2 x + 2 = 0$ (we know it has only one solution) by using your `newton` function.

What happens if you use `x0 = 1.0` as the initial value? Describe what happens and explain why.
