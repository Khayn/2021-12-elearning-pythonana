"""
* Assignment: Loop Nested Mean
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Calculate mean `Sepal length` value
    2. Run doctests - all must succeed

Polish:
    1. Wylicz średnią wartość `Sepal length`
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> result is not Ellipsis
    True
    >>> type(result)
    <class 'float'>

    >>> result
    5.911111111111111
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
    (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    (7.6, 3.0, 6.6, 2.1, 'virginica'),
    (4.6, 3.1, 1.5, 0.2, 'setosa'),
]

# float: arithmetic mean from `Sepal length` column

sepal = [x for line in DATA[1:] for x in line[0:1]]


result = sum(sepal) / len(sepal)
