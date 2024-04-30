import math
import random

import numpy as np
import pytest
from conftest import assert_has_function, optional, skip_if_no_function
from numpy.testing import assert_allclose

import task06_numpy as task


def test_rotation_matrix_2d():
    assert_has_function(task, "rotation_matrix_2d")

    # zero degree
    r = task.rotation_matrix_2d(0)
    expected = np.array([[1, 0], [0, 1]])
    assert isinstance(r, np.ndarray), "result must be a numpy array"
    assert r.shape == (2, 2), "result must be a 2x2 numpy array"
    assert_allclose(r, expected)

    # pi / 2
    r = task.rotation_matrix_2d(math.pi / 2)
    expected = np.array([[0, -1], [1, 0]])
    assert_allclose(r, expected, err_msg="(radian/degree confusion?)")
    # 30 radians
    r = task.rotation_matrix_2d(30)
    c, s = 0.154251449888, -0.988031624093
    expected = np.array([[c, -s], [s, c]])
    assert_allclose(r, expected, err_msg="(radian/degree confusion?)")

    for i in range(-5, 5):
        r = task.rotation_matrix_2d(30 + 2 * math.pi * i)
        expected = np.array([[c, -s], [s, c]])
        assert_allclose(r, expected)

    # random
    for _ in range(10):
        r = task.rotation_matrix_2d(random.uniform(-10, 10))
        assert r[0, 0] == r[1, 1], "diagonal elements should be equal"
        assert r[0, 1] == pytest.approx(-r[1, 0]), "off-diagonal sum should be zero"


def test_rotation_matrix_2d_degree():
    assert_has_function(task, "rotation_matrix_2d_degree")

    # zero degree
    r = task.rotation_matrix_2d_degree(0)
    expected = np.array([[1, 0], [0, 1]])
    assert isinstance(r, np.ndarray), "result must be a numpy array"
    assert r.shape == (2, 2), "result must be a 2x2 numpy array"
    assert_allclose(r, expected)

    # pi / 2
    r = task.rotation_matrix_2d_degree(math.pi / 2)
    expected = np.array([[0, -1], [1, 0]])
    assert_allclose(r, expected, err_msg="(radian/degree confusion?)")
    # 30 degrees
    r = task.rotation_matrix_2d_degree(30)
    c, s = 0.866025403784, 0.5
    expected = np.array([[c, -s], [s, c]])
    assert_allclose(r, expected, err_msg="(radian/degree confusion?)")

    for i in range(-5, 5):
        r = task.rotation_matrix_2d_degree(30 + 360 * i)
        expected = np.array([[c, -s], [s, c]])
        assert_allclose(r, expected)
    for _ in range(10):
        r = task.rotation_matrix_2d(random.randint(-2000, 2000))
        assert r[0, 0] == r[1, 1], "diagonal elements should be equal"
        assert r[0, 1] == pytest.approx(-r[1, 0]), "off-diagonal sum should be zero"


def test_distance():
    assert_has_function(task, "distance")
    assert task.distance((0, 0), (0, 0)) == pytest.approx(0)
    assert task.distance((9, 2), (9, 2)) == pytest.approx(0)
    assert task.distance((9, 2), (5, -1)) == pytest.approx(5)
    assert task.distance((-1, -1), (2, 3)) == pytest.approx(5)
    assert task.distance((3.121, 5.391), (1.131, -1.234)) == pytest.approx(6.9174218)


def test_rotate():
    assert_has_function(task, "rotate")
    actual = task.rotate((9, 8), 0)  # no rotation
    assert not isinstance(actual, list), "result must be tuple (not a list!)"
    assert isinstance(actual, tuple), "result must be a tuple (not a list!)"
    assert len(actual) == 2, "result must be a tuple with length 2"
    assert actual[0] == pytest.approx(9), "x coordinate must be unchanged for 0 rad"
    assert actual[1] == pytest.approx(8), "y coordinate must be unchanged for 0 rad"

    actual = task.rotate((1, 0), math.pi / 2)
    expected = (0, 1)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])
    actual = task.rotate((1, 0), math.pi / 4)
    expected = (0.707107, 0.707107)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])
    actual = task.rotate((1, 2), math.pi / 2)
    expected = (-2, 1)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])
    actual = task.rotate((1, 2), math.pi)
    expected = (-1, -2)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])
    actual = task.rotate((1, 2), 4 * math.pi)
    expected = (1.0, 2.0)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])
    actual = task.rotate((1.5, 3.2), 0.3)
    expected = (0.48734, 3.50036)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])
    actual = task.rotate((1.5, 3.2), 2.0)
    expected = (-3.53397, 0.0322763)
    assert actual[0] == pytest.approx(expected[0])
    assert actual[1] == pytest.approx(expected[1])


@optional
def test_rotation_matrix_3d():
    skip_if_no_function(task, "rotation_matrix_3d")

    # simplest
    cases = [
        ((0, 0, 0), [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
        ((0, 0, math.pi), [[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
        ((0, math.pi, 0), [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
        ((math.pi, 0, 0), [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
        ((0, math.pi, math.pi), [[-1, 0, 0], [0, -1, 0], [0, 0, 1]]),
        ((math.pi, math.pi, 0), [[1, 0, 0], [0, -1, 0], [0, 0, -1]]),
        ((math.pi, 0, math.pi), [[-1, 0, 0], [0, 1, 0], [0, 0, -1]]),
    ]
    for angles, matrix in cases:
        actual = task.rotation_matrix_3d(*angles)
        expected = np.array(matrix)
        assert isinstance(actual, np.ndarray), "result must be a numpy array"
        assert actual.shape == (3, 3), "result must be a 3x3 numpy array"
        assert_allclose(actual, expected)
    # numerical
    cases = [
        (
            (1, 2, 3),
            [
                [-0.22484510, +0.90238159, -0.36763046],
                [-0.35017549, -0.42691762, -0.83373765],
                [-0.90929743, -0.05872664, +0.41198225],
            ],
        ),
        (
            (-0.5, -1.1, 12.1),
            [
                [+0.39806805, +0.77989872, -0.48301120],
                [-0.21746556, +0.59174233, +0.77624078],
                [+0.89120736, -0.20395835, +0.40515483],
            ],
        ),
    ]
    for angles, matrix in cases:
        actual = task.rotation_matrix_3d(*angles)
        expected = np.array(matrix)
        assert_allclose(actual, expected)
