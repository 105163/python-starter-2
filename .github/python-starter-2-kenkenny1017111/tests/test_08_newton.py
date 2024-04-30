import numpy as np
import pytest
from conftest import assert_has_function, optional, skip_if_no_function

import task08_newton as task

import random
import math


def test_fixed_point_iteration():
    def g_example1(x):
        return (x * x + 1) / 3

    assert_has_function(task, "fixed_point_iteration")
    param1 = (g_example1, 1, 5)
    actual = task.fixed_point_iteration(*param1)
    expected = [1, 0.66666667, 0.48148148, 0.41060814, 0.38953301, 0.38391199]
    assert isinstance(actual, list), "result must be a list"
    assert len(actual) == 6, "result must contain (n+1) elements, not n."
    assert actual[0] == param1[1], "result must start with the initial value x0"
    assert actual == pytest.approx(expected)

    param1 = (g_example1, 2, 4)
    actual = task.fixed_point_iteration(*param1)
    expected = [2, 1.66666667, 1.25925926, 0.86191129, 0.58096369]
    assert actual == pytest.approx(expected)


def test_fixed_point_iteration_another_function():
    def g_example2(x):
        return 1 / (x * x + 1)

    assert_has_function(task, "fixed_point_iteration")
    actual = task.fixed_point_iteration(g_example2, 1, 100)
    assert isinstance(actual, list), "result must be a list"
    assert len(actual) == 101, "result must contain (n+1) elements, not n."
    assert actual[0:5] == pytest.approx([1, 0.5, 0.8, 0.60975610, 0.72896791])
    assert actual[100] == pytest.approx(0.68232780)


def test_newton():
    def f_sqrt(k):
        return (lambda x: x * x - k, lambda x: 2 * x)

    def f_cubic(a, b, c):
        return (lambda x: ((x + a) * x + b) * x + c, lambda x: (3 * x + 2 * a) * x + b)

    assert_has_function(task, "newton")

    # square root
    x0 = 0.5  # should work
    assert task.newton(*f_sqrt(9), x0) == pytest.approx(3)
    assert task.newton(*f_sqrt(1), x0) == pytest.approx(1)
    assert task.newton(*f_sqrt(1e-8), x0) == pytest.approx(1e-4)
    assert task.newton(*f_sqrt(1e8), x0) == pytest.approx(1e4)
    assert task.newton(*f_sqrt(5), x0) == pytest.approx(math.sqrt(5))
    for _ in range(10):
        n = random.randint(100, 1000)
        assert task.newton(*f_sqrt(n), 0.5) == pytest.approx(math.sqrt(n))

    f = f_cubic(0, 2, 2)  # x^3 = 2x + 2 = 0
    actual = task.newton(*f, -1.6)
    expected = -0.77091700
    assert actual == pytest.approx(expected)

    f = f_cubic(0, -2, 2)  # x^3 - 2x + 2 = 0
    actual = task.newton(*f, -1.6)
    expected = -1.76929235
    assert actual == pytest.approx(expected)
