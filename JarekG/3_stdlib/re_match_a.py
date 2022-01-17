"""
* Assignment: RE Match Phones
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Use regular expressions to validate phone numbers
    2. Valid phone number format: `+## ### ### ###` or `+## ## ### ####`
    3. Run doctests - all must succeed

Polish:
    1. Użyj wyrażeń regularnych do walidacji numeru telefonu
    2. Poprawne format numeru: `+## ### ### ###` lub `+## ## ### ####`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * Use f-string formatting to combine both formats
    * Use alternative `|` inside of round brackets `(...|...)`
    * Use begining `^` and end `$` of a line

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> def is_valid_phone(number):
    ...     if re.match(result, number):
    ...         return True
    ...     else:
    ...         return False

    >>> is_valid_phone('+48 (12) 355 5678')
    False
    >>> is_valid_phone('+48 123 555 678')
    True
    >>> is_valid_phone('123 555 678')
    False
    >>> is_valid_phone('+48 12 355 5678')
    True
    >>> is_valid_phone('+48 123-555-678')
    False
    >>> is_valid_phone('+48 123 555 6789')
    False
    >>> is_valid_phone('+1 (123) 555-6789')
    False
    >>> is_valid_phone('+1 (123).555.6789')
    False
    >>> is_valid_phone('+1 800-python')
    False
    >>> is_valid_phone('+48123555678')
    False
    >>> is_valid_phone('+48 123 555 678 wew. 1337')
    False
    >>> is_valid_phone('+48 123555678,1')
    False
    >>> is_valid_phone('+48 123555678,1,2,3')
    False
"""

import re


# str: pattern matching `+## ### ### ###`
cell = r'^\+\d{2}( \d{3}){3}$'

# str: pattern matching `+## ## ### ####`
work = r'^\+(\d{2} ){2}\d{3} \d{4}$'

# str: combination of `+## ### ### ###` and `+## ## ### ####`
result = rf'{cell}|{work}'
