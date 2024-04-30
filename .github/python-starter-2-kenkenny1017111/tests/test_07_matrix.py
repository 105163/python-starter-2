import numpy as np
import pytest
from conftest import assert_has_function, optional, skip_if_no_function

import task07_matrix as task


@pytest.fixture
def integer_matrices():
    def setup(a, sq=0, sym=0, skew=0, up=0, low=0, diag=0, scalar=0, one=0, zero=0):
        return (
            np.array(a),
            {
                "square": bool(sq),
                "symmetric": bool(sym),
                "skew": bool(skew),
                "upper": bool(up),
                "lower": bool(low),
                "diagonal": bool(diag),
                "scalar": bool(scalar),
                "one": bool(one),
                "zero": bool(zero),
            },
        )

    return [
        setup([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 0, 0, 0, 0, 0, 0, 0, 0),
        setup([[1, 2, 3], [2, 4, 5], [3, 5, 6]], 1, 1, 0, 0, 0, 0, 0, 0, 0),
        setup([[0, 2, -3], [-2, 0, 5], [3, -5, 0]], 1, 0, 1, 0, 0, 0, 0, 0, 0),
        setup([[1, 2, 3], [0, 4, 5], [0, 0, 6]], 1, 0, 0, 1, 0, 0, 0, 0, 0),
        setup([[1, 0, 0], [2, 4, 0], [3, 5, 6]], 1, 0, 0, 0, 1, 0, 0, 0, 0),
        setup([[9, 0, 0], [0, 9, 0], [0, 0, 9]], 1, 1, 0, 1, 1, 1, 1, 0, 0),
        setup([[1, 0, 0], [0, 4, 0], [0, 0, 6]], 1, 1, 0, 1, 1, 1, 0, 0, 0),
        setup([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1, 1, 0, 1, 1, 1, 0, 0, 0),
        setup([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 1, 1, 0, 1, 1, 1, 1, 1, 0),
        setup([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 1, 1, 1, 1, 1, 1, 1, 0, 1),
        setup([[1, 0], [0, 1]], 1, 1, 0, 1, 1, 1, 1, 1, 0),
        setup([[0, 0], [0, 0]], 1, 1, 1, 1, 1, 1, 1, 0, 1),
        setup([[8]], 1, 1, 0, 1, 1, 1, 1, 0, 0),
        setup([[1]], 1, 1, 0, 1, 1, 1, 1, 1, 0),
        setup([[0]], 1, 1, 1, 1, 1, 1, 1, 0, 1),
        setup([[1, 2, 3, 4], [5, 6, 7, 8]]),
        setup([[1, 2, 3, 4]]),
        setup([[1], [2], [3], [4]]),
        setup([[0, 0], [0, 0], [0, 0]], zero=1),
        setup([[0, 0, 0, 0]], zero=1),
    ]


def test_is_square(integer_matrices):
    assert_has_function(task, "is_square")
    for m, property in integer_matrices:
        actual = task.is_square(m)
        assert not isinstance(actual, str), 'return True/False, not "True"/"False"'
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["square"]


def test_is_symmetric(integer_matrices):
    assert_has_function(task, "is_symmetric")
    for m, property in integer_matrices:
        actual = task.is_symmetric(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["symmetric"]


def test_is_skew_symmetric(integer_matrices):
    assert_has_function(task, "is_skew_symmetric")
    for m, property in integer_matrices:
        actual = task.is_skew_symmetric(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["skew"]


def test_is_upper_triangular(integer_matrices):
    assert_has_function(task, "is_upper_triangular")
    for m, property in integer_matrices:
        actual = task.is_upper_triangular(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["upper"]


def test_is_lower_triangular(integer_matrices):
    assert_has_function(task, "is_lower_triangular")
    for m, property in integer_matrices:
        actual = task.is_lower_triangular(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["lower"]


def test_is_diagonal(integer_matrices):
    assert_has_function(task, "is_diagonal")
    for m, property in integer_matrices:
        actual = task.is_diagonal(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["diagonal"]


@optional
def test_is_scalar_matrix(integer_matrices):
    skip_if_no_function(task, "is_scalar_matrix")
    for m, property in integer_matrices:
        actual = task.is_scalar_matrix(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["scalar"]


@optional
def test_is_identity_matrix(integer_matrices):
    skip_if_no_function(task, "is_identity_matrix")
    for m, property in integer_matrices:
        actual = task.is_identity_matrix(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["one"]


@optional
def test_is_zero_matrix(integer_matrices):
    skip_if_no_function(task, "is_zero_matrix")
    for m, property in integer_matrices:
        actual = task.is_zero_matrix(m)
        assert isinstance(actual, bool), "result must be a bool"
        assert actual == property["zero"]


@optional
def test_is_idempotent():
    skip_if_no_function(task, "is_idempotent")
    assert task.is_idempotent(np.array([[1, 2], [3, 4]])) is False
    assert task.is_idempotent(np.array([[0, 0], [0, 0]])) is True
    assert task.is_idempotent(np.array([[1, 0], [0, 0]])) is True
    assert task.is_idempotent(np.array([[3, -6], [1, -2]])) is True
    assert task.is_idempotent(np.array([[0, 1], [0, 0]])) is False
    assert task.is_idempotent(np.array([[0, 0, 0], [0, 0, 0]])) is False
    assert task.is_idempotent(np.array([[0, 0, 0]])) is False
    assert task.is_idempotent(np.array([[0]])) is True
    assert task.is_idempotent(np.array([[1]])) is True
    assert task.is_idempotent(np.array([[-1]])) is False


@optional
def test_is_nilpotent():
    skip_if_no_function(task, "is_nilpotent")
    assert task.is_nilpotent(np.array([[1, 2], [3, 4]])) is False
    assert task.is_nilpotent(np.array([[0, 0], [0, 0]])) is True
    assert task.is_nilpotent(np.array([[1, 0], [0, 0]])) is False
    assert task.is_nilpotent(np.array([[0, 1], [0, 0]])) is True
    assert task.is_nilpotent(np.array([[0, 0, 0], [0, 0, 0]])) is False
    assert task.is_nilpotent(np.array([[0, 0, 0]])) is False
    assert task.is_nilpotent(np.array([[0]])) is True
    assert task.is_nilpotent(np.array([[1]])) is False
    assert task.is_nilpotent(np.array([[-1]])) is False

    # advanced examples
    n3 = [[2, 2, -2], [5, 1, -3], [1, 5, -3]]
    n5 = [
        [2, 2, 2, 2, -4],
        [7, 1, 1, 1, -5],
        [1, 7, 1, 1, -5],
        [1, 1, 7, 1, -5],
        [1, 1, 1, 7, -5],
    ]
    assert task.is_nilpotent(np.array(n3)) is True
    assert task.is_nilpotent(np.array(n5)) is True


def test_classify_linear_system():
    assert_has_function(task, "classify_linear_system")
    aug = np.array([[1, 2, 3], [4, 5, 6]])
    actual = task.classify_linear_system(aug)
    expected = "unique"
    assert isinstance(actual, str), "result must be a string"
    assert actual in ["unique", "many", "none"], 'return "unique", "many", or "none"'
    assert actual == expected

    assert task.classify_linear_system(np.array([[1, 2, 3], [2, 4, 9]])) == "none"
    assert task.classify_linear_system(np.array([[1, 2, 3], [2, 4, 6]])) == "many"


def test_classify_linear_system_advanced():
    assert_has_function(task, "classify_linear_system")
    examples_many = [
        [[0, 0]],
        [[0, 0, 0], [0, 0, 0]],
        [[1, 2, 3], [2, 4, 6], [3, 6, 9]],
        [[1, 2, 3, 4], [-1, -2, -3, -4], [2, 2, 1, 0]],
        [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15], [0, 0, 0, 1, 1]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
    ]
    examples_unique = [
        [[1, 4]],
        [[1, 4], [2, 8]],
        [[1, 2, 3], [2, 4, 6], [3, 6, 2]],
        [[1, 2, 3, 4], [0, 0, 1, 3], [2, 2, 1, 0]],
    ]
    examples_none = [
        [[0, 1]],
        [[1, 0], [2, 1]],
        [[1, 2, 3], [3, 3, 6], [2, 1, 2]],
        [[1, 1, 2, 4], [2, 1, 3, 2], [1, 2, 1, 5], [1, 1, 1, 2]],
    ]
    for i in examples_many:
        assert task.classify_linear_system(np.array(i)) == "many"
    for i in examples_unique:
        assert task.classify_linear_system(np.array(i)) == "unique"
    for i in examples_none:
        assert task.classify_linear_system(np.array(i)) == "none"
