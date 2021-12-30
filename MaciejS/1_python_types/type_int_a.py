"""
* Assignment: Type Int Add
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 3 min

English:
    1. One Kelvin is equal to 1 Celsius degree (1K = 1°C)
    2. Zero Celsius degrees is equal to 273.15 Kelvins
    3. For calculation use round number 273 (0°C = 273K)
    4. How many Kelvins has average temperatures at surface [1]:
        a. Mars highest: 20 °C
        b. Mars lowest: -153 °C
        c. Mars average: −63 °C
    5. Run doctests - all must succeed

Polish:
    1. Jeden Kelwin to jeden stopień Celsiusza (1K = 1°C)
    2. Zero stopni Celsiusza to 273.15 Kelwiny
    3. W zadaniu przyjmij równe 273°C (0°C = 273K)
    4. Ile Kelwinów wynoszą średnie temperatury powierzchni [1]:
        a. Mars najwyższa: 20 °C
        b. Mars najniższa: -153 °C
        c. Mars średnia: −63 °C
    5. Uruchom doctesty - wszystkie muszą się powieść

References:
    [1] Centro de Astrobiología (CSIC-INTA).
        Rover Environmental Monitoring Station, Mars Science Laboratory (NASA).
        Year: 2019.
        Retrieved: 2019-08-06.
        URL: http://cab.inta-csic.es/rems/marsweather.html

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert mars_max is not Ellipsis, \
    'Assign result to variable: `mars_max`'
    >>> assert mars_min is not Ellipsis, \
    'Assign result to variable: `mars_min`'
    >>> assert mars_min is not Ellipsis, \
    'Assign result to variable: `mars_min`'
    >>> assert type(mars_max) is int, \
    'Variable `mars_max` has invalid type, should be int'
    >>> assert type(mars_min) is int, \
    'Variable `mars_min` has invalid type, should be int'
    >>> assert type(mars_min) is int, \
    'Variable `mars_avg` has invalid type, should be int'

    >>> assert mars_max == 293, \
    'Invalid value for `mars_max`, should be 293. Check you calculation'

    >>> assert mars_min == 120, \
    'Invalid value for `mars_min`, should be 120. Check you calculation'

    >>> assert mars_avg == 210, \
    'Invalid value for `mars_avg`, should be 210. Check you calculation'

"""

Celsius = 1
Kelvin = 273

MARS_MAX = 20 * Celsius
MARS_MIN = -153 * Celsius
MARS_AVG = -63 * Celsius

# int: 20 Celsius in Kelvin
mars_max = ...

# int: -153 Celsius in Kelvin
mars_min = ...

# int: -63 Celsius in Kelvin
mars_avg = ...
