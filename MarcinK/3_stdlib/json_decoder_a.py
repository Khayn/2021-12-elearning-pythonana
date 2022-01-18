"""
* Assignment: JSON Decoder Martian
* Complexity: medium
* Lines of code: 11 lines
* Time: 13 min

English:
    1. Define `result: dict` with decoded `DATA` from JSON
    2. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict` z odkodowanym `DATA` z JSON
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isclass

    >>> assert isclass(Decoder), \
    'Decoder must be a class'

    >>> assert issubclass(Decoder, json.JSONDecoder), \
    'Decoder must inherit from `json.JSONDecoder`'

    >>> assert type(result) is dict, \
    'Result must be a dict'

    >>> assert len(result) > 0, \
    'Result cannot be empty'

    >>> assert all(type(key) is str
    ...            and type(value) in (str, datetime, list)
    ...            for key, value in result.items()), \
    'All keys must be str and all values must be either str, datetime or list'


    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'mission': 'Ares 3',
     'launch_date': datetime.datetime(2035, 6, 29, 0, 0),
     'destination': 'Mars',
     'destination_landing': datetime.datetime(2035, 11, 7, 0, 0),
     'destination_location': 'Acidalia Planitia',
     'crew': [{'name': 'Melissa Lewis', 'born': datetime.date(1995, 7, 15)},
              {'name': 'Rick Martinez', 'born': datetime.date(1996, 1, 21)},
              {'name': 'Alex Vogel', 'born': datetime.date(1994, 11, 15)},
              {'name': 'Chris Beck', 'born': datetime.date(1999, 8, 2)},
              {'name': 'Beth Johansen', 'born': datetime.date(2006, 5, 9)},
              {'name': 'Mark Watney', 'born': datetime.date(1994, 10, 12)}]}
"""

import json
from datetime import datetime


DATA = """
    {"mission": "Ares 3",
     "launch_date": "2035-06-29T00:00:00",
     "destination": "Mars",
     "destination_landing": "2035-11-07T00:00:00",
     "destination_location": "Acidalia Planitia",
     "crew": [{"name": "Melissa Lewis", "born": "1995-07-15"},
              {"name": "Rick Martinez", "born": "1996-01-21"},
              {"name": "Alex Vogel", "born": "1994-11-15"},
              {"name": "Chris Beck", "born": "1999-08-02"},
              {"name": "Beth Johansen", "born": "2006-05-09"},
              {"name": "Mark Watney", "born": "1994-10-12"}]}"""


class Decoder:
    ...


# dict[str, str|list|datetime]: with decoded DATA
result = ...
