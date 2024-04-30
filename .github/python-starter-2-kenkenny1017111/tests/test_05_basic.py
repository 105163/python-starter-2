import math
import random

import pytest
from conftest import assert_has_function, optional, skip_if_no_function

import task05_basic as task


def test_solve_equation_simplest():
    assert_has_function(task, "solve_equation")
    s = task.solve_equation(1, -3, 2)
    assert not isinstance(s, list), "result must be tuple (not a list!)"
    assert isinstance(s, tuple), "result must be a tuple (not a list!)"
    assert len(s) == 2, "result must be a tuple with length 2"
    assert s[0] is not None, "two real solution exists for a=1, b=-3, c=2"
    assert s[1] is not None, "two real solution exists for a=1, b=-3, c=2"
    assert s[0] < s[1], "first solution must be smaller than the second one"
    assert s[0] == 1, "first solution must be 1 for a=1, b=-3, c=2"
    assert s[1] == 2, "first solution must be 2 for a=1, b=-3, c=2"
    for _ in range(10):
        s1 = random.randint(-100, 100)
        s2 = random.randint(-100, 100)
        a = random.randint(-100, 100)
        a = 1 if a == 0 else a
        s2 = s2 + 1 if s1 == s2 else s2
        b = -s1 - s2
        c = s1 * s2
        actual = task.solve_equation(a, -a * (s1 + s2), a * s1 * s2)
        expected = (s1, s2) if s1 < s2 else (s2, s1)
        assert actual == expected, f"got {actual} for a={a}, b={b}, c={c}"


def test_solve_equation_duplication():
    assert_has_function(task, "solve_equation")
    s = task.solve_equation(1, -6, 9)
    assert isinstance(s, tuple), "result must be always a tuple"
    assert len(s) == 2, "result must be always a tuple with length 2"
    assert s[1] is None, "second element must be None for duplicated solutions"
    assert s[0] == 3, "first solution must be 3 for a=1, b=-6, c=9"
    for _ in range(10):
        s1 = random.randint(-100, 100)
        a = random.randint(-100, 100)
        a = 1 if a == 0 else a
        actual = task.solve_equation(a, -2 * a * s1, a * s1 * s1)
        expected = (s1, None)
        assert actual == expected, f"got {actual} for (x-a)^2 = 0"


def test_solve_equation_imaginary():
    assert_has_function(task, "solve_equation")
    s = task.solve_equation(1, 0, 1)
    assert isinstance(s, tuple), "result must be always a tuple"
    assert len(s) == 2, "result must be always a tuple with length 2"
    assert s == (None, None), "both solutions must be none for a=1, b=0, c=1"
    for _ in range(10):
        a = random.randint(-1000, 1000)
        a = 1 if a == 0 else a
        b = random.randint(-1000, 1000)
        c = int(b * b / 4 / a) + (3 if a > 0 else -3)
        actual = task.solve_equation(a, b, c)
        expected = (None, None)
        assert actual == expected, f"got {actual} for a={a}, b={b}, c={c}"


def test_solve_equation_zero_a():
    assert_has_function(task, "solve_equation")
    s = task.solve_equation(0, 1, 1)
    assert isinstance(s, tuple), "result must be always a tuple"
    assert len(s) == 2, "result must be always a tuple with length 2"
    assert s[1] is None, "second element must be None if only one solution"
    assert s == (-1, None), f"got {s} for a=0, b=1, c=1 (x+1=0)"
    for _ in range(10):
        a = 0
        b = random.randint(1, 1000000) * random.choice([-1, 1])
        c = random.randint(1, 1000000) * random.choice([-1, 1])
        actual = task.solve_equation(a, b, c)
        assert actual[1] is None, f"got {actual} for a={a}, b={b}, c={c}"
        assert actual[0] == pytest.approx(-c / b), f"got {actual} for {a},{b},{c}"


def test_solve_equation_raise():
    assert_has_function(task, "solve_equation")
    for i in [0, 1, -1, 30, -200]:
        with pytest.raises(ValueError):
            task.solve_equation(0, 0, i), f"a=0, b=0, c={i} should raise ValueError"


def test_calc_e():
    assert_has_function(task, "calc_e")
    actual = task.calc_e()
    assert isinstance(actual, float), "result must be a number (float)"
    actual_string = str(actual)
    assert actual_string[0:3] == "2.7", "it should start with 2.7"
    assert actual_string[0:11] == "2.718281828", "not match to e upto 9th digit"


@optional
def test_solve_equation_very_precise():
    skip_if_no_function(task, "solve_equation")
    a = 1
    c = 1
    s2 = 100000
    s1 = c / s2
    b = -(s1 + s2)
    expected = (s1, s2)
    actual = task.solve_equation(a, b, c)
    assert (
        actual == expected
    ), f"got {actual} for a=c=1, b={b}; too big error from expected {expected}"
    for _ in range(10):
        a = 1
        c = random.randint(1, 100) / 1000
        s1 = random.randint(10000, 1000000) * random.choice([-1, 1])
        s2 = c / s1
        b = -(s1 + s2)
        expected = (s1, s2) if s1 < s2 else (s2, s1)
        actual = task.solve_equation(a, b, c)
        assert actual == expected, f"got {actual} for a=c=1, b={b}; expected {expected}"


@optional
def test_calc_e_very_precise():
    skip_if_no_function(task, "calc_e")
    actual = task.calc_e()
    e0 = 2.71828182845904464  # 2.71828182845904464
    e1 = math.nextafter(e0, 3)  # 2.71828182845904509  # e=904523; closest
    e2 = math.nextafter(e1, 3)  # 2.71828182845904553
    e3 = math.nextafter(e2, 3)  # 2.71828182845904597

    actual_string = str(actual)
    assert actual_string[0:16] == "2.71828182845904", "not match to e upto 14th digit"
    assert e0 < actual < e3, f"expected {e0} < e < {e3}, got {actual}"
    assert actual != e2, "very very close but not the best precise value"
    assert actual == e1
