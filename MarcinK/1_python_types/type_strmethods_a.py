"""
* Assignment: String Methods Splitlines
* Required: no
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Split `DATA` by lines
    2. Run doctests - all must succeed

Polish:
    1. Podziel `DATA` po liniach
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'

    >>> assert len(result) == 3, \
    'Variable `result` length should be 3'

    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'

    >>> line = 'We choose to go to the Moon'
    >>> assert line in result, f'Line "{line}" is not in the result'

    >>> line = 'in this decade and do the other things.'
    >>> assert line in result, f'Line "{line}" is not in the result'

    >>> line = 'Not because they are easy, but because they are hard.'
    >>> assert line in result, f'Line "{line}" is not in the result'
"""

DATA = """We choose to go to the Moon
in this decade and do the other things.
Not because they are easy, but because they are hard."""

# list[str]: with DATA split by lines
result = DATA.split('\n')
