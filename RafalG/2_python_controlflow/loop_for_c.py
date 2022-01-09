"""
* Assignment: Loop For Segmentation
* Required: yes
* Complexity: easy
* Lines of code: 10 lines
* Time: 8 min

English:
    1. Count occurrences of each group
    2. Define groups:
        a. `small` - numbers in range [0-3)
        b. `medium` - numbers in range [3-7)
        c. `large` - numbers in range [7-10)
    3. Run doctests - all must succeed

Polish:
    1. Policz wystąpienia każdej z group
    2. Zdefiniuj grupy:
        a. `small` - liczby z przedziału <0-3)
        b. `medium` - liczby z przedziału <3-7)
        c. `large` - liczby z przedziału <7-10)
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'dict'>

    >>> assert all(type(x) is str for x in result.keys())
    >>> assert all(type(x) is int for x in result.values())

    >>> result
    {'small': 16, 'medium': 19, 'large': 15}
"""

DATA = [1, 4, 6, 7, 4, 4, 4, 5, 1, 7, 0,
        0, 6, 5, 0, 0, 9, 7, 0, 4, 4, 8,
        2, 4, 0, 0, 1, 9, 1, 7, 8, 8, 9,
        1, 3, 5, 6, 8, 2, 8, 1, 3, 9, 5,
        4, 8, 1, 9, 6, 3]

# dict[str,int] number of digit occurrences in segments
result = {'small': 0, 'medium': 0, 'large': 0}

for number in DATA:
    if number < 3:
        result["small"] += 1
    elif 3 <= number < 7:
        result["medium"] += 1
    elif 7 <= number < 10:
        result["large"] += 1