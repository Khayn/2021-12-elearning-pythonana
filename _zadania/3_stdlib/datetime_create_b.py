"""
* Assignment: Datetime Create Combine
* Complexity: easy
* Lines of code: 1 lines
* Time: 2 min

English:
    1. First human (Yuri Gagarin) flown to space on
       April 12th, 1961 at 6:07 a.m. from Bajkonur Cosmodrome in Kazahstan
    2. Combine date and time into `datetime` object representing
       exact moment of the launch
    3. Use `datetime.combine()`
    4. Run doctests - all must succeed

Polish:
    1. Pierwszy człowiek (Juri Gagarin) poleciał w kosmos
       12 kwietnia 1961 roku o 6:07 rano z kosmodromu Bajkonur w Kazachstanie
    2. Połącz datę i czas w obiekt `datetime` reprezentujący
       dokładny moment startu
    3. Użyj `datetime.combine()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is datetime, \
    'Variable `result` has invalid type, must be a datetime'

    >>> print(result)
    1961-04-12 06:07:00
"""

from datetime import date, datetime, time

d = date(1961, 4, 12)
t = time(6, 7)

# datetime: combine d and t to represent April 12th, 1961 6:07 a.m.
result = ...
