"""
* Assignment: Loop Unpacking Endswith
* Required: yes
* Complexity: medium
* Lines of code: 4 lines
* Time: 13 min

English:
    1. Define `result: set[str]`
    2. Iterating over data unpack row to `*features` and `label`
    3. Append to `result` species with endings in `SUFFIXES`
    4. Run doctests - all must succeed

Polish:
    1. Zdefiniuj `result: set[str]`
    2. Iterując po danych rozpakuj wiersz do `*features` oraz `label`
    3. Dodaj do `result` nazwy gatunków z końcówkami w `SUFFIXES`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `str.endswith()`
    * `set.pop()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result)
    <class 'set'>

    >>> 'virginica' in result
    True
    >>> 'setosa' in result
    True
    >>> 'versicolor' in result
    False
"""

DATA = [
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
    (5.8, 2.7, 5.1, 1.9, {'virginica'}),
    (5.1, 3.5, 1.4, 0.2, {'setosa'}),
    (5.7, 2.8, 4.1, 1.3, {'versicolor'}),
    (6.3, 2.9, 5.6, 1.8, {'virginica'}),
    (6.4, 3.2, 4.5, 1.5, {'versicolor'}),
    (4.7, 3.2, 1.3, 0.2, {'setosa'}),
    (7.0, 3.2, 4.7, 1.4, {'versicolor'}),
    (7.6, 3.0, 6.6, 2.1, {'virginica'}),
    (4.6, 3.1, 1.5, 0.2, {'setosa'}),
]

SUFFIXES = ('ca', 'osa')

features: tuple
label: set
species: str

# set[str]: species names ending with 'ca' or 'osa'
result = set()

header, *data = DATA

for *features, label in data:
    species = label.pop()
    if species.endswith(SUFFIXES):
        result.add(species)

print(result)