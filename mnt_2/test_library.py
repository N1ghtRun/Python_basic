import pytest
from math import sqrt
from library import exponent_multiplication


def test_type_error():
    with pytest.raises(TypeError):
        exponent_multiplication('2', {4}, exponent=[3])


def test_value_error():
    with pytest.raises(ValueError):
        exponent_multiplication(sqrt(-100), 4, exponent=2)


def test_negative_number():
    assert exponent_multiplication(-2, 3, exponent=2) == 36, 'Not expected result'


def test_result_type():
    assert type(exponent_multiplication(2.5, 3, exponent=2)) in (int, float), 'Wrong type of result'
