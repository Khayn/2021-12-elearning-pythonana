"""
* Assignment: Function Lambda Chain
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Inline functions `odd()` and `cube()` with `lambda` expressions
    2. Run doctests - all must succeed

Polish:
    1. Wciel kod `odd()` i `cube()` wykorzystując wyrażenia `lambda`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `mean = sum(...) / len(...)`
    * type cast to `list()` before calculating mean to expand generator

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is float
    True
    >>> result
    11502.0
"""


def odd(x):
    return x % 2


def cube(x):
    return x ** 3


numbers = (x for x in range(1, 34) if x % 3 == 0)
# numbers = filter(odd, numbers)
numbers = filter(lambda x: x % 2, numbers)
# numbers = map(cube, numbers)
numbers = map(lambda x: x**3, numbers)
numbers = list(numbers)
result = sum(numbers) / len(numbers)
