# Task 06: NumPy

Open `task06_numpy.py` and edit the file to do the following tasks.

You may open this file on GitHub so that equations are shown properly.

## NumPy and SciPy

This task requires you to use NumPy (and SciPy in future tasks). If you haven't installed them, please refer to the [README.md](/README.md) file.

## Software design

When starting a project, it's crucial to establish the conventions you'll use throughout.
In this lecture, angles are assumed to be in radians unless stated otherwise, aligning with Python's `math.sin` function.
So, functions dealing with angles in degrees must include `_degree` in their names, while other functions must not handle degrees.

Deciding on conventions **before beginning coding** (software design) is essential.
It ensures consistency and clarity throughout the project, preventing confusion and streamlining development.

This is a summary of the convention we will use:

- Degrees are presumably in radians.
- Points and vectors are represented as tuples. `(3, 1)` is a point in 2d space. `(0, 0, 0)` is the origin in 3d.
- These tuples are presumably in Cartesian coordinates. Tuples should not be used for representation in polar coordinates.
- 2d polar coordinates are given by $x = r \cos\theta$ and $y = r \sin\theta$.
- 3d polar coordinates are given by $x = r \sin\theta \cos\phi$, $y = r \sin\theta \sin\phi$, and $z = r \cos\theta$.

## Task 06a

Complete two function `rotation_matrix_2d(theta)` and `rotation_matrix_2d_degree(deg)`, which should give rotation matrices in 2d (see Problem 7.2.30 of the textbook).

The function `rotation_matrix(theta)` should return a 2x2 NumPy array representing the rotation matrix for the angle `theta` in **radians**.
Meanwhile, `rotation_matrix_degree(degree)` should return a 2x2 NumPy array representing the rotation matrix for the angle `degree` in **radians**.

- Input: `theta` or `degree` (float)
- Output: a 2x2 NumPy array

(Hint: Google `degree radian python` before you code.)

## Task 06b

We are going to use **tuples** to represent vectors and points. Complete a function `distance(p1, p2)` that returns the distance between two points `p1` and `p2`.

- Input: `p1` and `p2` are tuples of two floats. Namely, `(x1, y1)` and `(x2, y2)`.
- Output: a float representing the distance between `p` and `q`.

## Task 06c

Write a function `rotate(p, theta)` that rotates a point `p` around the origin by `theta` and returns its new coordinates after the rotation.

You should use `rotation_matrix(theta)` above. Also you are asked to convert `p` into a NumPy 1x2 array, rotate it by the matrix, and convert it back to a tuple.

- Input: `p` is a tuple of two floats. `theta` is the rotation angle in radians.
- Output: a tuple `(x, y)` of two floats.

## Task 06d (optional)

Rotations in 3d are surprisingly complicated than in 2d. Here we will use a convention using roll-pitch-yaw angles.

With yaw (`alpha`), pitch (`beta`), and roll (`gamma`), the rotation matrix is given by

![Rotation matrix in yaw-pitch-roll](/misc/rotation_matrix.png)

Write a function `rotation_matrix_3d(alpha, beta, gamma)` that returns a 3x3 NumPy array representing this matrix.

- Input: `alpha`, `beta`, `gamma` (float), representing yaw, pitch, and roll in radians.
- Output: a 3x3 NumPy array
