"""
* Assignment: Function Arguments Divide
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. Define function `divide`
    2. Function takes two arguments
    3. Function returns result of the division of both arguments
    4. If division cannot be made, raise `ValueError` with
       "Argument `b` cannot be zero"
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `divide`
    2. Funkcja przyjmuje dwa argumenty
    3. Funkcja zwraca wynik dzielenia dwóch argumentów
    4. Jeżeli nie można podzielić, podnieś `ValueError` z
       "Argument `b` cannot be zero"
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(divide)
    True
    >>> divide(4, 0)
    Traceback (most recent call last):
    ValueError: Argument `b` cannot be zero
    >>> divide(4, 2)
    2.0
"""
