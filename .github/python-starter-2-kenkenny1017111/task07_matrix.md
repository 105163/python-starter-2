# Task 07: Matrix

Open `task07_matrix.py` and edit the file to do the following tasks.

## Task 07a

Section 7.2 of Kreyszig defines several special matrices. We want to make functions to check if a matrix is one of these special matrices. So, complete the following functions.

- `is_square(m)` to check if `m` is square.
- `is_symmetric(m)` to check if `m` is (square and) symmetric.
- `is_skew_symmetric(m)` to check if `m` is (square and) skew-symmetric.
- `is_upper_triangular(m)` to check if `m` is (square and) upper-triangular.
- `is_lower_triangular(m)` to check if `m` is (square and) lower-triangular.
- `is_diagonal(m)` to check if `m` is (square and) diagonal.

All the functions have the same signature:

- Input: `m` is a NumPy 2-dimensional array. *(You can assume all elements are integer.)*
- Output: a bool (`True` or `False`)

You can assume `m` is a NumPy 2d array with at least one element; no need to check it.

Hint: First, have a look at the NumPy manual on [ndarray](https://numpy.org/doc/stable/reference/arrays.ndarray.html) and [ndarray.shape](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.shape.html).

## Task 07b

(This task will be a part of the "real" coding assignments after the midterm exam.)

In Kreyszig Section 7.5., we have learned how we can classify linear systems of equations (Theorem 1).
Let's make a code for this test.

As a linear system of equations is equivalent to an augmented matrix (See Section 7.3), we can use it as the input.
The output can just be a string: `"unique", "many", "none"` to represent how many solutions we have.

Complete the function `classify_linear_system(aug)`.

- Input: `aug` is the augmented matrix of a linear system of equations. It is a 2d NumPy array.
- Output: a string: `"unique"`, `"many"`, or `"none"`.

Hint: You don't have to implement rank calculation. Instead, read [the manual of numpy.linalg](https://numpy.org/doc/stable/reference/routines.linalg.html) very carefully.

## Task 07c (optional)

As a continuation of Task 07a, implement the following functions.

- `is_scalar_matrix(m)` to check if `m` is a scalar matrix.
- `is_identity_matrix(m)` to check if `m` is an identity matrix.
- `is_zero_matrix(m)` to check if `m` is a zero matrix.
- `is_idempotent(m)` to check if `m` is idempotent (Problem 7.2.7).

## Task 07d (optional, advanced)

You can further implement the following function, where you need to derive/find some mathematical theorems.

- `is_nilpotent(m)` to check if `m` is nilpotent (Problem 7.2.8).

## Task 07e (optional, advanced)

Task 07a has a remark *You can assume all elements are integer.* ...but why? Explain.

Furthermore, what happens if you run your code for non-integer matrices? Do they work? Or...?

(This is why, in **real projects**, we **need to** use pre-built codes and **should not** write our own codes. Meanwhile, in lecture courses, you are asked to write your own code so that you know how the pre-built codes are written and what kinds of caveats lie there.)
