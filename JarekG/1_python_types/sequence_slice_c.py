"""
* Assignment: Sequence Slice Sequence
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 3 min

English:
    1. Create set `result` with every second element from `a` and `b`
    2. Run doctests - all must succeed

Polish:
    1. Stwórz zbiór `result` z co drugim elementem `a` i `b`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is set, \
    'Variable `result` has invalid type, should be set'

    >>> result
    {0, 2, 4}
"""

a = (0, 1, 2, 3)
b = [2, 3, 4, 5]

# set[int]: with every second element from `a` and `b`
result = set(a)
result.update(set(b))
result = {x for x in result if x % 2 == 0}

