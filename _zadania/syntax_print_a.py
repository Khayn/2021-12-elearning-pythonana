"""
* Assignment: Syntax Print Newline
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. Define `result` with text 'Hello World'
    2. 'Hello' must be in a first line
    3. 'World' must be in a second line
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj zmienną `result` z tekstem 'Hello World'
    2. 'Hello' ma być w pierwszej linii
    3. 'World' ma być w drugiej linii
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Either quotes (") or apostrophes (') will work

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> 'Hello' in result
    True
    >>> '\\n' in result
    True
    >>> 'World' in result
    True
"""

# str: with Hello and World in separate lines
result = ...
