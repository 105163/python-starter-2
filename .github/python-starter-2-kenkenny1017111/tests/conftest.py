import re
from types import ModuleType
from typing import Any, List

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--optional",
        action="store_true",
        default=False,
        help="Run tests for optional assignments",
    )


optional = pytest.mark.skipif(
    "not config.getoption('--optional')",
    reason="optional; run when --optional is given",
)


def remove_trailing(text: str) -> str:
    # Remove trailing spaces of each line and trailing \n of the whole text.
    text = re.sub(r"\s$", "", text.rstrip(), flags=re.M)
    return text


def strip_all_lines(text: str) -> List[str]:
    return [line.strip() for line in text.strip().splitlines()]


def has_function(module: ModuleType, name: str) -> Any:
    # Return a callable function if exists
    if hasattr(module, name):
        f = getattr(module, name)
        if callable(f):
            return f
    return None


def assert_has_function(module: ModuleType, name: str) -> None:
    assert has_function(module, name), f"Function {name} not implemented."


def skip_if_no_function(module: ModuleType, name: str) -> Any:
    if not has_function(module, name):
        pytest.skip("Function {name} not implemented.")


""" def run_function(module: ModuleType, name: str, *args, **kwargs) -> Any:
    if not (f := has_function(module, name)):
        assert False, f"Function {name} not implemented."
    return f(*args, **kwargs)


def run_function_if_exists(module: ModuleType, name: str, *args, **kwargs) -> Any:

    # Return a callable function if exists
    if f := has_function(module, name):
        return f(*args, **kwargs)
    assert False, f"function {name} not found"
    return None
 """
