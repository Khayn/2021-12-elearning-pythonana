"""
* Assignment: Function Parameters Sequence
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Define function `total`
    2. Function parameter is `data` sequence of integers
    3. Function returns sum of all values in sequence
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `total`
    2. Parametrem do funkcji jest `data` sekwencja liczb
    3. Funkcja zwraca sumę wszystkich wartości z sekwencji
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `sum()`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(total)
    True
    >>> type(total([0, 1])) is int
    True
    >>> type(total([0.0, 1.1])) is float
    True
    >>> total([1,2,3])
    6
    >>> total([1,2,3,4,5,6])
    21
    >>> total(range(0,101))
    5050
"""
