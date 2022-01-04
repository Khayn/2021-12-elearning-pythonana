"""
* Assignment: Loop Unpacking Months
* Required: yes
* Complexity: easy
* Lines of code: 2 lines
* Time: 5 min

English:
    1. Use `enumerate()` to convert `MONTH` into `result: dict[int,str]`:
        a. Keys: month number
        b. Values: month name
    2. Run doctests - all must succeed

Polish:
    1. Użyj `enumerate()` do konwersji `MONTH` w `result: dict[int,str]`:
        a. klucz: numer miesiąca
        b. wartość: nazwa miesiąca
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> assert all(type(x) is int for x in result.keys())
    >>> assert all(type(x) is str for x in result.values())
    >>> assert all(x in result.keys() for x in range(1, 13))
    >>> assert all(x in result.values() for x in MONTHS)

    >>> 13 not in result
    True
    >>> 0 not in result
    True

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {1: 'January',
     2: 'February',
     3: 'March',
     4: 'April',
     5: 'May',
     6: 'June',
     7: 'July',
     8: 'August',
     9: 'September',
     10: 'October',
     11: 'November',
     12: 'December'}
"""

MONTHS = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August', 'September',
          'October', 'November', 'December']

# dict[int,str]: dict with month number and name. Start with 1
result = {}

for count, numMonth in enumerate(MONTHS, start=1):
    result[count] = numMonth

print(result)