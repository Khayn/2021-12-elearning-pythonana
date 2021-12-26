"""
* Assignment: Loop Nested Unique Keys
* Required: yes
* Complexity: medium
* Lines of code: 3 lines
* Time: 8 min

English:
    1. Collect unique keys from all rows in one sequence `result`
    2. Run doctests - all must succeed

Polish:
    1. Zbierz unikalne klucze z wszystkich wierszy w jednej sekwencji `result`
    2. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `row.keys()`
    * Compare solutions with :ref:`Micro-benchmarking use case`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result is not Ellipsis
    True
    >>> type(result) in (set, list, tuple)
    True
    >>> sorted(result)
    ['Petal length', 'Petal width', 'Sepal length', 'Sepal width', 'Species']
"""

DATA = [
    {'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
    {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
    {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
    {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
    {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
    {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'},
]

# set[str]: unique keys from DATA dicts
result = list({x for line in DATA[1:] for x in line.keys()})

