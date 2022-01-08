"""
* Assignment: Sequence GetItem Header/Data
* Required: yes
* Complexity: easy
* Lines of code: 11 lines
* Time: 5 min

English:
    1. Separate header (first line) from data:
       a. Define `header: tuple[str]` with header
       b. Define `data: list[tuple]` with other data without header
    2. Non-functional requirements:
       a. Use only indexes (`getitem`)
       b. Do not use `str.split()`, `slice`, `for`, `while` or any other
          control-flow statement
       c. You can use copy and paste and/or vertical select (`alt`)
    3. Run doctests - all must succeed

Polish:
    1. Odseparuj nagłówek (pierwsza linia) od danych:
       a. Zdefiniuj `header: tuple[str]` z nagłówkiem
       b. Zdefiniuj `data: list[tuple]` z danymi bez nagłówka
    2. Wymagania niefunkcjonalne:
       a. Korzystaj tylko z indeksów (`getitem`)
       b. Nie używaj `str.split()`, `slice`, `for`, `while` lub
          jakiejkolwiek innej instrukcji sterującej
       c. Możesz użyć kopiowania i wklejania lub/i zaznaczania pioniwego (`alt`)
    3. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `list.append()`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> assert header is not Ellipsis, \
    'Assign result to variable: `header`'
    >>> assert data is not Ellipsis, \
    'Assign result to variable: `data`'
    >>> assert type(header) is tuple, \
    'Variable `header` has invalid type, should be tuple'
    >>> assert all(type(x) is tuple for x in data), \
    'All elements in `data` should be tuple'
    >>> assert header not in data, \
    'Header should not be in `data`'

    >>> header
    ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species')

    >>> data  # doctest: +NORMALIZE_WHITESPACE
    [(5.8, 2.7, 5.1, 1.9, 'virginica'),
     (5.1, 3.5, 1.4, 0.2, 'setosa'),
     (5.7, 2.8, 4.1, 1.3, 'versicolor'),
     (6.3, 2.9, 5.6, 1.8, 'virginica'),
     (6.4, 3.2, 4.5, 1.5, 'versicolor'),
     (4.7, 3.2, 1.3, 0.2, 'setosa'),
     (7.0, 3.2, 4.7, 1.4, 'versicolor'),
     (7.6, 3.0, 6.6, 2.1, 'virginica'),
     (4.9, 3.0, 1.4, 0.2, 'setosa')]
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

# tuple[str]: with row at index 0 from DATA
header = tuple(DATA[0])

# list[tuple]: with rows at all the other indexes from DATA (use only getitem)
data = list(DATA[1:len(DATA)])

print(header)
print(data)