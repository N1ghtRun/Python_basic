from functools import cache


@cache
def exponent_multiplication(num1: int | float, num2: int | float, /, *, exponent: int | float) -> int | float:
    result = (num1 * num2) ** exponent
    return result
