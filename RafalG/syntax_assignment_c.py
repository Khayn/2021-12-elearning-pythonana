"""
* Assignment: Syntax Variables Str
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with text 'Hello World'
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z tekstem 'Hello World'
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Either quotes (") or apostrophes (') will work

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> assert result == 'Hello World', \
    'Variable `result` has invalid value, should be "Hello World"'
"""

# str: with Hello and World
result = "Hello World"
