"""
* Assignment: Function Scope Global
* Required: yes
* Complexity: easy
* Lines of code: 5 lines
* Time: 8 min

English:
    1. Define in global scope `SELECT: set[str]` with values:
       `'setosa', 'versicolor'`
    2. Define function `sumif(features, label)`
    3. Function sums `features`, only when `label` is in `SELECT`
    4. When `label` is not in `select` return `0` (zero)
    5. Run doctests - all must succeed

Polish:
    1. Zdefiniuj w przestrzeni globalnej `SELECT: set[str]` z wartościami:
       `'setosa', 'versicolor'`
    2. Zdefiniuj funkcję `sumif(features, label)`
    3. Funkcja sumuje `features`, tylko gdy `label` jest w `SELECT`
    4. Gdy `label` nie występuje w `select` zwróć `0` (zero)
    5. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from inspect import isfunction

    >>> isfunction(sumif)
    True
    >>> sum(sumif(X,y) for *X, y in DATA[1:])
    49.1
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, 'virginica'),
    (5.1, 3.5, 1.4, 0.2, 'setosa'),
    (5.7, 2.8, 4.1, 1.3, 'versicolor'),
    (6.3, 2.9, 5.6, 1.8, 'virginica'),
    (6.4, 3.2, 4.5, 1.5, 'versicolor'),
    (4.7, 3.2, 1.3, 0.2, 'setosa'),
]


SELECT = {'setosa', 'versicolor'}


def sumif(features, labels):
    suma = 0
    if labels in SELECT:
        suma += sum(features)
    return suma



