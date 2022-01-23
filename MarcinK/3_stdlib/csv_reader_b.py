"""
* Assignment: CSV Reader Substitute
* Complexity: easy
* Lines of code: 6 lines
* Time: 5 min

English:
    1. Using `csv.reader()` read data from `FILE`
    2. Define `result: list[tuple]` with converted data
    3. Use Unix `\n` line terminator
    4. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.reader()` wczytaj dane z `FILE`
    2. Zdefiniuj `result: list[tuple]` z przekonwerowanymi danymi
    3. Użyj zakończenia linii Unix `\n`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is list, \
    'Variable `result` has invalid type, should be list'
    >>> assert all(type(x) is tuple for x in result), \
    'All rows in `result` should be tuple'

    >>> result  # doctest: +NORMALIZE_WHITESPACE
    [('5.8', '2.7', '5.1', '1.9', 'virginica'),
     ('5.1', '3.5', '1.4', '0.2', 'setosa'),
     ('5.7', '2.8', '4.1', '1.3', 'versicolor')]

    >>> remove(FILE)
"""

import csv


FILE = r'_temporary.csv'

DATA = """5.8,2.7,5.1,1.9,1
5.1,3.5,1.4,0.2,0
5.7,2.8,4.1,1.3,2"""

SPECIES = {
    0: 'setosa',
    1: 'virginica',
    2: 'versicolor'}

with open(FILE, mode='w') as file:
    file.write(DATA)

# list[tuple]: data from file (note the list[tuple] format!)

data = []
with open(FILE, mode='rt') as file:
    dane = csv.reader(file)

    for line in dane:
        data.append(tuple(line))

result = []

for row in data:
    params = []
    for col in row:
        try:
            params.append(SPECIES.get(int(col)))
        except:
            params.append(col)
    result.append(tuple(params))

print(result)
