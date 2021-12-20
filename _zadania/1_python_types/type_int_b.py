"""
* Assignment: Type Int Sub
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Kelvin (absolute) is equal to -273.15 Celsius degrees
    3. For calculation use round number -273 (0K = -273°C)
    4. How many Celsius degrees has average temperatures at surface [1]:
        a. Lunar day: 453 K
        b. Lunar night: 93 K
    5. Run doctests - all must succeed

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero Kelwina (bezwzględne) to -273.15 stopni Celsiusza
    3. W zadaniu przyjmij równe -273°C (0K = -273°C)
    4. Ile stopni Celsiusza wynoszą średnie temperatury powierzchni [1]:
        a. Księżyca w dzień: 453 K
        b. Księżyca w nocy: 93 K
    5. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Centro de Astrobiología (CSIC-INTA).
        Rover Environmental Monitoring Station, Mars Science Laboratory (NASA).
        Year: 2019.
        Retrieved: 2019-08-06.
        URL: http://cab.inta-csic.es/rems/marsweather.html

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert lunar_day is not Ellipsis, \
    'Assign result to variable: `lunar_day`'
    >>> assert lunar_night is not Ellipsis, \
    'Assign result to variable: `lunar_night`'
    >>> assert type(lunar_day) is int, \
    'Variable `lunar_day` has invalid type, should be int'
    >>> assert type(lunar_night) is int, \
    'Variable `lunar_night` has invalid type, should be int'

    >>> lunar_day
    180
    >>> lunar_night
    -180
"""

Celsius = 273
Kelvin = 1

LUNAR_DAY = 453*Kelvin
LUNAR_NIGHT = 93*Kelvin

# int: 453 Kelvins in Celsius
lunar_day = ...

# int: 93 Kelvins in Celsius
lunar_night = ...
