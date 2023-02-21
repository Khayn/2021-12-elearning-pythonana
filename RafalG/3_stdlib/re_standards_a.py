"""
* Assignment: RE Standards PESEL
* Complexity: medium
* Lines of code: 0 lines
* Time: 5 min
* Warning: Do no write any code - **discussion only**

English:
    TODO: English Translation
    X. Run doctests - all must succeed

Polish:
    1. Napisz implementację `is_pesel_valid`
       a. Temat walidacji Pesel jest zbyt trudny dla Regex
       b. W tej funkcji użujemy prostego sprawdzenia r'^\d{11}$'
       c. Już tylko taki kawałek kodu pozwoli na uniknięcie 80% błędów
    2. Napisz implementację `is_pesel_woman`
       a. Pesel należy do kobiety, jeżeli przed ostatnia cyfra jest parzysta
       a. Nie korzystaj z regex
    3. Uruchom doctesty - wszystkie muszą się powieść

Discuss:
    * nie pisz kodu, przeprowadź tylko dyskusję
    * Co to jest suma kontrolna?
    * Mając PESEL "69072101234"
       a. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
       b. Jakie wyrażenie może być na drugim miejscu w PESEL?
       c. Jakie wyrażenie może być na trzecim miejscu w PESEL?
       d. Jakie wyrażenie może być na czwartym miejscu w PESEL?
       e. Jakie wyrażenie może być na piątym miejscu w PESEL?
       f. Jakie wyrażenie może być na szóstym miejscu w PESEL?
    * Mając PESEL "18220812345"
       a. Jakie wyrażenie może być na pierwszym miejscu w PESEL?
       b. Jakie wyrażenie może być na drugim miejscu w PESEL?
       c. Jakie wyrażenie może być na trzecim miejscu w PESEL?
       d. Jakie wyrażenie może być na czwartym miejscu w PESEL?
       e. Jakie wyrażenie może być na piątym miejscu w PESEL?
       f. Jakie wyrażenie może być na szóstym miejscu w PESEL?

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> is_pesel_valid('69072101234')
    True
    >>> is_pesel_valid('18220812345')
    True
    >>> is_pesel_woman('69072101234')
    False
    >>> is_pesel_woman('18220812345')
    True
"""

import re

PATTERN = r'^\d{11}$'


def is_pesel_valid(pesel: str) -> bool:
    if re.match(PATTERN, pesel):
        return True
    else:
        return False


def is_pesel_woman(pesel: str) -> bool:
    """
    Check whether PESEL is woman's.
    If the second to last number is even,
    then PESEL is woman's, in other case PESEL is man's.
    """
    ...
    if int(pesel[-2]) % 2 == 0:
        return True
    else:
        return False
