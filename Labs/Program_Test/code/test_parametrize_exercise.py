from typing import List
from math import isclose
import pytest


def norm(vec: List[float], norm: int):
    return pow(sum(pow(v, norm) for v in vec), 1/norm)


@pytest.mark.parametrize("vec_len", list(range(1, 10)))
@pytest.mark.parametrize("norm_num", list(range(1, 10)))
@pytest.mark.parametrize("val", [1, -1, 2])
def test_norm(vec_len, norm_num, val):
    assert isclose(norm([1] * vec_len, norm_num), abs(val)*pow(vec_len, 1/norm_num)) #nedd to deal with this(abs)
