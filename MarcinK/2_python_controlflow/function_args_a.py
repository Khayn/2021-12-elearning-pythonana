"""
* Assignment: Function Arguments Sequence
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function which takes sequence of integers as an argument
    2. Sum only even numbers
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję biorącą sekwencję liczb całkowitych jako argument
    2. Zsumuj tylko parzyste liczby
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(total)
    True
    >>> total([1,2,3,4])
    6
    >>> total([2,-1,0,2])
    4
    >>> total(range(0,101))
    2550
"""


def total(sekwencja):
    return sum(x for x in sekwencja if x % 2 == 0)
