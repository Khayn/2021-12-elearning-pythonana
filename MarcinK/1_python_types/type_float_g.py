"""
* Assignment: Type Float Percent
* Required: no
* Complexity: medium
* Lines of code: 2 lines
* Time: 3 min

English:
    1. International Standard Atmosphere (ISA) at sea level is
       1 ata = 1013.25 hPa
    2. Calculate `pO2` - partial pressure of Oxygen at sea level in hPa
    3. Round result to one decimal place
    4. To calculate partial pressure use ratio
       (100% is 1013.25 hPa, 20.946% is how many hPa?)
    5. Run doctests - all must succeed

Polish:
    1. Międzynarodowa standardowa atmosfera (ISA) na poziomie morza wynosi
       1 ata = 1013.25 hPa
    2. Oblicz `pO2` - ciśnienie parcjalne tlenu na poziomie morza w hPa
    3. Wynik zaokrąglij do jednego miejsca po przecinku
    4. Aby policzyć ciśnienie parcjalne skorzystaj z proporcji
       (100% to 1013.25 hPa, 20.946% to ile hPa?)
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 hPa = 100 Pa
    * 1 kPa = 1000 Pa
    * 1 ata = 1013.25 hPa (ISA - International Standard Atmosphere)
    * Atmosphere gas composition:

        * Nitrogen 78.084%
        * Oxygen 20.946%
        * Argon 0.9340%
        * Carbon Dioxide 0.0407%
        * Others 0.001%

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert pO2 is not Ellipsis, \
    'Assign result to variable: `pO2`'
    >>> assert type(pO2) is float, \
    'Variable `pO2` has invalid type, should be float'

    >>> pO2
    212.2
"""

PERCENT = 100
N2 = 78.084 / PERCENT
O2 = 20.946 / PERCENT
Ar = 0.9340 / PERCENT
CO2 = 0.0407 / PERCENT
Others = 0.001 / PERCENT

Pa = 1
hPa = 100 * Pa
kPa = 1000 * Pa

# float: pressure at sea level: 1013.25 hectopascals
ata = 1013.25*hPa

# float: 20.946% of pressure at sea level in hPa, round to one decimal place
pO2 = round(ata*O2/hPa, 1)
