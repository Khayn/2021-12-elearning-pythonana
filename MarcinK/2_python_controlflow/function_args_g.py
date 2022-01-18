"""
* Assignment: Function Arguments Range
* Required: no
* Complexity: medium
* Lines of code: 7 lines
* Time: 13 min

English:
    1. Define function `myrange` with parameters: `start`, `stop`, `step`
    2. Write own implementation of a built-in function
       `myrange(start, stop, step)`
    3. Do not use built-in `range()` function
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj funkcję `myrange` z parametrami: `start`, `stop`, `step`
    2. Zaimplementuj własne rozwiązanie wbudowanej funkcji
       `myrange(start, stop, step)`
    3. Nie używaj wbudowanej funkcji `range()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `while`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> assert isfunction(myrange)

    >>> myrange(0, 10, 2)
    [0, 2, 4, 6, 8]

    >>> myrange(0, 5)
    [0, 1, 2, 3, 4]
"""

def myrange(start, stop, step = 1):

    mySequence = []
    while start < stop:
        mySequence.append(start)
        start += step
    return mySequence