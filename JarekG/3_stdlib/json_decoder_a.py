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
import re
from datetime import datetime, date, time, timedelta


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


class Decoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, object_hook=self.default)

    @staticmethod
    def str2date(date):
        if ':' in date:
            return datetime.fromisoformat(date)
        else:
            return datetime.fromisoformat(date).date()

    def default(self, data: dict) -> dict:
        date = r'\d{4}-\d{2}-\d{2}'
        time = r'\d{2}:\d{2}:\d{2}'
        pattern = rf'^({date})(T{time})?$'
        for key, value in data.items():
            if not isinstance(value, str):
                continue
            if re.search(pattern, value):
                data[key] = self.str2date(value)
        return data

# dict[str, str|list|datetime]: with decoded DATA


decoder = Decoder()
result = decoder.decode(DATA)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        super().__init__(object_hook=lambda data: {
                field: self.default(field, value)
                for field, value in data.items()})

    def default(self, field, value):
        result = {
            'born': lambda x: date.fromisoformat(x),
            'launch': lambda x: datetime.fromisoformat(x),
            'landing': lambda x: time.fromisoformat(x),
            'duration': lambda x: timedelta(days=x),
        }.get(field, value)
        return result(value) if callable(result) else result
