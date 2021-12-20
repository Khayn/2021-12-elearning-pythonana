"""
* Assignment: Type Int Bytes
* Required: no
* Complexity: easy
* Lines of code: 7 lines
* Time: 3 min

English:
    1. File size is 100 megabytes
    2. Calculate size in kilobytes
    2. Calculate size in megabits
    3. Run doctests - all must succeed

Polish:
    1. Wielkość pliku to 100 megabajtów
    2. Oblicz wielkość w kilobajtach
    2. Oblicz wielkość w megabitach
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * 1 Kb = 1024 b
    * 1 Mb = 1024 Kb
    * 1 B = 8 b
    * 1 KB = 1024 B
    * 1 MB = 1024 KB

Tests:
    >>> import sys; sys.tracebacklimit = 0


    >>> assert size_kB is not Ellipsis, \
    'Assign result to variable: `size_kB`'
    >>> assert size_Mb is not Ellipsis, \
    'Assign result to variable: `size_Mb`'
    >>> assert type(size_kB) is int, \
    'Variable `size_kB` has invalid type, should be int'
    >>> assert type(size_Mb) is int, \
    'Variable `size_Mb` has invalid type, should be int'

    >>> size_kB
    102400
    >>> size_Mb
    800
"""

b = 1
kb = 1024 * b
Mb = 1024 * kb

B = 8 * b
kB = 1024 * B
MB = 1024 * kB

SIZE = 100 * MB

# int: SIZE in kilobytes
size_kB = ...

# int: SIZE in megabits
size_Mb = ...
