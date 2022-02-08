"""
* Assignment: Sequence Slice Train/Test
* Required: yes
* Complexity: easy
* Lines of code: 4 lines
* Time: 8 min

English:
    1. Divide `data` into two lists:
       a. `train`: 60% - training data
       b. `test`: 40% - testing data
    2. Calculate split point:
       a. `data` length multiplied by percent
       b. From `data` slice training data from start to split
       c. From `data` slice test data from split to end
    3. Run doctests - all must succeed

Polish:
    1. Podziel `data` na dwie listy:
       a. `train`: 60% - dane do uczenia
       b. `test`: 40% - dane do testów
    2. Aby to zrobić wylicz punkt podziału:
       a. Długość `data` razy procent
       c. Z `data` wytnij do uczenia rekordy od początku do punktu podziału
       d. Z `data` zapisz do testów rekordy od punktu podziału do końca
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert split is not Ellipsis, \
    'Assign result to variable: `split`'
    >>> assert train is not Ellipsis, \
    'Assign result to variable: `train`'
    >>> assert test is not Ellipsis, \
    'Assign result to variable: `test`'
    >>> assert type(split) is int, \
    'Variable `split` has invalid type, should be int'
    >>> assert type(train) is list, \
    'Variable `train` has invalid type, should be list'
    >>> assert type(train) is list, \
    'Variable `train` has invalid type, should be list'
    >>> assert type(test) is list, \
    'Variable `test` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in train), \
    'All elements in `train` should be tuple'
    >>> assert all(type(x) is tuple for x in test), \
    'All elements in `test` should be tuple'

    >>> split
    6

    >>> train  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa')]

    >>> test  # doctest: +NORMALIZE_WHITESPACE
    [(7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 3.0, 1.4, 0.2, 'setosa'),
     (4.9, 2.5, 4.5, 1.7, 'virginica')]
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
    (4.9, 3.0, 1.4, 0.2, 'setosa'),
    (4.9, 2.5, 4.5, 1.7, 'virginica')]


header = DATA[0]
data = DATA[1:]

# int: `data` length multiplied by percent
split = ...

# list[tuple]: first 60% from data
train = ...

# list[tuple]: last 40% from data
test = ...
