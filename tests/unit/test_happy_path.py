import pytest


def test_happy_path():
    assert 1 == 1


def add(a: int, b: int) -> int:
    return a + b


@pytest.mark.parametrize("a, b, output", [(1, 1, 2), (2, -2, 0)])
def test_happy_path_failed(a, b, output):
    assert add(a, b) == output
