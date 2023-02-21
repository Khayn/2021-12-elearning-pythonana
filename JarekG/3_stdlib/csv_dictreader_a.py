"""
* Assignment: CSV DictReader Iris
* Complexity: easy
* Lines of code: 5 lines
* Time: 5 min

English:
    1. Using `csv.DictReader` read the `FILE` content
    2. Use explicit `encoding`, `delimiter` and `quotechar`
    3. Replace column names with `FIELDNAMES`
    4. Skip the first line (header)
    5. Add rows to `result: list[dict]`
    6. Run doctests - all must succeed

Polish:
    1. Korzystając z `csv.DictReader` wczytaj zawartość pliku `FILE`
    2. Podaj jawnie `encoding`, `delimiter` oraz `quotechar`
    3. Podmień nazwy kolumn na `FIELDNAMES`
    4. Pomiń pierwszą linię (nagłówek)
    5. Dodaj wiersze do `result: list[dict]`
    6. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is dict for x in result), \
    'All rows in `result` should be dict'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [{'Sepal Length': '5.8', 'Sepal Width': '2.7', 'Petal Length': '5.1',
      'Petal Width': '1.9', 'Species': 'virginica'},
     {'Sepal Length': '5.1', 'Sepal Width': '3.5', 'Petal Length': '1.4',
      'Petal Width': '0.2', 'Species': 'setosa'},
     {'Sepal Length': '5.7', 'Sepal Width': '2.8', 'Petal Length': '4.1',
      'Petal Width': '1.3', 'Species': 'versicolor'}]
"""

import csv


DATA = """sepal_length,sepal_width,petal_length,petal_width,species
5.8,2.7,5.1,1.9,virginica
5.1,3.5,1.4,0.2,setosa
5.7,2.8,4.1,1.3,versicolor"""

FIELDNAMES = ['Sepal Length', 'Sepal Width',
              'Petal Length', 'Petal Width', 'Species']

FILE = r'_temporary.csv'

with open(FILE, mode='w') as file:
    file.write(DATA)

# list[dict]: Using `csv.DictReader` read the `FILE` content

result = []

with open(FILE, mode='rt', encoding="utf-8") as file:
    f = csv.DictReader(
        file,
        delimiter=',',
        quotechar="'",
        quoting=csv.QUOTE_ALL
    )
    for row in f:
        values = row.values()
        result.append(dict(zip(FIELDNAMES, values)))
