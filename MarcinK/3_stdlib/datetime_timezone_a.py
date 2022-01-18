"""
* Assignment: Datetime Timezone Pytz
* Complexity: easy
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Create `pytz.timezone` object of:
        a. UTC
        b. London, United Kingdom
        c. Moscow, Russian Federation
        d. Warsaw, Poland
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, New Zealand
        h. New York, USA
    2. Use `List of tz database time zones` [1]
    3. Run doctests - all must succeed

Polish:
    1. Stwórz obiekt `pytz.timezone` z:
        a. UCT
        b. London, Wielka Brytania
        c. Moscow, Rosja
        d. Warsaw, Polska
        e. Tokyo, Japan
        f. Sydney, Australia
        g. Auckland, Nowa Zelandia
        h. New York, USA
    2. Użyj `List of tz database time zones` [1]
    3. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Wikipedia. List of tz database time zones.
        URL: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
        Retrieved: 2021-03-24
    [2] IANA. Time Zone Database.
        URL: https://data.iana.org/time-zones/releases/
        Retrieved: 2021-03-24

Extra Task:
    1. Cape Canaveral, FL, USA
    2. Houston, TX, USA
    3. Bajkonur Cosmodrome, Kazachstan
    5. North Pole
    6. South Pole (Henryk Arctowski Polish Antarctic Station)

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pytz.tzinfo import DstTzInfo, BaseTzInfo

    >>> assert utc is not Ellipsis, \
    'Assign value to variable `utc` has instead of Ellipsis (...)'
    >>> assert london is not Ellipsis, \
    'Assign value to variable `london` instead of Ellipsis (...)'
    >>> assert moscow is not Ellipsis, \
    'Assign value to variable `moscow` instead of Ellipsis (...)'
    >>> assert warsaw is not Ellipsis, \
    'Assign value to variable `warsaw` instead of Ellipsis (...)'
    >>> assert tokyo is not Ellipsis, \
    'Assign value to variable `tokyo` instead of Ellipsis (...)'
    >>> assert sydney is not Ellipsis, \
    'Assign value to variable `sydney` instead of Ellipsis (...)'
    >>> assert auckland is not Ellipsis, \
    'Assign value to variable `auckland` instead of Ellipsis (...)'
    >>> assert new_york is not Ellipsis, \
    'Assign value to variable `new_york` instead of Ellipsis (...)'
    >>> assert cape_canaveral is not Ellipsis, \
    'Assign value to variable `cape_canaveral` instead of Ellipsis (...)'
    >>> assert houston is not Ellipsis, \
    'Assign value to variable `houston` instead of Ellipsis (...)'
    >>> assert bajkonur is not Ellipsis, \
    'Assign value to variable `bajkonur` instead of Ellipsis (...)'
    >>> assert north_pole is not Ellipsis, \
    'Assign value to variable `north_pole` instead of Ellipsis (...)'
    >>> assert south_pole is not Ellipsis, \
    'Assign value to variable `south_pole` instead of Ellipsis (...)'

    >>> assert isinstance(utc, BaseTzInfo), \
    'Variable `utc` has invalid type, must be a BaseTzInfo'
    >>> assert isinstance(london, DstTzInfo), \
    'Variable `london` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(moscow, DstTzInfo), \
    'Variable `moscow` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(warsaw, DstTzInfo), \
    'Variable `warsaw` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(tokyo, DstTzInfo), \
    'Variable `tokyo` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(sydney, DstTzInfo), \
    'Variable `sydney` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(auckland, DstTzInfo), \
    'Variable `auckland` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(new_york, DstTzInfo), \
    'Variable `new_york` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(cape_canaveral, DstTzInfo), \
    'Variable `cape_canaveral` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(houston, DstTzInfo), \
    'Variable `houston` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(bajkonur, DstTzInfo), \
    'Variable `bajkonur` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(north_pole, DstTzInfo), \
    'Variable `north_pole` has invalid type, must be a DstTzInfo'
    >>> assert isinstance(south_pole, DstTzInfo), \
    'Variable `south_pole` has invalid type, must be a DstTzInfo'

    >>> utc._utcoffset
    datetime.timedelta(0)
    >>> london._utcoffset
    datetime.timedelta(days=-1, seconds=86340)
    >>> moscow._utcoffset
    datetime.timedelta(seconds=9000)
    >>> warsaw._utcoffset
    datetime.timedelta(seconds=5040)
    >>> tokyo._utcoffset
    datetime.timedelta(seconds=33540)
    >>> sydney._utcoffset
    datetime.timedelta(seconds=36300)
    >>> auckland._utcoffset
    datetime.timedelta(seconds=41940)
    >>> new_york._utcoffset
    datetime.timedelta(days=-1, seconds=68640)
    >>> cape_canaveral._utcoffset
    datetime.timedelta(days=-1, seconds=68640)
    >>> houston._utcoffset
    datetime.timedelta(days=-1, seconds=65340)
    >>> bajkonur._utcoffset
    datetime.timedelta(seconds=18480)
    >>> north_pole._utcoffset
    datetime.timedelta(seconds=2580)
    >>> south_pole._utcoffset
    datetime.timedelta(seconds=5040)
"""

from pytz import timezone


# timezone in UTC
utc = ...

# timezone in London, United Kingdom
london = ...

# timezone in Moscow, Russian Federation
moscow = ...

# timezone in Warsaw, Poland
warsaw = ...

# timezone in Tokyo, Japan
tokyo = ...

# timezone in Sydney, Australia
sydney = ...

# timezone in Auckland, New Zealand
auckland = ...

# timezone in New York, USA
new_york = ...

# timezone in Cape Canaveral, FL, USA
cape_canaveral = ...

# timezone in Houston, TX, USA= ...
houston = ...

# timezone in Bajkonur Cosmodrome, Kazachstan
bajkonur = ...

# timezone in North Pole
north_pole = ...

# timezone in South Pole
south_pole = ...
