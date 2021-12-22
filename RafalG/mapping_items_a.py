"""
* Assignment: Mapping Items List
* Required: yes
* Complexity: easy
* Lines of code: 3 lines
* Time: 3 min

English:
    1. Define `keys: list[str]` with list of `DATA` keys
    2. Define `values: list[str]` with list of `DATA` values
    3. Define `items: list[tuple]` with list of `DATA` key-value pairs
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `keys: list[str]` z listą kluczy z `DATA`
    2. Zdefiniuj `values: list[str]` z listą wartości z `DATA`
    3. Zdefiniuj `items: list[tuple]` z listą par klucz-wartość z `DATA`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list()`
    * `dict.keys()`
    * `dict.values()`
    * `dict.items()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(keys) is list, \
    'Variable `keys` has invalid type, should be list'

    >>> assert type(values) is list, \
    'Variable `values` has invalid type, should be list'

    >>> assert type(items) is list, \
    'Variable `items` has invalid type, should be list'

    >>> assert all(type(x) is tuple for x in items), \
    'All rows in items should be tuples'

    >>> keys
    ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']

    >>> values
    [5.8, 2.7, 5.1, 1.9]

    >>> items  # doctest: +NORMALIZE_WHITESPACE
    [('Sepal length', 5.8),
     ('Sepal width', 2.7),
     ('Petal length', 5.1),
     ('Petal width', 1.9)]
"""

DATA = {'Sepal length': 5.8,
        'Sepal width': 2.7,
        'Petal length': 5.1,
        'Petal width': 1.9}

# list[str]: with keys from DATA
keys = [*DATA.keys()]

# list[float]: with values from DATA
values = [*DATA.values()]

# list[tuple]: with key-value pairs from DATA
items = [*DATA.items()]
