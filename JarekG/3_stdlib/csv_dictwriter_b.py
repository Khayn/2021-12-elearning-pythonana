"""
* Assignment: CSV DictWriter Schemaless
* Complexity: medium
* Lines of code: 7 lines
* Time: 5 min

English:
    1. Using `csv.DictWriter()` write variable schema data to `FILE`
    2. `fieldnames` must be automatically generated from `DATA`
    3. Non functional requirements:
        a. All fields must be enclosed by double quote `"` character
        b. Use `;` to separate columns
        c. Use `utf-8` encoding
        d. Use Unix `\n` line terminator
        e. Sort `fieldnames` using `sorted()`
    4. Run doctests - all must succeed

Polish:
    1. Za pomocą `csv.DictWriter()` zapisz dane o zmiennej strukturze do `FILE`
    2. `fieldnames` musi być generowane automatycznie na podstawie `DATA`
    3. Wymagania niefunkcjonalne:
        a. Wszystkie pola muszą być otoczone znakiem cudzysłowu `"`
        b. Użyj `,` do oddzielenia kolumn
        c. Użyj kodowania `utf-8`
        d. Użyj zakończenia linii Unix `\n`
        e. Posortuj `fieldnames` używając `sorted()`
    4. Uruchom doctesty - wszystkie muszą się powieść

Hint:
    * For Python before 3.8: `dict(OrderedDict)`

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from os import remove
    >>> result = open(FILE).read()
    >>> remove(FILE)

    >>> assert result is not Ellipsis, \
    'Assign result to variable: `result`'
    >>> assert type(result) is str, \
    'Variable `result` has invalid type, should be str'

    >>> print(result)
    "Petal length","Petal width","Sepal length","Sepal width","Species"
    "","","5.1","3.5","setosa"
    "4.1","1.3","","","versicolor"
    "","1.8","6.3","","virginica"
    "","0.2","5.0","","setosa"
    "4.1","","","2.8","versicolor"
    "","1.8","","2.9","virginica"
    <BLANKLINE>
"""
import csv


DATA = [{'Sepal length': 5.1, 'Sepal width': 3.5, 'Species': 'setosa'},
        {'Petal length': 4.1, 'Petal width': 1.3, 'Species': 'versicolor'},
        {'Sepal length': 6.3, 'Petal width': 1.8, 'Species': 'virginica'},
        {'Sepal length': 5.0, 'Petal width': 0.2, 'Species': 'setosa'},
        {'Sepal width': 2.8, 'Petal length': 4.1, 'Species': 'versicolor'},
        {'Sepal width': 2.9, 'Petal width': 1.8, 'Species': 'virginica'}]

FILE = r'_temporary.csv'


# ContextManager: Write DATA to FILE, generate header from DATA

fieldnames = {field for row in DATA for field in row.keys()}
fieldnames = sorted(fieldnames)

with open(FILE, mode='w', encoding='utf-8') as file:
    f = csv.DictWriter(
        file,
        quotechar='"',
        delimiter=',',
        quoting=csv.QUOTE_ALL,
        lineterminator='\n',
        fieldnames=fieldnames
    )
    f.writeheader()
    f.writerows(DATA)
