"""
* Assignment: Type Float Distance
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Convert units
    2. Instead `...` substitute calculated and converted values
    3. Note the number of decimal places
    4. Run doctests - all must succeed

Polish:
    1. Przekonwertuj jednostki
    2. Zamiast `...` podstaw wyliczone i przekonwertowane wartości
    3. Zwróć uwagę na ilość miejsc po przecinku
    4. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert meters is not Ellipsis, \
    'Assign result to variable: `meters`'
    >>> assert kilometers is not Ellipsis, \
    'Assign result to variable: `kilometers`'
    >>> assert miles is not Ellipsis, \
    'Assign result to variable: `miles`'
    >>> assert nautical_miles is not Ellipsis, \
    'Assign result to variable: `nautical_miles`'
    >>> assert all_units is not Ellipsis, \
    'Assign result to variable: `all_units`'
    >>> assert type(meters) is str, \
    'Variable `volume` has invalid type, should be str'
    >>> assert type(kilometers) is str, \
    'Variable `volume` has invalid type, should be str'
    >>> assert type(miles) is str, \
    'Variable `volume` has invalid type, should be str'
    >>> assert type(nautical_miles) is str, \
    'Variable `volume` has invalid type, should be str'
    >>> assert type(all_units) is str, \
    'Variable `volume` has invalid type, should be str'

    >>> meters
    'Meters: 1337'
    >>> kilometers
    'Kilometers: 1'
    >>> miles
    'Miles: 0.83'
    >>> nautical_miles
    'Nautical Miles: 0.722'
    >>> all_units
    'km: 1, mi: 0.8, NM: 0.72'
"""

m = 1
km = 1000 * m
mi = 1609.344 * m
NM = 1852 * m

distance = 1337 * m
distance_m = distance / m
distance_km = distance / km
distance_mi = distance / mi
distance_NM = distance / NM

# str: distance in meters 0 decimal places
meters = f'Meters: {...}'

# str: distance in kilometers with 0 decimal places
kilometers = f'Kilometers: {...}'

# str: distance in miles with 2 decimal places
miles = f'Miles: {...}'

# str: distance in nautical miles with 3 decimal places
nautical_miles = f'Nautical Miles: {...}'

# str: distance in km, mi, NM with 0, 1, 2 decimal places
all_units = (f'km: {...}, '
             f'mi: {...}, '
             f'NM: {...}')
