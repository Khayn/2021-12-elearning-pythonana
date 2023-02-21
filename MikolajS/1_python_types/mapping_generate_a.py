"""
* Assignment: Mapping Generate Pairs
* Required: yes
* Complexity: easy
* Lines of code: 1 lines
* Time: 3 min

English:
    1. Define `result: dict`
    2. Convert `DATA` to `dict` and assign to `result`
    3. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: dict`
    2. Przekonwertuj `DATA` do `dict` i przypisz do `result`
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `dict()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert type(result) is dict, \
    'Variable `result` has invalid type, should be dict'

    >>> assert all(type(x) is str for x in result.keys()), \
    'All dict keys should be str'

    >>> assert 'Sepal length' in result.keys()
    >>> assert 'Sepal width' in result.keys()
    >>> assert 'Petal length' in result.keys()
    >>> assert 'Petal width' in result.keys()
    >>> assert 'Species' in result.keys()

    >>> assert 5.8 in result.values()
    >>> assert 2.7 in result.values()
    >>> assert 5.1 in result.values()
    >>> assert 1.9 in result.values()
    >>> assert 'virginica' in result.values()

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    {'Sepal length': 5.8,
     'Sepal width': 2.7,
     'Petal length': 5.1,
     'Petal width': 1.9,
     'Species': 'virginica'}
"""

DATA = [
    ('Sepal length', 5.8),
    ('Sepal width', 2.7),
    ('Petal length', 5.1),
    ('Petal width', 1.9),
    ('Species', 'virginica')]

# dict[str,float|str]: converted DATA to dict
result = dict(DATA)
