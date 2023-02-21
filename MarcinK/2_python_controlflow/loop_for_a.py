"""
* Assignment: Loop For Count
* Required: yes
* Complexity: easy
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Count occurrences of each color
    2.
    3. Run doctests - all must succeed

Polish:
    1. Zlicz wystąpienia każdego z kolorów
    2. Nie używaj `list.count()`
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(red)
    <class 'int'>
    >>> type(green)
    <class 'int'>
    >>> type(blue)
    <class 'int'>
    >>> red
    3
    >>> green
    2
    >>> blue
    2
"""

DATA = ['red', 'green', 'blue', 'red', 'green', 'red', 'blue']

# int: number of 'red' elements in DATA
red = 0
for i in DATA:

    if i == 'red':
        red += 1
    else:
        continue

# int: number of 'green' elements in DATA
green = 0
for i in DATA:

    if i == 'green':
        green += 1
    else:
        continue
# int: number of 'blue' elements in DATA
blue = 0
for i in DATA:

    if i == 'blue':
        blue += 1
    else:
        continue