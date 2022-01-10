"""
* Assignment: Datetime Timezone ZoneInfo
* Complexity: easy
* Lines of code: 13 lines
* Time: 13 min

English:
    1. Create `zoneinfo.ZoneInfo` object of:
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
    1. Stwórz obiekt `zoneinfo.ZoneInfo` z:
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

    >>> assert isinstance(utc, ZoneInfo), \
    'Variable `utc` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(london, ZoneInfo), \
    'Variable `london` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(moscow, ZoneInfo), \
    'Variable `moscow` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(warsaw, ZoneInfo), \
    'Variable `warsaw` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(tokyo, ZoneInfo), \
    'Variable `tokyo` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(sydney, ZoneInfo), \
    'Variable `sydney` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(auckland, ZoneInfo), \
    'Variable `auckland` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(new_york, ZoneInfo), \
    'Variable `new_york` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(cape_canaveral, ZoneInfo), \
    'Variable `cape_canaveral` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(houston, ZoneInfo), \
    'Variable `houston` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(bajkonur, ZoneInfo), \
    'Variable `bajkonur` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(north_pole, ZoneInfo), \
    'Variable `north_pole` has invalid type, must be a ZoneInfo'
    >>> assert isinstance(south_pole, ZoneInfo), \
    'Variable `south_pole` has invalid type, must be a ZoneInfo'

    >>> utc.key
    'UTC'
    >>> london.key
    'Europe/London'
    >>> moscow.key
    'Europe/Moscow'
    >>> warsaw.key
    'Europe/Warsaw'
    >>> tokyo.key
    'Asia/Tokyo'
    >>> sydney.key
    'Australia/Sydney'
    >>> auckland.key
    'Pacific/Auckland'
    >>> new_york.key
    'America/New_York'
    >>> cape_canaveral.key
    'America/New_York'
    >>> houston.key
    'America/Chicago'
    >>> bajkonur.key
    'Asia/Almaty'
    >>> north_pole.key
    'Arctic/Longyearbyen'
    >>> south_pole.key
    'Europe/Warsaw'
"""

from zoneinfo import ZoneInfo


# ZoneInfo: timezone in UTC
utc = ...

# ZoneInfo: timezone in London, United Kingdom
london = ...

# ZoneInfo: timezone in Moscow, Russian Federation
moscow = ...

# ZoneInfo: timezone in Warsaw, Poland
warsaw = ...

# ZoneInfo: timezone in Tokyo, Japan
tokyo = ...

# ZoneInfo: timezone in Sydney, Australia
sydney = ...

# ZoneInfo: timezone in Auckland, New Zealand
auckland = ...

# ZoneInfo: timezone in New York, USA
new_york = ...

# ZoneInfo: timezone in Cape Canaveral, FL, USA
cape_canaveral = ...

# ZoneInfo: timezone in Houston, TX, USA= ...
houston = ...

# ZoneInfo: timezone in Bajkonur Cosmodrome, Kazachstan
bajkonur = ...

# ZoneInfo: timezone in North Pole
north_pole = ...

# ZoneInfo: timezone in South Pole
south_pole = ...
