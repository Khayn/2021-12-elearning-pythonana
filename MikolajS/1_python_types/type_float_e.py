"""
* Assignment: Type Float Velocity
* Required: yes
* Complexity: easy
* Lines of code: 9 lines
* Time: 3 min

English:
    1. Speed limit is 75 MPH
    2. Data uses imperial (US) system
    3. Convert to metric (SI) system
    4. Speed limit print in KPH (km/h)
    5. Round speed limit to one decimal place
    6. Run doctests - all must succeed

Polish:
    1. Ograniczenie prędkości wynosi 75 MPH
    2. Dane używają systemu imperialnego (US)
    3. Przelicz je na system metryczny (układ SI)
    4. Ograniczenie prędkości wypisz w KPH (km/h)
    5. Zaokrąglij ograniczenie prędkości do jednego miejsca po przecinku
    6. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert kph is not Ellipsis, \
    'Assign result to variable: `kph`'
    >>> assert mph is not Ellipsis, \
    'Assign result to variable: `mph`'
    >>> assert speed_limit_mph is not Ellipsis, \
    'Assign result to variable: `speed_limit_mph`'
    >>> assert speed_limit_kph is not Ellipsis, \
    'Assign result to variable: `speed_limit_kph`'
    >>> assert type(kph) is float, \
    'Variable `kph` has invalid type, should be float'
    >>> assert type(mph) is float, \
    'Variable `mph` has invalid type, should be float'
    >>> assert type(speed_limit_mph) is float, \
    'Variable `speed_limit_mph` has invalid type, should be float'
    >>> assert type(speed_limit_kph) is float, \
    'Variable `speed_limit_kph` has invalid type, should be float'

    >>> round(mph, 3)
    0.447
    >>> round(kph, 3)
    0.278
    >>> speed_limit_mph
    75.0
    >>> speed_limit_kph
    120.7
"""

SECOND = 1
MINUTE = 60 * SECOND
HOUR = 60 * MINUTE

m = 1
km = 1000 * m
mi = 1609.344 * m

# float: miles per hour
mph = mi / HOUR
print(f'{mph=} m/s')

# float: kilometers per hour
kph = km / HOUR
print(f'{kph=:.3f} m/s')

# float: 75 miles per hour
speed_limit = 75 * mph
print(f'{speed_limit=} m/s')

# float: speed limit in miles per hour, round to one decimal place
speed_limit_mph = round(speed_limit / mph, 1)
print(f'{speed_limit_mph=} mph')

# float: speed limit in kilometers per hour, round to one decimal place
speed_limit_kph = round(speed_limit / kph, 1)
print(f'{speed_limit_kph=} kph')

